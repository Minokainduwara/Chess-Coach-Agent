import os
from dotenv import load_dotenv # type: ignore
from mistralai import Mistral # type: ignore

load_dotenv()

# ✅ correct client initialization for v2.x
client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))


def explain_position(data):

    prompt = f"""
You are a chess coach.

FEN:
{data["fen"]}

Stockfish Evaluation:
- Score: {data["score"]}
- Best Move: {data["best_move"]}

Explain:
1. What is happening
2. Why best move is correct
3. Simple explanation for 1500 player
"""

    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content