import tkinter as tk
from tkinter import ttk
# from PIL import Image, ImageTk  # Ensure Pillow is installed
from theme import Theme
import os  # Check if image files exist


class DashboardPage:
    def __init__(self, root):
        self.root = root

        # Main container
        self.container = tk.Frame(self.root, bg=Theme.BACKGROUND)
        self.container.pack(fill=tk.BOTH, expand=True)

        # Sidebar
        self.sidebar = tk.Frame(self.container, bg=Theme.PRIMARY, width=250)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar.pack_propagate(False)

        # Content area (Dashboard)
        self.content_frame = tk.Frame(self.container, bg=Theme.BACKGROUND)
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.create_sidebar()
        self.create_dashboard()

    def create_sidebar(self):
        """Creates the sidebar with icons & navigation."""

        # Load logo (fallback if missing)
        logo_path = "assets/logo.png"
        if os.path.exists(logo_path):
            logo_img = Image.open(logo_path).resize((80, 80), Image.LANCZOS)
            self.logo = ImageTk.PhotoImage(logo_img)
            logo_label = tk.Label(self.sidebar, image=self.logo,
                                  bg=Theme.PRIMARY)
        else:
            logo_label = tk.Label(
                self.sidebar, text="LOGO", font=("Arial", 16),
                bg=Theme.PRIMARY, fg="white"
            )
        logo_label.pack(pady=20)

        # Sidebar menu items
        menu_items = [
            ("Dashboard", "assets/Dashboard.png"),
            ("Cases", "assets/Folder_Check.png"),
            ("Calendar", "assets/Manager_Desk.png"),
            ("Documents", "assets/Document_Filled.png"),
            ("Clients", "assets/User_Circle_Single.png"),
            ("Settings", "assets/Setting.png"),
        ]

        for text, icon_path in menu_items:
            icon_img = None
            if os.path.exists(icon_path):
                icon = Image.open(icon_path).resize((25, 25), Image.LANCZOS)
                icon_img = ImageTk.PhotoImage(icon)

            btn = tk.Button(
                self.sidebar,
                text=f" {text}",
                font=("Arial", 12, "bold"),
                image=icon_img if icon_img else None,
                compound=tk.LEFT,
                bg=Theme.PRIMARY,
                fg=Theme.TEXT_PRIMARY,
                activebackground=Theme.PRIMARY,
                relief=tk.FLAT,
                padx=20,
                pady=10,
                anchor="w",
                cursor="hand2",
                command=lambda t=text: self.handle_menu_click(t),
            )
            btn.image = icon_img  # Prevent garbage collection
            btn.pack(fill=tk.X, padx=10, pady=5)
    def create_dashboard(self):
        """Creates the main dashboard UI."""
        self.clear_content()

        # Welcome Message
        tk.Label(
            self.content_frame,
            text="Welcome Back, John Doe",
            font=("Arial", 24, "bold"),
            bg=Theme.BACKGROUND,
            fg=Theme.TEXT_PRIMARY,
            pady=10,
        ).pack(anchor="w", padx=20)

        # Dashboard Stats
        stats_frame = tk.Frame(self.content_frame, bg=Theme.BACKGROUND)
        stats_frame.pack(pady=20, fill=tk.BOTH, expand=True)

        stats = [
            ("2700", "Total Cases"),
            ("1250", "Solved Cases"),
            ("1450", "Pending Cases"),
        ]

        for count, label in stats:
            card = tk.Frame(
                stats_frame, bg=Theme.PRIMARY, padx=20, pady=10,
                width=200, height=100
            )
            card.pack(side=tk.LEFT, padx=10)

            tk.Label(
                card,
                text=count,
                font=("Arial", 18, "bold"),
                bg=Theme.PRIMARY,
                fg=Theme.TEXT_PRIMARY,
            ).pack()
            tk.Label(
                card,
                text=label,
                font=("Arial", 12),
                bg=Theme.PRIMARY,
                fg=Theme.TEXT_SECONDARY,
            ).pack()

    def handle_menu_click(self, menu_item):
        """Handles sidebar navigation."""
        self.clear_content()

        if menu_item == "Dashboard":
            self.create_dashboard()
        elif menu_item == "Documents":
            from client_documents import ClientDocumentManager
            ClientDocumentManager(self.content_frame, client_id="123")  

    def clear_content(self):
        """Clears the content area before switching views."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
