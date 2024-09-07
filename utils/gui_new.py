import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
from ttkthemes import ThemedTk  # 
from tkinter import ttk  # 

# validate inputs
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
        
        # Example of generated testbench code (Replace with your own function)
        testbench_code = f"module {module_name}_tb;\n" + "\n".join([f"reg {inp};" for inp in input_names]) + \
                         "\n" + "\n".join([f"wire {out};" for out in output_names]) + \
                         f"\n\n// Instantiate the {module_name} module\n" \
                         f"{module_name} uut (\n" + \
                         ",\n".join([f".{inp}({inp})" for inp in input_names]) + \
                         ",\n" + \
                         ",\n".join([f".{out}({out})" for out in output_names]) + ");\n"
        
        # generated testbench in the text box
        result_box.config(state=tk.NORMAL)
        result_box.delete(1.0, tk.END)
        result_box.insert(tk.END, testbench_code)
        highlight_syntax(testbench_code)
        result_box.config(state=tk.DISABLED)

# highlight syntax 
def highlight_syntax(code):
    result_box.tag_remove("keyword", 1.0, tk.END)
    result_box.tag_remove("comment", 1.0, tk.END)
    
    keywords = ["module", "reg", "wire", "initial", "begin", "end", "$monitor", "$dumpfile", "$dumpvars", "$finish"]
    
    result_box.config(state=tk.NORMAL)
    for keyword in keywords:
        start = 1.0
        while True:
            pos = result_box.search(r"\b" + keyword + r"\b", start, stopindex=tk.END, regexp=True)
            if not pos:
                break
            end = f"{pos}+{len(keyword)}c"
            result_box.tag_add("keyword", pos, end)
            start = end
    
    start = 1.0
    while True:
        pos = result_box.search("//", start, stopindex=tk.END)
        if not pos:
            break
        end = result_box.search("\n", pos, stopindex=tk.END)
        result_box.tag_add("comment", pos, end)
        start = end
    
    
    result_box.tag_config("keyword", foreground="cyan", font=("Courier", 10, "bold"))
    result_box.tag_config("comment", foreground="light green", font=("Courier", 10, "italic"))
    result_box.config(state=tk.DISABLED)


def copy_to_clipboard():
    result_box.config(state=tk.NORMAL)
    testbench_code = result_box.get(1.0, tk.END)
    root.clipboard_clear()
    root.clipboard_append(testbench_code)
    messagebox.showinfo("Copied", "Testbench code copied to clipboard!")

#
def save_to_file():
    testbench_code = result_box.get(1.0, tk.END)
    if testbench_code.strip():
        file_path = filedialog.asksaveasfilename(defaultextension=".v", filetypes=[("Verilog Files", "*.v"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(testbench_code)
            messagebox.showinfo("Saved", "Testbench saved successfully!")
    else:
        messagebox.showwarning("Empty", "No testbench code to save.")
if __name__ == "__main__":

    root = ThemedTk(theme="equilux")  
    root.title("Verilog Testbench Generator")

    #
    style = ttk.Style()
    root.configure(bg='#2B2B2B')  #

    style.configure('TLabel', background='#2B2B2B', foreground='white', font=('Arial', 12))
    style.configure('TEntry', fieldbackground='#3C3F41', foreground='white', background='#2B2B2B')
    style.configure('TButton', background='#3C3F41', foreground='white', padding=6, font=('Arial', 12))

    # Module Name Label and Entry
    module_name_label = ttk.Label(root, text="Module Name:")
    module_name_label.grid(row=0, column=0, padx=10, pady=5)
    module_name_field = ttk.Entry(root)
    module_name_field.grid(row=0, column=1, padx=10, pady=5)

    # Input Names Label and Entry
    input_label = ttk.Label(root, text="Input Names (comma-separated):")
    input_label.grid(row=1, column=0, padx=10, pady=5)
    input_field = ttk.Entry(root)
    input_field.grid(row=1, column=1, padx=10, pady=5)

    # Output Names Label and Entry
    output_label = ttk.Label(root, text="Output Names (comma-separated):")
    output_label.grid(row=2, column=0, padx=10, pady=5)
    output_field = ttk.Entry(root)
    output_field.grid(row=2, column=1, padx=10, pady=5)

    # Button to generate the testbench
    generate_button = ttk.Button(root, text="Generate Testbench", command=on_generate)
    generate_button.grid(row=3, columnspan=2, padx=10, pady=10)

    # Scrolled text widget to display the result
    result_box = scrolledtext.ScrolledText(root, width=60, height=20, font=("Courier", 10), background='#2B2B2B', foreground='white', insertbackground='white')
    result_box.grid(row=4, columnspan=2, padx=10, pady=10)

    # Button to copy the generated testbench code to clipboard
    copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
    copy_button.grid(row=5, columnspan=2, padx=10, pady=10)

    # Button to save to file
    save_button = ttk.Button(root, text="Save to File", command=save_to_file)
    save_button.grid(row=6, columnspan=2, padx=10, pady=10)

    root.mainloop()
