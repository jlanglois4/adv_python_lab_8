import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sitings_per_year = {}
dates_list = []
sitings_list = []

with open("./ufo-sightings.csv", 'rt') as file:
    csv_reader = csv.reader(file)
    data_list = list(csv_reader)
    data_list = data_list[1:]
    for line in data_list:
        year = line[0][6:10]
        if year in sitings_per_year:
            sitings_per_year[year] += int(line[1])
        else:
            sitings_per_year[year] = int(line[1])

    print("UFO Sightings per Year")
    print("YEAR    Sightings")

    total = 0

    for key in sitings_per_year:
        dates_list.append(key)
        sitings_list.append(sitings_per_year[key])
        print(f"{key}    {sitings_per_year[key]}")
        total += sitings_per_year[key]

    dates_array = np.array(dates_list)
    sitings_array = np.array(sitings_list)

    print(f"Total: {total}")
    print(f"Average: {round(np.mean(sitings_list), 2)}")
    print(f"Median: {int(np.median(sitings_list))}")
    print(f"Standard Deviation: {round(np.std(sitings_list), 2)}")

    sns.distplot(sitings_list)
    plt.show()

    plt.hist(sitings_list, 10)
    plt.show()

    plt.scatter(sitings_list, sitings_list)
    plt.show()