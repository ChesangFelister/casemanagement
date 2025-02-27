import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from tkcalendar import DateEntry  # type: ignore  # Ensure this is installed: `pip install tkcalendar`
from theme import Theme


class AddCasePage:
    def __init__(self, parent):
        self.parent = parent
        self.create_modal()

    def create_modal(self):
        """Creates the modal window for adding a new case."""
        self.modal = tk.Toplevel(self.parent)
        self.modal.title("Add New Case")
        self.modal.geometry("600x700")
        self.modal.configure(bg=Theme.WHITE)
        self.modal.resizable(False, False)

        form = tk.Frame(self.modal, bg=Theme.WHITE, padx=40, pady=30)
        form.pack(fill=tk.BOTH, expand=True)

        tk.Label(
            form, text="New Case Details", font=("Arial", 20, "bold"), bg=Theme.WHITE
        ).pack(anchor="w", pady=(0, 30))

        self.entries = {}
        self.fields = [
            ("Case Title", "entry"),
            (
                "Case Type",
                "combobox",
                ["Criminal", "Civil", "Corporate", "Family", "Property"],
            ),
            ("Client Name", "entry"),
            ("Court", "entry"),
            ("Judge", "entry"),
            ("Filing Date", "date"),
            ("Description", "text"),
        ]

        for field in self.fields:
            self.create_form_field(form, field)

        # Buttons
        button_frame = tk.Frame(form, bg=Theme.WHITE)
        button_frame.pack(fill=tk.X, pady=20)

        tk.Button(
            button_frame,
            text="Cancel",
            bg=Theme.BACKGROUND,
            fg=Theme.TEXT_PRIMARY,
            font=("Arial", 12),
            padx=30,
            pady=10,
            command=self.modal.destroy,
        ).pack(side=tk.LEFT)

        tk.Button(
            button_frame,
            text="Save Case",
            bg=Theme.SECONDARY,
            fg=Theme.WHITE,
            font=("Arial", 12, "bold"),
            padx=30,
            pady=10,
            command=self.save_case,
        ).pack(side=tk.LEFT, padx=10)

        tk.Button(
            button_frame,
            text="Submit",
            bg=Theme.PRIMARY,  # Assuming Theme.PRIMARY is defined
            fg=Theme.WHITE,
            font=("Arial", 12, "bold"),
            padx=30,
            pady=10,
            command=self.submit_case,
        ).pack(side=tk.RIGHT)

    def create_form_field(self, parent, field):
        """Creates form fields dynamically."""
        label, field_type, *options = field

        tk.Label(parent, text=label, font=("Arial", 12), bg=Theme.WHITE).pack(
            anchor="w", pady=(10, 5)
        )

        if field_type == "entry":
            entry = tk.Entry(
                parent, font=("Arial", 12), bg=Theme.BACKGROUND, relief="flat", width=40
            )
            entry.pack(fill=tk.X, ipady=8)
            self.entries[label] = entry

        elif field_type == "combobox":
            combo = ttk.Combobox(
                parent,
                values=options[0],
                font=("Arial", 12),
                state="readonly",
                width=38,
            )
            combo.pack(fill=tk.X, ipady=4)
            self.entries[label] = combo

        elif field_type == "text":
            text = tk.Text(
                parent,
                font=("Arial", 12),
                bg=Theme.BACKGROUND,
                relief="flat",
                height=4,
                width=40,
            )
            text.pack(fill=tk.X)
            self.entries[label] = text

        elif field_type == "date":
            date = DateEntry(
                parent,
                font=("Arial", 12),
                background=Theme.SECONDARY,
                foreground=Theme.WHITE,
                width=38,
            )
            date.pack(fill=tk.X, ipady=4)
            self.entries[label] = date

    def save_case(self):
        """Validates and saves the case details into the database."""
        case_data = self.get_case_data()
        if not case_data:
            return

        self.insert_into_db(case_data)
        messagebox.showinfo("Success", "Case saved successfully!")
        self.modal.destroy()

    def submit_case(self):
        """Handles case submission."""
        case_data = self.get_case_data()
        if not case_data:
            return

        self.insert_into_db(case_data)
        messagebox.showinfo("Submitted", "Case submitted successfully!")
        self.modal.destroy()

    def get_case_data(self):
        """Retrieves and validates case details."""
        case_data = {}
        for label, widget in self.entries.items():
            if isinstance(widget, tk.Text):
                value = widget.get("1.0", tk.END).strip()
            else:
                value = widget.get().strip()
            case_data[label] = value

        # Validation
        required_fields = ["Case Title", "Client Name", "Filing Date"]
        for field in required_fields:
            if not case_data[field]:
                messagebox.showerror("Error", f"{field} is required.")
                return None

        return case_data

    def insert_into_db(self, case_data):
        """Inserts case details into the SQLite database."""
        conn = sqlite3.connect("cases.db")
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS cases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                case_title TEXT NOT NULL,
                case_type TEXT,
                client_name TEXT NOT NULL,
                court TEXT,
                judge TEXT,
                filing_date TEXT NOT NULL,
                description TEXT
            )
            """
        )
        cursor.execute(
            "INSERT INTO cases (case_title, case_type, client_name, court, judge, filing_date, description) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                case_data["Case Title"],
                case_data["Case Type"],
                case_data["Client Name"],
                case_data["Court"],
                case_data["Judge"],
                case_data["Filing Date"],
                case_data["Description"],
            ),
        )
        conn.commit()
        conn.close()
