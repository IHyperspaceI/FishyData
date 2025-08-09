import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("fixed_csv.csv")

plt.scatter(data["Weight (lbs)"], data["Core Temperature (°F)"])

plt.xlabel("Weight")
plt.ylabel("Temperature")
plt.title("Weight/Temp")

plt.show()