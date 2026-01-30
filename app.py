from flask import Flask, render_template, request, jsonify
import math
import ollama  # Connects to your local AI [cite: 53]

app = Flask(__name__)

# Constants based on your project thumb rules [cite: 221-245]
CONSTRUCTION_RATES = {
    "STEEL_PER_SQ_YARD": 3.5,  # kg per sq yard [cite: 239]
    "CEMENT_PER_SQ_YARD": 0.4, # bags per sq yard [cite: 240]
    "SAND_PER_SQ_YARD": 0.6,   # tons per sq yard [cite: 242]
    "WATER_PER_SQ_YARD": 500,  # liters per sq yard [cite: 251]
    "STEEL_RATE": 60000,       # INR per ton [cite: 233]
    "CEMENT_RATE": 420         # INR per bag [cite: 234]
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/calculate", methods=["POST"])
def calculate():
    data = request.json
    area = float(data.get("built_up_area", 0))
    floors = data.get("floors", "G+0")
    
    # Material Math [cite: 95, 239-245]
    steel = (area * CONSTRUCTION_RATES["STEEL_PER_SQ_YARD"]) / 1000
    cement = area * CONSTRUCTION_RATES["CEMENT_PER_SQ_YARD"]
    
    # Optimized AI Prompt for maximum speed 
    try:
        response = ollama.chat(
            model='granite3.3:2b', 
            messages=[{
                'role': 'user', 
                'content': f"As a construction expert, give a 2-sentence planning tip for a {floors} building of {area} sq yards."
            }],
            options={'num_predict': 150} # Limit output tokens for speed 
        )
        ai_tip = response['message']['content']
    except Exception as e:
        ai_tip = "AI is currently offline. Ensure Ollama is running 'granite3.3:2b'!"

    return jsonify({
        "steel": f"{round(steel, 2)} tons",
        "cement": f"{math.ceil(cement)} bags",
        "ai_insight": ai_tip
    })

if __name__ == "__main__":
    # Running on local port 5000 [cite: 312, 443]
    app.run(debug=True, port=5000)