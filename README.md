# AI-Assisted-Code-Debugger
The AI-Assisted Code Debugger is a Python-based tool that identifies basic syntax and logical errors in code using static code analysis techniques. This tool is designed to help developers detect and fix common coding mistakes quickly, improving code quality and development efficiency.

# AI-Assisted Code Debugger (Basic Version)

## Overview

The **AI-Assisted Code Debugger** is a Python-based tool that identifies basic syntax and logical errors in code using static code analysis techniques. This tool is designed to help developers detect and fix common coding mistakes quickly, improving code quality and development efficiency.

---

## Features

1. **Syntax Error Detection**:
   - Parses code to identify common syntax errors.
2. **Logical Error Detection**:
   - Highlights potential logical issues using static code analysis tools like **pylint** or **flake8**.
3. **Support for Multiple Languages**:
   - Primarily supports Python but can be extended for other languages.
4. **User-Friendly GUI**:
   - Built with **Tkinter** for ease of use.
5. **File Input and Analysis**:
   - Upload a file for debugging and view results in real-time.

---

## Folder Structure

Here’s the folder structure of the project:

```bash
CodeDebugger/
├── data/
│   ├── sample_code/              # Sample code files for testing
├── gui/
│   ├── __init__.py               # Initializes the GUI module
│   ├── debugger_gui.py           # Tkinter GUI for the application
├── utils/
│   ├── __init__.py               # Initializes the utils module
│   ├── static_analysis.py        # Static code analysis logic
│   ├── file_handler.py           # File upload and handling logic
├── main.py                       # Entry point to run the application
├── requirements.txt              # Dependencies required for the project
├── README.md                     # Documentation for the project
```

---

## Installation and Setup

### **Prerequisites**

Ensure you have the following installed:
- **Python 3.8+**

---

### **Installation Steps**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/thekartikeyamishra/AI-Assisted-Code-Debugger.git
   cd CodeDebugger
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python main.py
   ```

---

## How to Use

1. Launch the application by running `main.py`.
2. Upload a Python file using the **Upload File** button.
3. Click **Analyze Code** to view detected syntax or logical errors.
4. Review results displayed in the output window.

---

## Example Output

### Input Code (Example `sample_code.py`):
```python
def add(a, b)
    return a + b
```

### Output:
```
Syntax Error: Missing colon at line 1
```

---

## Dependencies

The project uses the following libraries:
- **pylint**: For static code analysis.
- **tkinter**: For building the graphical user interface.
- **os**: For file handling.

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## Folder Structure

Here’s how the project is organized:

```bash
CodeDebugger/
├── data/
│   ├── sample_code/              # Sample code files for testing
├── gui/
│   ├── __init__.py               # Initializes the GUI module
│   ├── debugger_gui.py           # Tkinter GUI for the application
├── utils/
│   ├── __init__.py               # Initializes the utils module
│   ├── static_analysis.py        # Static code analysis logic
│   ├── file_handler.py           # File upload and handling logic
├── main.py                       # Entry point to run the application
├── requirements.txt              # Dependencies required for the project
├── README.md                     # Documentation for the project
```

---

## Future Enhancements

1. Add support for additional programming languages (e.g., Java, C++).
2. Implement auto-fix suggestions for common issues.
3. Integrate advanced AI models for deeper logical analysis.

---

## Acknowledgments

- **Pylint**: For static code analysis.
- **Python**: The programming language used to build this tool.
- **Tkinter**: For the graphical interface.
```

---

### **Summary**

This **README file** and **folder structure** ensure clarity and ease of use for developers using or contributing to the project. Let me know if you'd like further guidance or enhancements!
