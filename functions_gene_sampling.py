from functions_generic import *

def create_fib_string(length):
    f1 = "B"
    f2 = "A"
    f3 = f2+f1
    for i in range(length-2):
        f3 = f2 + f1
        f1 = f2
        f2 = f3
    return f3

def create_random_string(length):
    import random
    output = ""
    heads = "B"
    tails = "A"

    for i in range(length):
        result = random.randint(0, 1)
        if result == 0:
            output = output + heads
        else:
            output = output + tails
    return output

def create_4_random_string(length):
    import random
    output = ""

    for i in range(length):
        result = random.randint(0, 3)
        if result == 0:
            output = output + "A"
        elif result == 1:
            output = output + "B"
        elif result == 2:
            output = output + "C"
        else:
            output = output + "D"

    return output

def count_bwt_runs(string,d,m):
    n = len(string)
    concat_string = ""
    for i in range(0,n+1-m,d):
        substring = string[i:i+m]
        concat_string += substring
    concat_bwt = bwt(concat_string).replace("$", "")
    previous_letter = "NA"
    count = 0
    for letter in concat_bwt:
        if letter is not previous_letter:
            count += 1
        previous_letter = letter
    return count

def concat_string(string,d,m):
    n = len(string)
    concat_string = ""
    for i in range(0, n + 1 - m, d):
        substring = string[i:i + m]
        concat_string += substring
    return concat_string

def count_runs(string):
    previous_letter = "NA"
    count = 0
    for letter in string:
        if letter is not previous_letter:
            count += 1
        previous_letter = letter
    return count