def get_input():
    text=input().split()
    return text

def is_even_length(value):
    if len(value)%2==0:
        return True

def get_even_lenght_words(values):
    return [value for value in values if is_even_length(value)]

def print_even_words(list_of_values):
    for value in list_of_values:
        print(value)


words=get_input()
even_length_words=get_even_lenght_words(words)
print_even_words(even_length_words)