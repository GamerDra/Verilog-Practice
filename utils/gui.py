import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import itertools
from test import generate_verilog_testbench
from ttkthemes import ThemedTk
from tkinter import filedialog


# Function to validate inputs
def validate_inputs():
    if not module_name_field.get().strip():
        messagebox.showwarning("Invalid Input", "Module name cannot be empty.")
        return False
    if not input_field.get().strip():
        messagebox.showwarning("Invalid Input", "Input names cannot be empty.")
        return False
    if not output_field.get().strip():
        messagebox.showwarning("Invalid Input", "Output names cannot be empty.")
        return False
    return True

def on_generate():
    if validate_inputs():
        input_names = input_field.get().split(',')
        output_names = output_field.get().split(',')
        module_name = module_name_field.get()
        
        # Generate the testbench
        testbench_code = generate_verilog_testbench(input_names, output_names, module_name)
        
        # Display the generated testbench in the text box
        result_box.config(state=tk.NORMAL)
        result_box.delete(1.0, tk.END)
        result_box.insert(tk.END, testbench_code)
        highlight_syntax(testbench_code)
        result_box.config(state=tk.DISABLED)
    
    

# Function to highlight syntax in the text box
def highlight_syntax(code):
    # Clear previous tags
    result_box.tag_remove("keyword", 1.0, tk.END)
    result_box.tag_remove("comment", 1.0, tk.END)
    
    # Define keywords and apply tags
    keywords = ["module", "reg", "wire", "initial", "begin", "end", "$monitor", "$dumpfile", "$dumpvars", "$finish"]
    for keyword in keywords:
        start = 1.0
        while True:
            pos = result_box.search(r"\b" + keyword + r"\b", start, stopindex=tk.END, regexp=True)
            if not pos:
                break
            end = f"{pos}+{len(keyword)}c"
            result_box.tag_add("keyword", pos, end)
            start = end
    
    # Highlight comments
    start = 1.0
    while True:
        pos = result_box.search("//", start, stopindex=tk.END)
        if not pos:
            break
        end = result_box.search("\n", pos, stopindex=tk.END)
        result_box.tag_add("comment", pos, end)
        start = end
    
    # Configure tag styles
    result_box.tag_config("keyword", foreground="blue", font=("Courier", 10, "bold"))
    result_box.tag_config("comment", foreground="green", font=("Courier", 10, "italic"))

# Function to copy the testbench code to clipboard
def copy_to_clipboard():
    result_box.config(state=tk.NORMAL)
    testbench_code = result_box.get(1.0, tk.END)
    root.clipboard_clear()
    root.clipboard_append(testbench_code)
    messagebox.showinfo("Copied", "Testbench code copied to clipboard!")


# Function to save the testbench code to a file
def save_to_file():
    testbench_code = result_box.get(1.0, tk.END)
    if testbench_code.strip():  # Only proceed if the testbench isn't empty
        file_path = filedialog.asksaveasfilename(defaultextension=".v", filetypes=[("Verilog Files", "*.v"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(testbench_code)
            messagebox.showinfo("Saved", "Testbench saved successfully!")
    else:
        messagebox.showwarning("Empty", "No testbench code to save.")


# Create the main window



# Replace root with ThemedTk window
root = ThemedTk(theme="equilux")  # Dark theme

root.title("Verilog Testbench Generator")

# Module Name Label and Entry
module_name_label = tk.Label(root, text="Module Name:")
module_name_label.grid(row=0, column=0, padx=10, pady=5)
module_name_field = tk.Entry(root)
module_name_field.grid(row=0, column=1, padx=10, pady=5)

# Input Names Label and Entry
input_label = tk.Label(root, text="Input Names (comma-separated):")
input_label.grid(row=1, column=0, padx=10, pady=5)
input_field = tk.Entry(root)
input_field.grid(row=1, column=1, padx=10, pady=5)

# Output Names Label and Entry
output_label = tk.Label(root, text="Output Names (comma-separated):")
output_label.grid(row=2, column=0, padx=10, pady=5)
output_field = tk.Entry(root)
output_field.grid(row=2, column=1, padx=10, pady=5)

# Button to generate the testbench
generate_button = tk.Button(root, text="Generate Testbench", command=on_generate)
generate_button.grid(row=3, columnspan=2, padx=10, pady=10)

# Scrolled text widget to display the result
result_box = scrolledtext.ScrolledText(root, width=60, height=20, font=("Courier", 10))
result_box.grid(row=4, columnspan=2, padx=10, pady=10)

# Button to copy the generated testbench code to clipboard
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=5, columnspan=2, padx=10, pady=10)

save_button = tk.Button(root, text="Save to File", command=save_to_file)
save_button.grid(row=6, columnspan=2, padx=10, pady=10)



root.mainloop()

