import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci("stockfish")


def analyze_fen(fen):
    board = chess.Board(fen)

    # Stockfish analysis
    info = engine.analyse(board, chess.engine.Limit(time=0.5))

    score = info["score"].relative
    best_move = info.get("pv")[0] if "pv" in info else None

    result = {
        "fen": fen,
        "best_move": str(best_move) if best_move else "N/A",
        "score": None
    }

    if score.is_mate():
        result["score"] = f"Mate in {score.mate()}"
    else:
        result["score"] = score.score()

    return result


def close_engine():
    engine.quit()