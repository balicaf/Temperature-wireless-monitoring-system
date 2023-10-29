import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Initialize lists to store data
timestamps = []
temperature1 = []
temperature2 = []

# Path to your CSV file
csv_file = "/Users/racinecubix/Documents/temperature2.csv"

# Read data from the CSV file
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row if it exists

    for row in csv_reader:
        try:
            timestamp = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')
            temperature1_value = float(row[1])
            temperature2_value = float(row[2])

            # Append the valid data
            timestamps.append(timestamp)
            temperature1.append(temperature1_value)
            temperature2.append(temperature2_value)
        except (ValueError, IndexError):
            # Handle exceptions - for example, print an error message
            print(f"Skipping row: {row}")

# Create a line plot if there is valid data
if timestamps and temperature1 and temperature2:
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, temperature1, label='Temperature 1')
    plt.plot(timestamps, temperature2, label='Temperature 2')
    plt.xlabel('Timestamp')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Data')
    plt.ylim(12, 20)  # Set the y-axis limits to constrain between 12 and 20 degrees Celsius
    plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M:%S'))
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("No valid data to plot.")