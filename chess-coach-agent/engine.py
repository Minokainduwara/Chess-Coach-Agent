import chess # type: ignore
import chess.engine # type: ignore
from config import STOCKFISH_PATH, ENGINE_CONFIG, DEPTH, MULTI_PV

engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
engine.configure(ENGINE_CONFIG)


def classify(eval_cp):
    """Simple human-like classification"""
    if eval_cp is None:
        return "unknown"

    if eval_cp > 200:
        return "winning"
    elif eval_cp > 50:
        return "slightly better"
    elif eval_cp > -50:
        return "equal"
    elif eval_cp > -200:
        return "mistake"
    else:
        return "blunder"


def analyze_fen(fen):
    board = chess.Board(fen)

    info = engine.analyse(
        board,
        chess.engine.Limit(depth=DEPTH),
        multipv=MULTI_PV
    )

    # normalize multipv
    if not isinstance(info, list):
        info = [info]

    best = info[0]

    best_move = None
    if "pv" in best and len(best["pv"]) > 0:
        best_move = best["pv"][0]

    # SAFE move validation
    if best_move and best_move not in board.legal_moves:
        best_move = None

    # score
    score_obj = best["score"].relative

    if score_obj.is_mate():
        score_cp = 100000 if score_obj.mate() > 0 else -100000
        score = f"Mate in {score_obj.mate()}"
    else:
        score_cp = score_obj.score(mate_score=100000)
        score = score_cp / 100.0

    # SAN conversion
    best_move_san = board.san(best_move) if best_move else "N/A"

    # top moves (multi PV)
    top_moves = []

    for line in info[:MULTI_PV]:
        pv = line.get("pv", [])
        if pv:
            move = pv[0]
            if move in board.legal_moves:
                top_moves.append(board.san(move))

    # evaluation classification
    label = classify(score_cp / 100.0)

    return {
        "fen": fen,
        "best_move_san": best_move_san,
        "best_move_uci": str(best_move) if best_move else "N/A",
        "evaluation": score,
        "classification": label,
        "top_moves": top_moves
    }


def close_engine():
    engine.quit()