import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("mean of popultion:- ", mean)
print("Standard deviation of popultion:- ", std_deviation)


def random_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


mean_list = []
for i in range(0, 1000):
    set_of_means = random_mean(100)
    mean_list.append(set_of_means)


std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("mean of sampling distribution:- ", mean)
print("Standard deviation of sampling distribution:- ", std_deviation)


first_std_deviation_start, first_std_deviation_end = mean - \
    std_deviation, mean+std_deviation

second_std_deviation_start, second_std_deviation_end = mean - \
    (2*std_deviation), mean+(2*std_deviation)

third_std_deviation_start, third_std_deviation_end = mean - \
    (3*std_deviation), mean+(3*std_deviation)

print("std1", first_std_deviation_start, first_std_deviation_end)
print("std2", second_std_deviation_start, second_std_deviation_end)
print("std3", third_std_deviation_start, third_std_deviation_end)

df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()

mean_of_sample3 = statistics.mean(data)

print("mean of sample3:- ", mean_of_sample3)
