import tkinter as tk
from tkinter import PhotoImage  # For icons
from theme import Theme

def create_sidebar(self, parent):
    """Creates a sidebar with modern styling."""
    
    # Add a logo (ensure the file exists)
    logo = PhotoImage(file="assets/logo.png")  # Place the logo in an "assets" folder
    logo_label = tk.Label(parent, image=logo, bg=Theme.PRIMARY)
    logo_label.image = logo  # Keep a reference to avoid garbage collection
    logo_label.pack(pady=10)

    menu_items = [
        ("Dashboard", "assets/dashboard.png"),
        ("Cases", "assets/cases_icon.png"),
        ("Calendar", "assets/calendar_icon.png"),
        ("Documents", "assets/DocumentFilled.png"),
        ("Clients", "assets/clients_icon.png"),
        ("Settings", "assets/settings.png"),
    ]

    for text, icon_path in menu_items:
        icon = PhotoImage(file=icon_path)
        btn = tk.Button(
            parent,
            text=f" {text}",
            font=("Arial", 12, "bold"),
            image=icon,
            compound=tk.LEFT,  # Align icon to the left
            bg=Theme.PRIMARY,
            fg=Theme.TEXT_PRIMARY,
            bd=0,
            relief=tk.FLAT,
            padx=20,
            pady=10,
            anchor="w",
            cursor="hand2",
            activebackground=Theme.BUTTON_HOVER,
            command=lambda t=text: self.handle_menu_click(t),
        )
        btn.image = icon  # Keep a reference
        btn.pack(fill=tk.X, padx=10, pady=5)
