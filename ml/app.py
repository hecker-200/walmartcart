from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import clean_and_load_products
import re

# 🧹 Load and clean products
products = clean_and_load_products("products.csv", "cleaned_products.json")

app = Flask(__name__)
CORS(app)

# 🔑 Occasion → keywords mapping
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

    # 🎉 Match occasion keywords
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

    # 🔍 Default: tag matching
    tag_matched = [
        p for p in products
        if any(tag in query for tag in p["tags"]) and p["availability"]
    ]

    # 💸 Filter under budget
    selected = []
    total = 0
    for item in sorted(tag_matched, key=lambda x: x["price"]):
        if total + item["price"] <= budget:
            selected.append(item)
            total += item["price"]

    return jsonify({"products": selected})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
