import tkinter as tk
from tkinter import ttk
from theme import Theme  # ✅ Ensure theme.py exists


class AddClientForm:
    def __init__(self, parent):
        self.modal = tk.Toplevel(parent)  # ✅ Create modal window
        self.modal.title("Add New Client")
        self.modal.geometry("500x600")
        self.modal.configure(bg=Theme.WHITE)
        self.modal.resizable(False, False)
        self.modal.grab_set()  # ✅ Prevent interaction with main window

        self.setup_form()

    def setup_form(self):
        container = tk.Frame(self.modal, bg=Theme.WHITE, padx=40, pady=30)
        container.pack(fill=tk.BOTH, expand=True)

        tk.Label(
            container,
            text="New Client Information",
            font=("Arial", 20, "bold"),
            bg=Theme.WHITE,
        ).pack(anchor="w", pady=(0, 30))

        fields = [
            ("Full Name", "entry"),
            ("Email", "entry"),
            ("Phone", "entry"),
            ("Address", "text"),
            ("ID/Passport", "entry"),
            ("Client Type", "combobox", ["Individual", 
                                         "Corporate", "Government"]),
            ("Notes", "text"),
        ]

        self.entries = {}
        for field in fields:
            self.create_form_field(container, field)

        button_frame = tk.Frame(container, bg=Theme.WHITE)
        button_frame.pack(fill=tk.X, pady=20)

        tk.Button(
            button_frame,
            text="Cancel",
            bg=Theme.BACKGROUND,
            fg=Theme.TEXT_PRIMARY,
            font=("Arial", 12),
            padx=30,
            pady=10,
            command=self.modal.destroy,  # ✅ Closes modal
        ).pack(side=tk.LEFT)

        tk.Button(
            button_frame,
            text="Save Client",
            bg=Theme.SECONDARY,
            fg=Theme.WHITE,
            font=("Arial", 12, "bold"),
            padx=30,
            pady=10,
            command=self.save_client,
        ).pack(side=tk.RIGHT)

    def create_form_field(self, parent, field):
        label, field_type, *options = field

        tk.Label(parent, text=label, font=("Arial", 12), bg=Theme.WHITE).pack(
            anchor="w", pady=(10, 5)
        )

        if field_type == "entry":
            widget = tk.Entry(
                parent, font=("Arial", 12), bg=Theme.BACKGROUND, 
                relief="flat", width=40
            )
            widget.pack(fill=tk.X, ipady=8)

        elif field_type == "text":
            widget = tk.Text(
                parent,
                font=("Arial", 12),
                bg=Theme.BACKGROUND,
                relief="flat",
                height=3,
                width=40,
            )
            widget.pack(fill=tk.X)

        elif field_type == "combobox":
            widget = ttk.Combobox(
                parent,
                values=options[0],
                font=("Arial", 12),
                state="readonly",
                width=38,
            )
            widget.pack(fill=tk.X, ipady=4)

        self.entries[label] = widget

    def save_client(self):
        """Collects and prints client data, then closes the modal"""
        client_data = {}
        for label, widget in self.entries.items():
            if isinstance(widget, tk.Text):
                value = widget.get("1.0", tk.END).strip()
            else:
                value = widget.get().strip()
            client_data[label] = value

        print("New client data:", client_data)
        self.modal.destroy()  # ✅ Closes the modal after saving


# ✅ Example usage: Open the form in a test environment
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # ✅ Hide main window for testing
    AddClientForm(root)
    root.mainloop()
