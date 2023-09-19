import tkinter as tk
from tkinter import ttk

class LegalCaseManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Legal Case Management")
        
        self.case_list = []
        
        # Create and configure the case list treeview
        self.case_tree = ttk.Treeview(root, columns=("Name", "Type", "Date"))
        self.case_tree.heading("#1", text="Name")
        self.case_tree.heading("#2", text="Type")
        self.case_tree.heading("#3", text="Date")
        self.case_tree.pack(padx=10, pady=10)
        
        # Create buttons for adding and viewing cases
        add_button = tk.Button(root, text="Add Case", command=self.add_case)
        view_button = tk.Button(root, text="View Case", command=self.view_case)
        
        add_button.pack(padx=10, pady=5)
        view_button.pack(padx=10, pady=5)
        
    def add_case(self):
        # Create a new window for adding a case
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Case")
        
        # Create labels and entry fields for case details
        name_label = tk.Label(add_window, text="Name:")
        type_label = tk.Label(add_window, text="Type:")
        date_label = tk.Label(add_window, text="Date:")
        
        name_entry = tk.Entry(add_window)
        type_entry = tk.Entry(add_window)
        date_entry = tk.Entry(add_window)
        
        name_label.grid(row=0, column=0, padx=10, pady=5)
        type_label.grid(row=1, column=0, padx=10, pady=5)
        date_label.grid(row=2, column=0, padx=10, pady=5)
        
        name_entry.grid(row=0, column=1, padx=10, pady=5)
        type_entry.grid(row=1, column=1, padx=10, pady=5)
        date_entry.grid(row=2, column=1, padx=10, pady=5)
        
        # Create a button to save the case
        save_button = tk.Button(add_window, text="Save Case", command=lambda: self.save_case(
            name_entry.get(), type_entry.get(), date_entry.get(), add_window))
        save_button.grid(row=3, columnspan=2, padx=10, pady=10)
    
    def save_case(self, name, case_type, date, window):
        # Add the case to the list and update the treeview
        self.case_list.append((name, case_type, date))
        self.update_case_tree()
        
        # Close the add case window
        window.destroy()
    
    def view_case(self):
        # Get the selected item in the treeview
        selected_item = self.case_tree.selection()
        
        if not selected_item:
            return
        
        # Get the case details
        case_details = self.case_list[int(selected_item[0])-1]  # Subtract 1 to account for 0-based indexing
        
        # Create a new window to display the case details
        view_window = tk.Toplevel(self.root)
        view_window.title("View Case")
        
        # Display case details
        name_label = tk.Label(view_window, text=f"Name: {case_details[0]}")
        type_label = tk.Label(view_window, text=f"Type: {case_details[1]}")
        date_label = tk.Label(view_window, text=f"Date: {case_details[2]}")
        
        name_label.pack(padx=10, pady=5)
        type_label.pack(padx=10, pady=5)
        date_label.pack(padx=10, pady=5)
    
    def update_case_tree(self):
        # Clear the treeview
        for item in self.case_tree.get_children():
            self.case_tree.delete(item)
        
        # Populate the treeview with case data
        for i, case in enumerate(self.case_list):
            self.case_tree.insert("", "end", values=(case[0], case[1], case[2]), iid=str(i+1))

if __name__ == "__main__":
    root = tk.Tk()
    app = LegalCaseManagementApp(root)
    root.mainloop()
