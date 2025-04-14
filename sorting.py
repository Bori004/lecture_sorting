import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data



def selection_sort(number_array, direction='ascending'):
    """
    :param list number_array: list with numeric array
    :param string direction: string indicating sorting direction: ascending / descending
    :return: sorted numeric array
    """

    n = len(number_array)
    for i in range(n):
        min_max_idx = i
        for num_idx in range(i+1,n):
             if direction == "ascending":
                 if number_array[num_idx] < number_array [min_max_idx]:
                    min_max_idx = num_idx

             elif direction == "descending":
                 if number_array[num_idx] > number_array[min_max_idx]:
                     min_max_idx = num_idx

        number_array[i], number_array[min_max_idx] = number_array[min_max_idx], number_array[i]

    return number_array


def bubble_sort(number_array):
    """
    :param str number_array: list with numeric array
    :return: sorted numeric array
    """
    n = len(number_array)
    switched = True
    print(number_array)
    while switched:
        switched = False
        for i in range(n-1):
            number = number_array[i]
            if number_array[i] > number_array[i+1]:
                number_array[i] = number_array[i+1]
                number_array[i+1] = number
                switched = True
            print(number_array)
        print(10*"*")
        i +=1


    return number_array



# def insertion_sort(number_array):
#     n = len(number_array)
#     for i in range(n-1):
#         print(5*"*")
#         print(number_array[i])
#         print(5*"*")
#         for number in number_array[(i+1):(n-1)]:
#             print(number)
#             if number < number_array[i]:
#                 print(True)
#                 for j in number_array[:i+1]:
#                     print(5*"/")
#                     print(j)
#                     if number_array[j]> number:
#                         number_array.insert(number, j)

def insertion_sort(number_array):
    n = len(number_array)
    for i in range(1,n):
        key = number_array[i]
        j = i-1
        while j>= 0 and number_array[j] > key:
            number_array[j+1] = number_array[j]
            j = j-1
        number_array[j+1] = key
    return number_array



def main():
    data = read_data("numbers.csv")
    print(data)
    # sorted_data = selection_sort(data["series_1"])
    # print(sorted_data)
    # bubbled_data = bubble_sort(data["series_1"])
    # print(bubbled_data)
    inserted_data = insertion_sort(data["series_1"])
    print(inserted_data)




if __name__ == '__main__':
    main()
