import requests # type: ignore


class ChessCoach:

    def __init__(self, model="llama3.2:latest"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def explain(self, data):

        prompt = f"""
You are a professional chess coach.

Analyze this position:

FEN:
{data["fen"]}

Engine Output:
- Best Move: {data["best_move_san"]}
- Evaluation: {data["evaluation"]}
- Position Type: {data["classification"]}
- Top Moves: {data["top_moves"]}

Explain clearly:
1. What is happening
2. Why best move is correct
3. What mistake level means
4. Simple improvement advice
"""

        try:
            res = requests.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=60
            )

            return res.json().get("response", "⚠ No AI response")

        except Exception as e:
            return f"❌ AI Error: {str(e)}"