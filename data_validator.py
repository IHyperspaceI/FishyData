import csv

csv_header = ["Timestamp", "Tank Lot", "Processing Start", "Quality", "Core Temperature (°F)", "Comments"]
fish_dict = []

def fix_comments(old_comment):
    position = old_comment.split(",")[0]
    weight = old_comment.split(",")[1]

    if len(position) > 3:
        new_pos = ""
        print("Old: " + position)
        if "mid" in position or "Mid" in position:
            new_pos += "M"
        if "top" in position or "Top" in position:
            new_pos += "T"
        if "bottom" in position or "Bottom" in position:
            new_pos += "B"
        if "left" in position or "Left" in position:
            new_pos += "L"
        if "right" in position or "Right" in position:
            new_pos += "R"

        position = new_pos
            
    return position + ", " + weight


def fix_data(reader):
    for x in reader:
        # print(x["Comments"])
        timestamp = x["Timestamp"]
        tank_lot = x["Tank Lot"]
        processing_start = x["Processing Start"]
        quality = x["Quality"]
        core_temp = x["Core Temperature (°F)"]
        comment = fix_comments(x["Comments"])

        fish_dict.append({csv_header[0]:timestamp, csv_header[1]:tank_lot, csv_header[2]:processing_start, csv_header[3]:quality, csv_header[4]:core_temp, csv_header[5]:comment, })


def write_to_csv(list, filename):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_header)
        writer.writeheader()
        writer.writerows(list)


with open("test_fish.csv", "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    fix_data(reader)
    write_to_csv(fish_dict, "fixed_csv.csv")