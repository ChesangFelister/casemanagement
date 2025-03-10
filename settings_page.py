import tkinter as tk
from tkinter import messagebox
from theme import Theme  


class SettingsPage:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        """Setup the main settings UI"""
        self.clear_content()

        # Settings categories
        categories = [
            ("Profile", self.create_profile_settings),
            ("Notifications", self.create_notification_settings),
            ("Appearance", self.create_appearance_settings),
            ("Security", self.create_security_settings),
            ("Backup", self.create_backup_settings),
        ]

        # Create settings navigation
        self.create_settings_nav(categories)

    def create_settings_nav(self, categories):
        """Creates navigation buttons for different settings sections"""
        nav_frame = tk.Frame(self.parent, bg=Theme.WHITE)  # ✅ Use Theme colors
        nav_frame.pack(fill=tk.X, padx=20, pady=20)

        for text, command in categories:
            tk.Button(
                nav_frame,
                text=text,
                bg=Theme.PRIMARY,  # ✅ Use Theme color
                fg=Theme.WHITE,
                font=("Arial", 12),
                padx=15,
                pady=8,
                command=command,
            ).pack(side=tk.LEFT, padx=5)

    def create_profile_settings(self):
        """Creates the profile settings section"""
        self.clear_content()

        profile_frame = tk.Frame(self.parent, bg=Theme.WHITE)
        profile_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(
            profile_frame,
            text="Profile Settings",
            font=("Arial", 16, "bold"),
            bg=Theme.WHITE,
        ).pack(pady=10)

        # Profile form fields
        form_fields = [
            "Full Name",
            "Email",
            "Phone",
            "Bar Council ID",
            "Office Address",
        ]

        for field in form_fields:
            self.create_form_field(profile_frame, field)

    def create_form_field(self, parent, field_name):
        """Creates a labeled entry field"""
        field_frame = tk.Frame(parent, bg=Theme.WHITE)
        field_frame.pack(fill=tk.X, pady=5)

        tk.Label(
            field_frame,
            text=field_name,
            bg=Theme.WHITE,
            font=("Arial", 12),
            anchor="w",
        ).pack(side=tk.LEFT, padx=5)

        tk.Entry(field_frame, font=("Arial", 12)).pack(
            side=tk.RIGHT, expand=True, fill=tk.X, padx=5
        )

    def clear_content(self):
        """Clears the parent container before loading new content"""
        for widget in self.parent.winfo_children():
            widget.destroy()

    # Placeholder functions for other settings
    def create_notification_settings(self):
        self.clear_content()
        tk.Label(
            self.parent, text="Notification Settings", font=("Arial", 14)
        ).pack(pady=20)

    def create_appearance_settings(self):
        self.clear_content()
        tk.Label(
            self.parent, text="Appearance Settings", font=("Arial", 14)
        ).pack(pady=20)

    def create_security_settings(self):
        self.clear_content()
        tk.Label(
            self.parent, text="Security Settings", font=("Arial", 14)
        ).pack(pady=20)

    def create_backup_settings(self):
        self.clear_content()
        tk.Label(
            self.parent, text="Backup Settings", font=("Arial", 14)
        ).pack(pady=20)