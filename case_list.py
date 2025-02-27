import tkinter as tk
from tkinter import ttk
from theme import Theme

class CaseListPage:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        # Main container
        container = tk.Frame(self.parent, bg=Theme.WHITE)
        container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Header with search and filters
        self.create_header(container)

        # Cases table
        self.create_cases_table(container)

    def create_header(self, parent):
        header = tk.Frame(parent, bg=Theme.WHITE)
        header.pack(fill=tk.X, pady=(0, 20))

        # Search bar
        search_frame = tk.Frame(header, bg=Theme.BACKGROUND, padx=10, pady=5)
        search_frame.pack(side=tk.LEFT)

        tk.Entry(
            search_frame,
            font=("Arial", 12),
            bg=Theme.BACKGROUND,
            width=40,
            relief="flat"
        ).pack(side=tk.LEFT, ipady=5)

        # Filter buttons
        filters = ["All Cases", "Active", "Pending", "Closed"]
        filter_frame = tk.Frame(header, bg=Theme.WHITE)
        filter_frame.pack(side=tk.RIGHT)

        for filter_text in filters:
            bg_color = Theme.PRIMARY if filter_text == "All Cases" else Theme.BACKGROUND
            fg_color = Theme.WHITE if filter_text == "All Cases" else Theme.TEXT_PRIMARY
            tk.Button(
                filter_frame,
                text=filter_text,
                bg=bg_color,
                fg=fg_color,
                font=("Arial", 11),
                padx=15,
                pady=5,
                relief="flat",
                cursor="hand2"
            ).pack(side=tk.LEFT, padx=5)
    def create_cases_table(self, parent):
        columns = (
            "Case ID",
            "Title",
            "Client",
            "Type",
            "Status",
            "Next Hearing",
            "Actions"
        )

        tree = ttk.Treeview(
            parent,
            columns=columns,
            show="headings",
            height=20
        )

        # Configure headers
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)

        # Sample data
        sample_cases = [
            ("C001", "Smith vs State", 
             "John Smith", "Criminal", "Active", "2024-02-15", ""),
            ("C002", "Property Dispute", "Mary Johnson", 
             "Civil", "Pending", "2024-02-20", ""),
            ("C003", "Corporate Merger", "Tech Corp",
             "Corporate", "Active", "2024-02-18", ""),
            ("C004", "Divorce Case", 
             "Robert Brown", "Family", "Closed", "N/A", "")
        ]

        # Insert sample data
        for case in sample_cases:
            tree.insert("", tk.END, values=case)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(
            parent,
            orient=tk.VERTICAL,
            command=tree.yview
        )
        tree.configure(yscrollcommand=scrollbar.set)

        # Pack elements
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

class CaseListPage:
    # Assuming the class definition is here
    pass


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x800")
    CaseListPage(root)
    root.mainloop()