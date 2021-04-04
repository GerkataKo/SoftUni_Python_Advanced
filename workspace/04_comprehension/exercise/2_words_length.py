def get_input():
    text=input().split(", ")
    return text

def get_length_of_words(value):
    return len(value)

def print_result(values):
     print(", ".join((f"{value} -> {get_length_of_words(value)}" for value in values)))

words=get_input()
print_result(words)