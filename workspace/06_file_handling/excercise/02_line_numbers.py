import re


def counter(pattern, line):
    return len(re.findall(pattern, line))


char_pattern = r"[^\w\s]"
let_pattern = r"[a-zA-Z]"

with open("text.txt", "r") as file:
    with open("output.txt", "w") as output:
        lines = file.readlines()
        for line_num in range(len(lines)):
            line = re.sub("\n","", lines[line_num])
            char_count = counter(char_pattern, line)
            let_count = counter(let_pattern, line)
            output.writelines(f"Line {line_num}:{line} ({let_count})({char_count}) \n")
