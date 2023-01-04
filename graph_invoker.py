import requests

import matplotlib.pyplot as plt

base = "http://127.0.0.1:5000/"


def plot_line_chart():
    response = requests.get(base + "get_line_chart_data")
    if response.status_code == 200:
        raw_data = response.json()

        plt.plot(raw_data[0], raw_data[1])
        plt.title("Total billing over years (in USD)")
        plt.show()
    else:
        print(
            f"Hello person, there's a {response.status_code} error with your request")


def plot_bar_chart():
    response = requests.get(base + "get_bar_chart_data")
    if response.status_code == 200:
        raw_data = response.json()

        plt.bar(raw_data[0], raw_data[1])
        plt.title("Total albums (top 10)")
        plt.show()
    else:
        print(
            f"Hello person, there's a {response.status_code} error with your request")


def plot_scatter_chart():
    response = requests.get(base + "get_scatter_chart_data")
    if response.status_code == 200:
        raw_data = response.json()

        plt.scatter(raw_data[0], raw_data[1])
        plt.title("Min to MB ratio")
        plt.xlabel("Min")
        plt.ylabel("MB")
        plt.show()
    else:
        print(
            f"Hello person, there's a {response.status_code} error with your request")


def plot_pie_chart():
    response = requests.get(base + "get_pie_chart_data")
    if response.status_code == 200:
        raw_data = response.json()

        plt.pie(raw_data[1], labels=raw_data[0])
        plt.title("MediaType minutes distribution")
        plt.show()
    else:
        print(
            f"Hello person, there's a {response.status_code} error with your request")


while True:
    print("Please choose an option")
    print("1. Line Chart")
    print("2. Bar Chart")
    print("3. Scatter Chart")
    print("4. Pie Chart")
    print("0. Exit")

    i = input()
    valid = True

    if not i.isdigit():
        valid = False

    if valid:
        i = int(i)

        if not 0 <= i <= 4:
            valid = False

    if not valid:
        print("Please choose from the given options only")
        continue
    else:
        if i == 1:
            plot_line_chart()
        elif i == 2:
            plot_bar_chart()
        elif i == 3:
            plot_scatter_chart()
        elif i == 4:
            plot_pie_chart()
        else:
            break

