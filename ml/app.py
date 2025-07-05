from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

# 🛒 Big Product List
products = [
    # Staples
    {"id": 1, "name": "Basmati Rice", "price": 90, "aisle": "Staples", "availability": True, "tags": ["rice", "staple", "indian", "meal"]},
    {"id": 2, "name": "Toor Dal", "price": 75, "aisle": "Staples", "availability": True, "tags": ["dal", "pulses", "protein", "indian"]},
    {"id": 3, "name": "Wheat Flour", "price": 60, "aisle": "Staples", "availability": True, "tags": ["atta", "flour", "roti", "indian"]},

    # Breakfast
    {"id": 4, "name": "Maggi Noodles", "price": 15, "aisle": "Snacks", "availability": True, "tags": ["noodles", "breakfast", "quick", "kids"]},
    {"id": 5, "name": "Poha Pack", "price": 25, "aisle": "Staples", "availability": True, "tags": ["poha", "breakfast", "light", "healthy"]},
    {"id": 6, "name": "Upma Mix", "price": 35, "aisle": "Ready-to-Cook", "availability": True, "tags": ["breakfast", "instant", "south indian"]},

    # Spices & Condiments
    {"id": 7, "name": "Turmeric Powder", "price": 20, "aisle": "Spices", "availability": True, "tags": ["spice", "masala", "haldi"]},
    {"id": 8, "name": "Garam Masala", "price": 45, "aisle": "Spices", "availability": True, "tags": ["spice", "masala", "north indian"]},
    {"id": 9, "name": "Pickle (Mango)", "price": 60, "aisle": "Condiments", "availability": True, "tags": ["achar", "indian", "side"]},

    # Dairy
    {"id": 10, "name": "Amul Butter", "price": 55, "aisle": "Dairy", "availability": True, "tags": ["butter", "bread", "breakfast"]},
    {"id": 11, "name": "Paneer 200g", "price": 80, "aisle": "Dairy", "availability": True, "tags": ["protein", "vegetarian", "meal"]},
    {"id": 12, "name": "Curd (Dahi)", "price": 30, "aisle": "Dairy", "availability": True, "tags": ["curd", "probiotic", "cooling"]},

    # Snacks
    {"id": 13, "name": "Lay’s Chips", "price": 20, "aisle": "Snacks", "availability": True, "tags": ["snack", "party", "chips"]},
    {"id": 14, "name": "Kurkure", "price": 10, "aisle": "Snacks", "availability": True, "tags": ["snack", "crunchy", "kids"]},
    {"id": 15, "name": "Bingo Mad Angles", "price": 25, "aisle": "Snacks", "availability": True, "tags": ["snack", "spicy", "party"]},

    # Puja Items
    {"id": 16, "name": "Agarbatti", "price": 10, "aisle": "Puja", "availability": True, "tags": ["puja", "spiritual", "festive"]},
    {"id": 17, "name": "Camphor", "price": 15, "aisle": "Puja", "availability": True, "tags": ["puja", "cleanse", "temple"]},
    {"id": 18, "name": "Ghee Diya", "price": 20, "aisle": "Puja", "availability": True, "tags": ["puja", "lamp", "festive"]},

    # Personal care
    {"id": 19, "name": "Lifebuoy Soap", "price": 25, "aisle": "Personal Care", "availability": True, "tags": ["soap", "hygiene", "bath"]},
    {"id": 20, "name": "Colgate Toothpaste", "price": 50, "aisle": "Personal Care", "availability": True, "tags": ["toothpaste", "hygiene", "oral"]},

    # Festive
    {"id": 21, "name": "Rakhi Thread", "price": 15, "aisle": "Festive", "availability": True, "tags": ["raksha bandhan", "festive", "gift"]},
    {"id": 22, "name": "Diya Set", "price": 40, "aisle": "Festive", "availability": True, "tags": ["diwali", "light", "festive"]},

    # Cleaning
    {"id": 23, "name": "Phenyl", "price": 35, "aisle": "Cleaning", "availability": True, "tags": ["cleaning", "home", "floor"]},
    {"id": 24, "name": "Detergent Powder", "price": 50, "aisle": "Cleaning", "availability": True, "tags": ["washing", "clothes", "cleaning"]},

    # Drinks
    {"id": 25, "name": "Frooti", "price": 20, "aisle": "Beverages", "availability": True, "tags": ["juice", "drink", "kids"]},
    {"id": 26, "name": "Bisleri Water Bottle", "price": 20, "aisle": "Beverages", "availability": True, "tags": ["water", "hydration", "drink"]},
    {"id": 27, "name": "Chai Patti (Brooke Bond)", "price": 70, "aisle": "Beverages", "availability": True, "tags": ["tea", "chai", "indian", "morning"]},

    # Utility
    {"id": 28, "name": "Plastic Bags", "price": 10, "aisle": "Utilities", "availability": True, "tags": ["bag", "carry", "utility"]},
    {"id": 29, "name": "Aluminium Foil", "price": 30, "aisle": "Utilities", "availability": True, "tags": ["packing", "kitchen", "utility"]}
]

# 🔑 Occasion keyword → item names
occasion_keywords = {
    "trip": ["maggi", "chips", "bisleri", "frooti", "tissues"],
    "birthday": ["cake", "soda", "chips", "plastic bags", "napkins"],
    "monthly groceries": ["rice", "dal", "atta", "turmeric", "soap", "toothpaste"],
    "puja": ["agarbatti", "camphor", "ghee diya"],
    "college": ["maggi", "kurkure", "bisleri", "poha", "detergent"]
}

@app.route('/generate', methods=['POST'])
def generate_cart():
    data = request.json
    query = data.get('input', '').lower()

    # 🎯 Extract budget
    prices = re.findall(r'\d+', query)
    budget = int(prices[0]) if prices else 9999

    # 🔍 Check for occasion-specific keywords
    for occasion, keywords in occasion_keywords.items():
        if occasion in query:
            matched = []
            total = 0
            for kw in keywords:
                for p in products:
                    if kw in p["name"].lower() and p["availability"]:
                        if total + p["price"] <= budget:
                            matched.append(p)
                            total += p["price"]
                            break
            return jsonify({"products": matched})

    # 📦 Default: Match by tags
    tag_matched = [p for p in products if any(tag in query for tag in p["tags"]) and p["availability"]]

    # 💸 Filter those that stay under budget
    selected = []
    total = 0
    for item in sorted(tag_matched, key=lambda x: x["price"]):
        if total + item["price"] <= budget:
            selected.append(item)
            total += item["price"]

    return jsonify({"products": selected})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
