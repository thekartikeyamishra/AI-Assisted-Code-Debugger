def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return f"Error reading file : {e}"


def save_report(report, file_path):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(report)
    except Exception as e:
        print(f"Error saving report : {e}")
