import tkinter as tk
from tkinter import ttk
from theme import Theme


class ClientManagementPage:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        container = tk.Frame(self.parent, bg=Theme.WHITE)
        container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Header with search and add client button
        self.create_header(container)

        # Client cards grid
        self.create_client_grid(container)

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
            relief="flat",
            placeholder="Search clients...",
        ).pack(side=tk.LEFT, ipady=5)

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

    def create_client_grid(self, parent):
        grid_frame = tk.Frame(parent, bg=Theme.WHITE)
        grid_frame.pack(fill=tk.BOTH, expand=True)

        # Sample client data
        clients = [
            {
                "name": "John Smith",
                "email": "john@email.com",
                "phone": "+1 234-567-8900",
                "cases": 3,
                "status": "Active",
            },
            {
                "name": "Mary Johnson",
                "email": "mary@email.com",
                "phone": "+1 234-567-8901",
                "cases": 1,
                "status": "Active",
            },
        ]

        # Create client cards
        for idx, client in enumerate(clients):
            self.create_client_card(grid_frame, client, idx)

    def create_client_card(self, parent, client, idx):
        card = tk.Frame(parent, bg=Theme.WHITE,
                        padx=20, pady=20, relief="ridge", bd=1)
        card.grid(row=idx // 3, column=idx % 3,
                  padx=10, pady=10, sticky="nsew")

        # Client name
        tk.Label(
            card, text=client["name"], font=("Arial", 16, "bold"),
            bg=Theme.WHITE
        ).pack(anchor="w")

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
        # Create new client modal
        modal = tk.Toplevel(self.parent)
        modal.title("Add New Client")
        modal.geometry("500x600")
        # self.AddClientForm(modal)