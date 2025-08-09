import random
import csv
import datetime

csv_header = ["Timestamp", "Tank Lot", "Processing Start", "Quality", "Core Temperature (°F)", "Comments"]

species_names = ["sockeye", "coho", "king", "dark chum", "bright chum", "pink"]
rack_positions = ["TL", "TR", "MTL", "MTR", "ML", "MR", "MBL", "MBR", "BL", "BR", "top left", "top right", "mid bottom left", "bottom mid right"]

species_random_weights = [[2.5, 5], [2.5, 6], [12, 40], [3, 11], [3, 12], [1.5, 4]]
temp_range = [-32, 0.5]

test_fish = ["11:30", "lot", "sockeye", -20, "TL, 3"]
test_fish_no_species = ["11:30", "lot", -20, "TL, 3"]

test_fish = []

def generate_random_fish():
    timestamp = datetime.datetime(2025, 8, random.randint(1, 28))
    tank_lot = "test_lot"
    processing_start = timestamp
    quality = "Pass"
    log_species_index = random.randint(0, len(species_names) - 1)
    # log_species = species_names[log_species_index]
    log_position = random.choice(rack_positions)
    log_weight = round(random.triangular(species_random_weights[log_species_index][0], species_random_weights[log_species_index][1]), 2)
    core_temp = round(random.triangular(temp_range[0], temp_range[1]), 1)
    
    return {csv_header[0]: timestamp, csv_header[1]: tank_lot, csv_header[2]: processing_start, csv_header[3]: quality, csv_header[4]: core_temp, csv_header[5]: (log_position + ", " + str(log_weight))}

def write_to_csv(list):
    with open("test_fish.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_header)
        writer.writeheader()
        writer.writerows(test_fish)

for i in range(200):
    fish = generate_random_fish()
    test_fish.append(fish)

write_to_csv(test_fish)