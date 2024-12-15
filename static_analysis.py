import subprocess


def analyze_code(file_path):
    try:
        result = subprocess.run(
            ["pylint", file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return result.stdout
    except Exception as e:
        return f"Error during analysis : {e}"
