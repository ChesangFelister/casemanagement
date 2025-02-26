import tkinter as tk
# from PIL import Image, ImageTk
from theme import Theme


class ClientsPage:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        # Header with search and add client button
        self.create_header()

        # Main content area with client cards
        self.create_client_cards()

        # Client details sidebar
        self.create_sidebar()

    def create_client_cards(self):
        # Implement the logic for creating client cards here
        pass

    def create_header(self):
        header = tk.Frame(self.parent, bg=Theme.WHITE)
        header.pack(fill=tk.X, padx=20, pady=20)

        # Search bar with icon
        search_frame = tk.Frame(header, bg=Theme.BACKGROUND, padx=10, pady=5)
        search_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        search_icon = Image.open("assets/search.png")
        self.search_photo = ImageTk.PhotoImage(
            search_icon
        )  # Store as instance variable
        tk.Label(search_frame, image=self.search_photo, bg=Theme.BACKGROUND).pack(
            side=tk.LEFT
        )

        tk.Entry(
            search_frame,
            font=Theme.BODY_FONT,
            bg=Theme.BACKGROUND,
            relief="flat",
            width=40,
        ).pack(side=tk.LEFT, padx=10)

        # Add client button
        tk.Button(
            header,
            text="+ New Client",
            bg=Theme.SECONDARY,
            fg=Theme.WHITE,
            font=Theme.BODY_FONT,
            padx=20,
            pady=10,
            command=self.add_new_client,
        ).pack(side=tk.RIGHT)

    def create_sidebar(self):
        # Implement sidebar creation
        pass

    def add_new_client(self):
        # Implement the logic for adding a new client here
        pass
