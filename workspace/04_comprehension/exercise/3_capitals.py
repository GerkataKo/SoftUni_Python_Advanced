def get_input():
    text=input().split(", ")
    return text

def get_length_of_words(value):
    return len(value)

def print_result(values):
    {print(f"{key} -> {value}") for key, value in values.items()}

countries=get_input()
capitals=get_input()
pairs=dict(zip(countries,capitals))
print_result(pairs)