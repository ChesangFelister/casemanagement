class SettingsPage:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
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
        nav_frame = tk.Frame(self.parent, bg=Theme.WHITE)
        nav_frame.pack(fill=tk.X, padx=20, pady=20)

        for text, command in categories:
            tk.Button(
                nav_frame,
                text=text,
                bg=Theme.PRIMARY,
                fg=Theme.WHITE,
                font=Theme.BODY_FONT,
                padx=15,
                pady=8,
                command=command,
            ).pack(side=tk.LEFT, padx=5)

    def create_profile_settings(self):
        profile_frame = tk.Frame(self.parent, bg=Theme.WHITE)
        profile_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Profile picture
        photo_frame = tk.Frame(profile_frame, bg=Theme.WHITE)
        photo_frame.pack(pady=20)

        # Profile form
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
            field_frame = tk.Frame(parent, bg=self.Theme.WHITE)
            field_frame.pack(fill=tk.X, pady=5)

            label = tk.Label(field_frame, text=field_name, bg=self.Theme.WHITE, font=self.Theme.BODY_FONT)
            label.pack(side=tk.LEFT)

            entry = tk.Entry(field_frame, font=self.Theme.BODY_FONT)
            entry.pack(side=tk.RIGHT, expand=True, fill=tk.X)