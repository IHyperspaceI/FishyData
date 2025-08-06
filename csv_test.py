import random
import csv

csv_header = ["time", "lot", "species", "temp", "comments"]

species_names = ["sockeye", "coho", "king", "dark chum", "bright chum", "pink"]
rack_positions = ["TL", "TR", "MTL", "MTR", "ML", "MR", "MBL", "MBR", "BL", "BR"]

species_random_weights = [[2.5, 5], [2.5, 6], [12, 40], [3, 11], [3, 12], [1.5, 4]]
temp_range = [-32, 0.5]

test_fish = ["11:30", "lot", "sockeye", -20, "TL, 3"]
test_fish_no_species = ["11:30", "lot", -20, "TL, 3"]

test_fish = []

def generate_random_fish():
    log_time = random.randrange(0, 1440)
    log_lot = "test_lot"
    log_species_index = random.randint(0, len(species_names) - 1)
    log_species = species_names[log_species_index]
    log_position = random.choice(rack_positions)
    log_weight = random.triangular(species_random_weights[log_species_index][0], species_random_weights[log_species_index][1])
    log_temp = random.triangular(temp_range[0], temp_range[1])

    [log_time, log_lot, log_species, log_temp, log_position + ", " + str(log_weight)]
    
    return {csv_header[0]: log_time, csv_header[1]: log_lot, csv_header[2]: log_species, csv_header[3]: log_temp, csv_header[4]: (log_position + ", " + str(log_weight))}

for i in range(20):
    fish = generate_random_fish()
    test_fish.append(fish)


with open("test_fish.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_header)
    writer.writeheader()
    writer.writerows(test_fish)