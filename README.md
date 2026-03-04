# 🤖 RUD AI — Multi-Mode AI Assistant

> A conversational AI assistant with 6 specialized modes, built with Flask + Ollama (llama3.1). Runs entirely **offline** — no API key, no cost.

---

## 📸 Screenshots

### 🖥️ Desktop
| Welcome Screen | Chat Interface |
|---|---|
| <img src="https://github.com/user-attachments/assets/c460dc92-e213-4b39-ad30-342064b8a5ee" width="420"/> | <img src="https://github.com/user-attachments/assets/b860fd7e-f346-4053-9014-b23d52fb975f" width="420"/> |

### 📱 Mobile
| Home | Chat | Sidebar |
|---|---|---|
| <img src="https://github.com/user-attachments/assets/77f07637-c622-46ff-b545-d67af43711a6" width="200"/> | <img src="https://github.com/user-attachments/assets/3586ef5b-4c02-4fe1-916f-7d6d50b3691b" width="200"/> | <img src="https://github.com/user-attachments/assets/3267c096-cee5-4f01-b8e8-6614d1f8523f" width="200"/> |

---

## ✨ Features

- 🧠 **6 Intelligent Modes** — Normal, Banking, Cooking, Study, Entertainment, Fun
- 💬 **Full Conversation Memory** — remembers the entire chat session
- 🏦 **Banking Knowledge Base** — 40 pre-loaded financial Q&A pairs
- 🍳 **Cooking Mode** — step-by-step recipe formatting
- 📚 **Study Mode** — structured educational responses
- 📱 **Responsive UI** — works on mobile and desktop
- 💸 **100% Free** — powered by local Ollama, no cloud API needed

---

## 🖥️ Demo

![RUD AI](https://img.shields.io/badge/Status-Active-brightgreen) ![Python](https://img.shields.io/badge/Python-3.8+-blue) ![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey) ![Ollama](https://img.shields.io/badge/Ollama-llama3.1-orange)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai) installed and running
- llama3.1 model pulled

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/Rudra-Gupta15/Conversational_AI.git
cd Conversational_AI
```

**2. Install Python dependencies**
```bash
pip install -r requirements.txt
```

**3. Install and start Ollama**
```bash
# Download from https://ollama.ai then pull the model
ollama pull llama3.1
```

**4. Run the app**
```bash
python app_ollama.py
```

**5. Open in browser**
```
http://localhost:5000
```

---

## 🎯 Modes

| Mode | Description |
|------|-------------|
| 🌐 **Normal** | General purpose assistant — ask anything |
| 🏦 **Banking** | Finance, investments, budgeting, banking advice |
| 🍳 **Cooking** | Recipes with step-by-step formatting |
| 📚 **Study** | Structured learning with definitions, examples & tips |
| 🎬 **Entertainment** | Movies, music, games, shows & pop culture |
| 😄 **Fun** | Jokes, riddles, word games & challenges |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, Vanilla JavaScript |
| Backend | Python, Flask |
| AI Model | Ollama (llama3.1) |
| Data | CSV Knowledge Base + Pickle vectors |

---

## 📁 Project Structure

```
Conversational_AI/
├── templates/
│   └── Index.html              # Frontend UI
├── app_ollama.py               # Flask backend + AI logic
├── banking_knowledge_base.csv  # Banking Q&A dataset
├── Q&A.txt                     # Raw Q&A source
├── answers.pkl                 # Preprocessed answers
├── question_vectors.pkl        # Question embeddings
├── sections.pkl                # Category sections
├── vectorizer.pkl              # TF-IDF vectorizer
├── requirements.txt            # Python dependencies
└── .gitignore
```

---

## 👨‍💻 Author

**Rudra Gupta** — AI/ML Engineer & Game Developer

- 🌐 Portfolio: [rudra-gupta.vercel.app](https://rudra-gupta.vercel.app/)
- 💼 GitHub: [@Rudra-Gupta15](https://github.com/Rudra-Gupta15)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
