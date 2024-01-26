""" @package shared
Documentation for result module.

More details.
Class for storing the result of a thread.
"""
import csv

from matplotlib import pyplot as plt


class Result:
    def __init__(self, name, message, data):
        """
        The constructor for Result class.
        :param name: name of the result
        :param message: message to print on the graph
        :param data: data of the result
        """

        self.name = name
        self.message = message
        self.data = data


def plot_data(data_list: [Result]):
    """
    Plot the data in the data_list.
    :param data_list: list of data to plot
    :return:
    """

    for i, data in enumerate(data_list):
        plt.figure()
        plt.plot(data.data[0], data.data[1])
        plt.xlabel("Temps (s)")
        plt.ylabel(data.message)
        plt.title(data.name)
    plt.show()


def smooth_data(data_list: [Result], nb_points: int):
    """
    Smooth the data in the data_list.
    :param data_list: list of data to smooth
    :param nb_points: number of points to use for smoothing
    :return: list of smoothed data
    """

    result = []
    for data in data_list:
        list_data = []
        list_time_data = []
        for i in range(0, len(data.data[0])):
            start_index = max(0, i - int(nb_points / 2) + 1)
            end_index = min(len(data.data[0]), i + int(nb_points / 2) + 1)
            window_time_data = data.data[0][start_index:end_index]
            window_data = data.data[1][start_index:end_index]
            list_data.append(sum(window_data) / len(window_data))
            list_time_data.append(sum(window_time_data) / len(window_time_data))
        result.append(Result(data.name, data.message, [list_time_data, list_data]))
    return result


def save_data(file_name, data: [Result]):
    """
    Save the data in a csv file.
    :param file_name: name of the file
    :param data: data to save
    :return: status of the function
    """

    for result in data:
        full_csv_file_name = file_name + "_" + result.name + ".csv"
        with open(full_csv_file_name, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Écriture de l'en-tête
            csv_writer.writerow(["Temp", result.message])
            for temp, data in zip(result.data[0], result.data[1]):
                csv_writer.writerow([temp, data])

        print(f"Les données de {result.name} ont été écrites dans {full_csv_file_name}.")


def read_data(path: str, result: Result):
    """
    Read the data in a csv file.
    :param path: path of the file
    :param result:
    :return: result with the data
    """
    time_data = []
    data_data = []
    with open(path, mode='r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        premiere_ligne = next(csv_reader, None)
        if premiere_ligne is not None:
            result.message = str(premiere_ligne[1])
        for row in csv_reader:
            time_data.append(float(row[0]))
            data_data.append(float(row[1]))
    result.data = [time_data, data_data]
    return result
