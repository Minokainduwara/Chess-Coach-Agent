# ♟️ Chess AI Coach

> A fully local chess analysis tool powered by **Stockfish** + **Ollama (LLM)** — get engine-level move analysis with human-readable AI explanations, right from your terminal.

---

## ✨ Features

- 🔍 **Deep position analysis** via Stockfish (configurable depth)
- 🤖 **AI-powered explanations** using a local LLM (Ollama / llama3.2)
- 📋 **SAN notation output** — human-readable moves like `Rg8`, `Qxf7+`, `Nf3`
- 📊 **Multi-PV analysis** — top 3 candidate moves per position
- ⚠️ **Move classification** — blunder / mistake / equal / winning
- ✅ **Legal move validation** — no invalid engine output ever shown
- 💻 **Simple CLI interface** — paste a FEN and get instant feedback
- 🔒 **100% offline** — no paid APIs, no internet required after setup

---

## 🧠 How It Works

```
FEN Input
    ↓
Stockfish Engine  →  Evaluation + Best Moves (SAN + UCI)
    ↓
Ollama LLM  →  Human-readable coaching explanation
    ↓
CLI Output
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.11+ | Core language |
| [python-chess](https://python-chess.readthedocs.io/) | Board logic, move validation, SAN conversion |
| [Stockfish](https://stockfishchess.org/) | Chess engine (analysis backend) |
| [Ollama](https://ollama.com/) | Local LLM runner |
| llama3.2 / mistral | AI explanation model |
| Requests | HTTP communication with Ollama |

---

## 📁 Project Structure

```
chess-ai-coach/
├── main.py        # CLI entry point
├── engine.py      # Stockfish integration (Multi-PV, SAN, classification)
├── coach.py       # Ollama AI explanation layer
└── config.py      # Engine settings (depth, threads, hash)
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/chess-ai-coach.git
cd chess-ai-coach
```

### 2. Install Python dependencies

```bash
pip install python-chess requests
```

### 3. Install Stockfish

**macOS**
```bash
brew install stockfish
```

**Linux (Ubuntu/Debian)**
```bash
sudo apt install stockfish
```

**Windows**
Download the binary from [stockfishchess.org/download](https://stockfishchess.org/download/) and update `STOCKFISH_PATH` in `config.py`.

### 4. Install Ollama and pull a model

```bash
# Install Ollama
brew install ollama        # macOS
# or visit https://ollama.com for Linux/Windows

# Start the Ollama service
ollama serve

# Pull a model (in a new terminal)
ollama pull llama3.2:latest
```

---

## ▶️ Usage

```bash
python main.py
```

Paste any valid FEN string when prompted:

```
♟ Chess Engine V2 (AI Coach + Stockfish)
Type 'exit' to quit

Enter FEN: 5r1k/1p1R3R/1q4p1/8/5r2/8/PP4QK/8 b - - 0 40
```

---

## 💡 Example Output

```
📊 Stockfish Result:
Best Move:   Rg8
Evaluation:  Mate in -1
Type:        blunder
Top Moves:   ['Rg8', 'Qxg7+', 'Kh8']

🤖 AI Coach:
This position is completely lost for Black. The engine recommends Rg8
to delay the inevitable mate, but White has a forced checkmate with Rxh7#.
Black's queen on b6 is too far away to help with the defence...
```

---

## ⚙️ Configuration

Edit `config.py` to tune the engine to your hardware:

```python
STOCKFISH_PATH = "stockfish"   # or full path on Windows

ENGINE_CONFIG = {
    "Threads": 4,       # CPU threads to use
    "Hash": 512,        # Hash table size in MB
    "Skill Level": 20   # 0–20 (20 = maximum strength)
}

DEPTH = 18      # Search depth (higher = stronger, slower)
MULTI_PV = 3    # Number of top moves to analyse
```

---

## 📊 Move Classification Reference

| Evaluation (centipawns) | Classification |
|---|---|
| +200 or above | ✅ Winning |
| +50 to +200 | 🟡 Slightly better |
| -50 to +50 | ⚖️ Equal |
| -50 to -200 | 🟠 Mistake |
| -200 or below | 🔴 Blunder |

---

## 🗺️ Roadmap

- [ ] PGN full-game analysis (move-by-move review)
- [ ] Accuracy score (0–100, Chess.com style)
- [ ] Opening classification (ECO codes)
- [ ] Endgame detection
- [ ] Web dashboard (React + FastAPI)
- [ ] "You missed mate in N" detection

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📜 License

[MIT](LICENSE) — free to use, modify, and distribute.

---

## ⭐ Support

If you find this project useful, give it a star! It helps others discover it.

Built with ♟️ by a developer passionate about chess, AI, and building real things.