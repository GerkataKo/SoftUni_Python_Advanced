input = input()
is_balanced = True
opening_bracket = []

bracket_types = {
                "(": ")",
                "[": "]",
                "{": "}",
                }

for char in input:
    if char in "({[":
        opening_bracket.append(char)
    else:
        if not opening_bracket:
            is_balanced=False
            break
        bracket_opening=opening_bracket.pop()
        if not bracket_types[bracket_opening]==char:
            is_balanced=False
            break

if is_balanced:
    print("YES")
else:
    print("NO")
