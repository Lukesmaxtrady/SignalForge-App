import csv

def export_csv(data, filename="export.csv"):
    if not data:
        return
    keys = data[0].keys()
    with open(filename, "w", newline='') as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(data)
    return filename