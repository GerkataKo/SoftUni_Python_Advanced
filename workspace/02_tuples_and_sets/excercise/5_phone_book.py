def print_result(name, dict):
    if name in dict:
        print(f"{name} -> {dict[name]}")
    else:
        print(f"Contact {name} does not exist.")

phonebook={}

while True:
    line=input()
    try:
        name, phone = line.split("-")
        phonebook[name]=phone
    except ValueError:
        n= int(line)
        break

for i in range(n):
    print_result(input(), phonebook)



