from engine import analyze_fen, close_engine
from coach import explain_position


def run_cli():

    print("\n♟ AI Chess FEN Analyzer")
    print("Type 'exit' to quit\n")

    while True:

        fen = input("Enter FEN: ")

        if fen.lower() == "exit":
            break

        try:
            print("\n🔍 Analyzing...\n")

            data = analyze_fen(fen)

            print("📊 Stockfish Result:")
            print("Best Move:", data["best_move"])
            print("Evaluation:", data["score"])

            print("\n🤖 AI Explanation:\n")

            explanation = explain_position(data)

            print(explanation)
            print("\n" + "-"*50 + "\n")

        except Exception as e:
            print("Error:", e)

    close_engine()


if __name__ == "__main__":
    run_cli()