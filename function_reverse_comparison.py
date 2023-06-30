from functions_generic import *
import csv

def make_reverse_mean_data_csv(n):
    data = []
    for i in range(1,n+1):
        print("starting loop",i)
        language = all_binary_strings(i)
        for string in language:
            data.append([i,string,calc_dif(string)])

    print("saving")
    with open("reverse_mean_data.csv", "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(data)


def calc_dif(string):
    return count_runs(bbwt(string))-count_runs(bbwt(reverse_string(string)))

def count_runs(string):
    previous_letter = "NA"
    count = 0
    for letter in string:
        if letter is not previous_letter:
            count += 1
        previous_letter = letter
    return count

def all_binary_strings(length):
    strings = ['']
    for x in range(length):
        new_strings = []
        for string in strings:
            new_strings.append(string + 'a')
            new_strings.append(string + 'b')
        strings = new_strings
    return strings

def reverse_string(string):
    reversed = ""
    for letter in string:
        reversed = letter + reversed
    return reversed
