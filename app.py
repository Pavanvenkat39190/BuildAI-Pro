from flask import Flask, render_template, request, jsonify
import math
import ollama

app = Flask(__name__)

# Realistic Residential Construction Standards
CONSTRUCTION_RATES = {
    "STEEL_PER_SQ_YARD": 4.0,   
    "CEMENT_PER_SQ_YARD": 0.5,  
    "SAND_PER_SQ_YARD": 0.06,   
    "WATER_PER_SQ_YARD": 150,   
    "LABOR_FACTOR": 0.504       
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/calculate", methods=["POST"])
def calculate():
    data = request.json
    area = float(data.get("area", 1000))
    floors_str = data.get("floors", "G+2")
    daily_wage = float(data.get("wage", 500))
    unit_cost = float(data.get("unit_cost", 1500))
    
    try:
        num_floors = int(floors_str.lower().split('+')[-1]) + 1
    except:
        num_floors = 1

    # 1. Resource Logic
    steel = (CONSTRUCTION_RATES["STEEL_PER_SQ_YARD"] * area * num_floors) / 1000
    cement = CONSTRUCTION_RATES["CEMENT_PER_SQ_YARD"] * area * num_floors
    sand = CONSTRUCTION_RATES["SAND_PER_SQ_YARD"] * area * num_floors
    water = CONSTRUCTION_RATES["WATER_PER_SQ_YARD"] * area * num_floors
    
    # 2. Financial Logic
    material_cost = area * unit_cost * num_floors
    total_labor_days = int(area * CONSTRUCTION_RATES["LABOR_FACTOR"])
    labor_cost = total_labor_days * daily_wage
    overhead = (material_cost + labor_cost) * 0.10
    total_estimate = material_cost + labor_cost + overhead

    # 3. AI Strategic Tip
    try:
        response = ollama.chat(
            model='granite3.3:2b', 
            messages=[{
                'role': 'user', 
                'content': f"Provide two short paragraphs of construction advice for a {floors_str} building with a budget of ₹{total_estimate:,.0f}."
            }],
            options={'num_predict': 512} 
        )
        ai_tip = response['message']['content']
    except:
        ai_tip = "AI Strategic Insight Module Offline."

    return jsonify({
        "steel": f"{round(steel, 2)} tons",
        "cement": f"{math.ceil(cement)} bags",
        "sand": f"{round(sand, 2)} tons",
        "water": f"{water:,.0f} L",
        "labor_cost": f"₹{labor_cost:,.0f}",
        "material_cost": f"₹{material_cost:,.0f}",
        "overhead": f"₹{overhead:,.0f}",
        "total_estimate": f"₹{total_estimate:,.0f}",
        "days": total_labor_days,
        "ai_insight": ai_tip
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)