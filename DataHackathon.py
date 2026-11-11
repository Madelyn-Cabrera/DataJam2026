import csv

with open("/Users/hanabarati/Documents/GitHub/DataJam2026/Vancouver.csv", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)

    PRICE_COL = 46
    price=[]
    for values in reader:
        if len(values) <= PRICE_COL:      # skip short/blank rows
            continue
        raw = values[PRICE_COL].replace("$", "").replace(",", "").strip()
        if raw == "":                     # skip missing prices
            continue
        price.append(float(raw))
print(sum(price))