import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("School2.csv")
data = df["Math_score"].tolist()


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


df = pd.read_csv("School_1_Sample.csv")

data = df["Math_score"].tolist()
mean_of_sample1 = statistics.mean(data)


print("Mean of sample1:- ", mean_of_sample1)


df = pd.read_csv("School_2_Sample.csv")

data = df["Math_score"].tolist()
mean_of_sample2 = statistics.mean(data)


df = pd.read_csv("School_3_Sample.csv")

data = df["Math_score"].tolist()

mean_of_sample3 = statistics.mean(data)


z_score = (mean - mean_of_sample2)/std_deviation
print("The z score is = ", z_score)
