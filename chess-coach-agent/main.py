from engine import analyze_fen, close_engine
from coach import ChessCoach


def run_cli():

    print("\n♟ Chess Engine V2 (AI Coach + Stockfish)")
    print("Type 'exit' to quit\n")

    engine_data = None
    coach = ChessCoach()

    try:
        while True:

            fen = input("Enter FEN: ").strip()

            if fen.lower() == "exit":
                break

            if not fen:
                print("⚠ Empty FEN")
                continue

            print("\n🔍 Analyzing...\n")

            engine_data = analyze_fen(fen)

            print("📊 Stockfish Result:")
            print("Best Move:", engine_data["best_move_san"])
            print("Evaluation:", engine_data["evaluation"])
            print("Type:", engine_data["classification"])
            print("Top Moves:", engine_data["top_moves"])

            print("\n🤖 AI Coach:\n")
            print(coach.explain(engine_data))

            print("\n" + "-" * 60 + "\n")

    except KeyboardInterrupt:
        print("\n⚠ Interrupted")

    finally:
        close_engine()
        print("\n👋 Engine closed safely")


if __name__ == "__main__":
    run_cli()