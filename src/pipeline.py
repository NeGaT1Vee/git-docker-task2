import csv

INPUT_PATH = "data/sales.csv"
OUTPUT_PATH = "data/processed_sales.csv"

total_revenue = 0
processed_rows = []

with open(INPUT_PATH, newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        quantity = int(row["quantity"])
        price = float(row["price"])
        total = quantity * price

        total_revenue += total
        processed_rows.append({
            "product": row["product"],
            "quantity": quantity,
            "price": price,
            "total": total
        })

print(f"Total Revenue: {total_revenue:.0f}")

with open(OUTPUT_PATH, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["product", "quantity", "price", "total"])
    writer.writeheader()
    writer.writerows(processed_rows)