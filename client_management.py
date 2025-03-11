import tkinter as tk
from tkinter import ttk
from theme import Theme


class ClientManagementPage:
    def __init__(self, parent):
        self.parent = parent
        self.clients = [  # Initial sample data
            {"name": "John Smith", "email": "john@email.com", "phone": "+1 234-567-8900", "cases": 3, "status": "Active"},
            {"name": "Mary Johnson", "email": "mary@email.com", "phone": "+1 234-567-8901", "cases": 1, "status": "Active"},
        ]
        self.filtered_clients = self.clients[:]  # To store search results
        self.setup_ui()

    def setup_ui(self):
        self.container = tk.Frame(self.parent, bg=Theme.WHITE)
        self.container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Header with search and add client button
        self.create_header(self.container)

        # Client cards grid
        self.grid_frame = tk.Frame(self.container, bg=Theme.WHITE)
        self.grid_frame.pack(fill=tk.BOTH, expand=True)

        self.update_client_grid()

    def create_header(self, parent):
        header = tk.Frame(parent, bg=Theme.WHITE)
        header.pack(fill=tk.X, pady=(0, 20))

        # Search bar
        search_frame = tk.Frame(header, bg=Theme.BACKGROUND, padx=10, pady=5)
        search_frame.pack(side=tk.LEFT)

        self.search_entry = tk.Entry(
            search_frame,
            font=("Arial", 12),
            bg=Theme.BACKGROUND,
            width=40,
            relief="flat"
        )
        self.search_entry.pack(side=tk.LEFT, ipady=5)
        self.search_entry.bind("<KeyRelease>", self.search_clients)

        # Add client button
        tk.Button(
            header,
            text="+ New Client",
            bg=Theme.SECONDARY,
            fg=Theme.WHITE,
            font=("Arial", 12),
            padx=20,
            pady=8,
            relief="flat",
            cursor="hand2",
            command=self.add_new_client,
        ).pack(side=tk.RIGHT)

    def update_client_grid(self):
        """Refreshes the client grid when adding new clients or searching."""
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        for idx, client in enumerate(self.filtered_clients):
            self.create_client_card(self.grid_frame, client, idx)

    def create_client_card(self, parent, client, idx):
        """Creates a styled client card."""
        card = tk.Frame(parent, bg=Theme.WHITE, padx=20, pady=20, relief="ridge", bd=1)
        card.grid(row=idx // 3, column=idx % 3, padx=10, pady=10, sticky="nsew")

        # Client name
        tk.Label(card, text=client["name"], font=("Arial", 16, "bold"), bg=Theme.WHITE).pack(anchor="w")

        # Client details
        details = [
            ("📧", client["email"]),
            ("📱", client["phone"]),
            ("📁", f"{client['cases']} Cases"),
            ("⭐", client["status"]),
        ]

        for icon, text in details:
            tk.Label(
                card,
                text=f"{icon} {text}",
                font=("Arial", 12),
                bg=Theme.WHITE,
                fg=Theme.TEXT_SECONDARY,
            ).pack(anchor="w", pady=2)

        # Action buttons
        button_frame = tk.Frame(card, bg=Theme.WHITE)
        button_frame.pack(fill=tk.X, pady=(15, 0))

        actions = [("View Profile", Theme.PRIMARY), ("Edit", Theme.SECONDARY)]

        for text, color in actions:
            tk.Button(
                button_frame,
                text=text,
                bg=color,
                fg=Theme.WHITE,
                font=("Arial", 11),
                padx=15,
                pady=5,
                relief="flat",
                cursor="hand2",
            ).pack(side=tk.LEFT, padx=5)

    def add_new_client(self):
        """Opens a modal to add a new client."""
        modal = tk.Toplevel(self.parent)
        modal.title("Add New Client")
        modal.geometry("400x500")
        modal.configure(bg=Theme.WHITE)

        tk.Label(modal, text="Add Client", font=("Arial", 16, "bold"), bg=Theme.WHITE).pack(pady=10)

        form_frame = tk.Frame(modal, bg=Theme.WHITE)
        form_frame.pack(pady=10, padx=20, fill=tk.BOTH)

        fields = ["Name", "Email", "Phone", "Cases", "Status"]
        self.client_data = {}

        for field in fields:
            tk.Label(form_frame, text=field, font=("Arial", 12), bg=Theme.WHITE).pack(anchor="w", pady=5)
            entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
            entry.pack(anchor="w", ipady=3, pady=2)
            self.client_data[field] = entry

        # Save Button
        tk.Button(
            modal,
            text="Save Client",
            bg=Theme.PRIMARY,
            fg=Theme.WHITE,
            font=("Arial", 12),
            padx=20,
            pady=8,
            relief="flat",
            cursor="hand2",
            command=lambda: self.save_client(modal),
        ).pack(pady=15)

    def save_client(self, modal):
        """Saves the new client and updates the UI."""
        new_client = {
            "name": self.client_data["Name"].get(),
            "email": self.client_data["Email"].get(),
            "phone": self.client_data["Phone"].get(),
            "cases": int(self.client_data["Cases"].get() or 0),
            "status": self.client_data["Status"].get(),
        }

        # Ensure all fields are filled
        if not all(new_client.values()):
            return

        self.clients.append(new_client)
        self.filtered_clients = self.clients[:]
        self.update_client_grid()
        modal.destroy()

    def search_clients(self, event=None):
        """Filters clients based on search input."""
        query = self.search_entry.get().lower()
        if query:
            self.filtered_clients = [client for client in self.clients if query in client["name"].lower()]
        else:
            self.filtered_clients = self.clients[:]

        self.update_client_grid()
