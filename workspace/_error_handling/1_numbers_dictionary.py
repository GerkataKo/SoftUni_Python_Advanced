numbers_dictionary = {}
line = input()
while line != "Search":
    number_as_string=line
    try:
        number = int(input())
    except ValueError:
        print("The variable number must be an integer")
    else:
        numbers_dictionary[number_as_string] = number
    finally:
        line = input()

line = input()
while line != "Remove":
    try:
        print(numbers_dictionary[line])
    except KeyError:
        print("Number does not exist in dictionary")
    finally:
        line = input()

line = input()
while line != "End":
    try:
        del numbers_dictionary[line]
    except KeyError:
        print("Number does not exist in dictionary")
    finally:
        line = input()

print(numbers_dictionary)
