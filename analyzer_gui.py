import tkinter as tk
from tkinter import filedialog, messagebox
from utils.static_analysis import analyze_code
from utils.file_handler import save_report


class CodeAnalyzerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Code Analyzer")

        tk.Label(self.root, text="Upload a Python File:", font=("Helvetica", 12)).pack(pady=5)
        self.upload_button = tk.Button(self.root, text="Browse", command=self.upload_file)
        self.upload_button.pack(pady=5)

        tk.Label(self.root, text="Analysis Result", font=("Helvetica", 12)).pack(pady=5)
        self.result_text = tk.Text(self.root, height=15, width=60, wrap=tk.WORD, state=tk.DISABLED)
        self.result_text.pack(pady=5)

        self.save_button = tk.Button(self.root, text="Save Report", command=self.save_report, state=tk.DISABLED)
        self.save_button.pack(pady=5)

        self.analysis_result = None

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            self.run_analysis(file_path)

    def run_analysis(self, file_path):
        result = analyze_code(file_path)
        self.analysis_result = result

        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)
        self.result_text.config(state=tk.DISABLED)
        self.save_button.config(state=tk.NORMAL)

    def save_report(self):
        if self.analysis_result:
            save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text File", "*.txt")])
            if save_path:
                save_report(self.analysis_result, save_path)
                messagebox.showinfo("Success", "Report saved successfully!")
            else:
                messagebox.showerror("Error", "No analysis result to save.")

    def run(self):
        self.root.mainloop()
