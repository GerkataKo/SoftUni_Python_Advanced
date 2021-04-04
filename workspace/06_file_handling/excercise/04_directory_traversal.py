import os
import pathlib


def extract_files(dir):
    return [file for file in dir if os.path.isfile(file)]


def report_for_file_extensions(files):
    report = {}
    for file in files:
        file_name, extension = os.path.splitext(file)
        if extension not in report:
            report[extension] = []
        report[extension].append(file_name)
    return report


files = extract_files(os.listdir())
files_report = report_for_file_extensions(files)
report_text = ""
for extension, file_names in sorted(files_report.items(), key=lambda x: x[0]):
    report_text += f"{extension}\n"
    for name in file_names:
        report_text += f"- - - {name}{extension}\n"

desktop = pathlib.Path.home() / "Desktop"
with open(os.path.join(desktop, "report.txt"), "w") as file:
    file.write(report_text)
