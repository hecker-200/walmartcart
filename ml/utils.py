import csv
import json
import re

def generate_tags(row):
    tags = []
    for col in ["category", "sub_category", "type", "brand"]:
        if row.get(col):
            tags.extend(row[col].lower().split())

    if row.get("description"):
        desc_words = re.findall(r'\b\w+\b', row["description"].lower())
        tags.extend(desc_words)

    return list(set(tags))  # Remove duplicates

def clean_and_load_products(csv_path, json_path="cleaned_products.json"):
    cleaned_data = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader, start=1):
            try:
                name = row["product"].strip()
                price = float(row["sale_price"])
                if not name or price <= 0:
                    print(f"❌ Skipping row {i}: Invalid name or price => {name} / {price}")
                    continue

                product = {
                    "id": i,
                    "name": name,
                    "price": round(price),
                    "aisle": row["category"].strip() or "Misc",
                    "availability": True,
                    "tags": generate_tags(row)
                }

                cleaned_data.append(product)
                print(f"✅ Added: {name} ₹{price}")
            except Exception as e:
                print(f"⚠️ Error in row {i}: {e}")
                continue

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=2)

    print(f"\n🧼 Total cleaned products: {len(cleaned_data)}")
    return cleaned_data
