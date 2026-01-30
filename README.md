# BuildAI Pro: Intelligent Construction Planning System

BuildAI Pro is a project planning assistant that combines advanced calculation algorithms with the **IBM Granite 3.3 2B** AI model to provide instant, data-driven construction insights[cite: 8, 736].

## 🚀 Features
* **Material Estimation:** Instant calculations for Steel, Cement, Sand, and Water based on area and floors[cite: 25, 95].
* **AI Strategy:** Personalized construction tips generated locally by **IBM Granite 3.3 2B**[cite: 10, 538].
* **Privacy-First:** Powered by **Ollama**, ensuring all data stays local with no cloud API keys required[cite: 11, 737].
* **Phase-by-Phase Schedule:** A complete week-by-week timeline from site prep to final handover [cite: 39-44, 669-705].

## 🛠️ Technical Architecture
* **Backend:** Flask (Python) [cite: 53]
* **AI Model:** IBM Granite 3.3 2B (Local via Ollama) [cite: 53, 60]
* **Frontend:** Responsive HTML5/CSS3/JavaScript [cite: 55, 106]

## 📋 Installation
1. Install [Ollama](https://ollama.ai/) and pull the model: `ollama pull granite3.3:2b` [cite: 59-61].
2. Install Python dependencies: `pip install -r requirements.txt`[cite: 82].
3. Run the app: `python app.py` and visit `http://localhost:5000`[cite: 312, 443].