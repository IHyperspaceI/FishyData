import csv
import re

csv_header = ["Timestamp", "Tank Lot", "Processing Start", "Quality", "Core Temperature (°F)", "Comments", "Weight (lbs)"]
fish_dict = []

def parse_comments(old_comment):
    if not old_comment or not old_comment.strip():
        return "", ""

    comment_lower = old_comment.lower().strip()

    # Extract weight (e.g., "5.12lbs", "5 lbs", "5lb")
    weight_match = re.search(r"(\d+(?:\.\d+)?)\s*(?:lb|lbs)\b", comment_lower)
    weight = weight_match.group(1) if weight_match else ""

    # Determine position code
    pos_code = ""
    if "mid" in comment_lower:
        pos_code += "M"
    if "top" in comment_lower:
        pos_code += "T"
    if "bottom" in comment_lower:
        pos_code += "B"
    if "left" in comment_lower:
        pos_code += "L"
    if "right" in comment_lower:
        pos_code += "R"

    return pos_code.upper(), weight

def fix_data(reader):
    for x in reader:
        comment, weight = parse_comments(x.get("Comments", ""))

        fish_dict.append({
            csv_header[0]: x.get("Timestamp", ""),
            csv_header[1]: x.get("Tank Lot", ""),
            csv_header[2]: x.get("Processing Start", ""),
            csv_header[3]: x.get("Quality", ""),
            csv_header[4]: x.get("Core Temperature (°F)", ""),
            csv_header[5]: comment,
            csv_header[6]: weight
        })

def write_to_csv(list_data, filename):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_header)
        writer.writeheader()
        writer.writerows(list_data)

with open("test_fish.csv", "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    fix_data(reader)
    write_to_csv(fish_dict, "fixed_csv.csv")