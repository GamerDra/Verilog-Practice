from ttkthemes import ThemedTk  # For modern themes
from tkinter import ttk
from gui_new import *



root = ThemedTk(theme="arc")  # You can choose from many modern themes like "arc", "yaru", "plastik"
root.title("Verilog Testbench Generator")

# Create a style object for further customizations
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12))
style.configure('TEntry', font=('Arial', 12))
style.configure('TButton', font=('Arial', 12), padding=6)

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
result_box = scrolledtext.ScrolledText(root, width=60, height=20, font=("Courier", 10))
result_box.grid(row=4, columnspan=2, padx=10, pady=10)

# Button to copy the generated testbench code to clipboard
copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=5, columnspan=2, padx=10, pady=10)

# Button to save to file
save_button = ttk.Button(root, text="Save to File", command=save_to_file)
save_button.grid(row=6, columnspan=2, padx=10, pady=10)

root.mainloop()
