input = input()
opening_bracket = []

for i in range(len(input)):
    if input[i] == "(":
        opening_bracket.append(i)
    elif input[i] == ")":
        start_index = opening_bracket.pop()
        print(input[start_index:i + 1])
