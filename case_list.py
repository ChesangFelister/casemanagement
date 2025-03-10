import tkinter as tk
from tkinter import ttk
from theme import Theme  # Ensure theme.py exists


class CaseListPage:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        container = tk.Frame(self.parent, bg=Theme.BACKGROUND, padx=20, pady=20)
        container.pack(fill=tk.BOTH, expand=True)

        self.create_header(container)
        self.create_cases_table(container)

    def create_header(self, parent):
        """Creates the header with a search bar and filters."""
        header = tk.Frame(parent, bg=Theme.BACKGROUND)
        header.pack(fill=tk.X, pady=(0, 20))

        # Search Bar
        search_frame = tk.Frame(header, bg=Theme.WHITE, relief="ridge", bd=1)
        search_frame.pack(side=tk.LEFT, padx=10)

        self.search_entry = tk.Entry(
            search_frame,
            font=("Arial", 12),
            bg=Theme.BACKGROUND,
            fg=Theme.TEXT_SECONDARY,
            width=40,
            relief="flat",
        )
        self.search_entry.pack(side=tk.LEFT, ipady=5, padx=10, pady=5)
        self.search_entry.bind("<KeyRelease>", self.filter_cases)

        search_icon = tk.Label(
            search_frame, text="🔍", font=("Arial", 14), bg=Theme.WHITE
        )
        search_icon.pack(side=tk.RIGHT, padx=5)

        # Filter Buttons
        filters = ["All Cases", "Active", "Pending", "Closed"]
        filter_frame = tk.Frame(header, bg=Theme.BACKGROUND)
        filter_frame.pack(side=tk.RIGHT)

        self.selected_filter = tk.StringVar(value="All Cases")

        for filter_text in filters:
            bg_color = Theme.PRIMARY if filter_text == "All Cases" else Theme.WHITE
            fg_color = (
                Theme.WHITE if filter_text == "All Cases" 
                else Theme.TEXT_SECONDARY
            )

            filter_button = tk.Button(
                filter_frame,
                text=filter_text,
                bg=bg_color,
                fg=fg_color,
                font=("Arial", 11, "bold"),
                padx=15,
                pady=5,
                relief="solid",
                cursor="hand2",
                borderwidth=1,
                command=lambda ft=filter_text: self.apply_filter(ft),
            )
            filter_button.pack(side=tk.LEFT, padx=5)
    def create_cases_table(self, parent):
        """Creates a styled table for case listings."""
        columns = (
            "Case ID",
            "Title",
            "Client",
            "Type",
            "Status",
            "Next Hearing",
            "Actions",
        )

        style = ttk.Style()
        style.configure(
            "Treeview",
            font=("Arial", 11),
            rowheight=30,
            background=Theme.WHITE,
            fieldbackground=Theme.WHITE,
        )
        style.configure(
            "Treeview.Heading",
            font=("Arial", 12, "bold"),
            background=Theme.PRIMARY,
            foreground=Theme.WHITE,
        )

        tree_frame = tk.Frame(parent, bg=Theme.BACKGROUND)
        tree_frame.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(
            tree_frame, columns=columns, show="headings", height=15
        )

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=150)

        scrollbar = ttk.Scrollbar(
            tree_frame, orient=tk.VERTICAL, command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.load_sample_data()

    def load_sample_data(self):
        """Loads sample data into the table."""
        self.sample_cases = [
            (
                "C001",
                "Smith vs State",
                "John Smith",
                "Criminal",
                "Active",
                "2024-02-15",
                "🔎",
            ),
            (
                "C002",
                "Property Dispute",
                "Mary Johnson",
                "Civil",
                "Pending",
                "2024-02-20",
                "🔎",
            ),
            (
                "C003",
                "Corporate Merger",
                "Tech Corp",
                "Corporate",
                "Active",
                "2024-02-18",
                "🔎",
            ),
            ("C004", 
             "Divorce Case", 
             "Robert Brown", 
             "Family", "Closed", "N/A", "🔎"),
        ]

        for case in self.sample_cases:
            self.tree.insert("", tk.END, values=case)

    def filter_cases(self, event=None):
        """Filters cases based on search input."""
        search_text = self.search_entry.get().lower()
        self.tree.delete(*self.tree.get_children())

        for case in self.sample_cases:
            if search_text in case[1].lower() or search_text in case[2].lower():
                self.tree.insert("", tk.END, values=case)

    def apply_filter(self, filter_text):
        """Filters cases based on status."""
        self.selected_filter.set(filter_text)
        self.tree.delete(*self.tree.get_children())

        for case in self.sample_cases:
            if filter_text == "All Cases" or case[4] == filter_text:
                self.tree.insert("", tk.END, values=case)


# Run the Case List Page for Testing
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x800")
    root.configure(bg=Theme.BACKGROUND)
    CaseListPage(root)
    root.mainloop()
