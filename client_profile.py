class ClientProfileView:
    def __init__(self, parent, client_id):
        self.parent = parent
        self.client_id = client_id
        self.setup_profile()

    def setup_profile(self):
        container = tk.Frame(self.parent, bg=Theme.WHITE)
        container.pack(fill=tk.BOTH, expand=True)

        # Profile header
        self.create_profile_header(container)

        # Main content with tabs
        self.create_tabbed_content(container)

    def create_profile_header(self, parent):
        header = tk.Frame(parent, bg=Theme.PRIMARY, height=200)
        header.pack(fill=tk.X)
        header.pack_propagate(False)

        # Client avatar and basic info
        info_frame = tk.Frame(header, bg=Theme.PRIMARY)
        info_frame.pack(pady=30)

        # Avatar circle
        avatar = tk.Canvas(
            info_frame, width=80, height=80, bg=Theme.SECONDARY, highlightthickness=0
        )
        avatar.create_text(
            40, 40, text="JS", fill=Theme.WHITE, font=("Arial", 24, "bold")
        )
        avatar.pack()

        # Client name and status
        tk.Label(
            info_frame,
            text="John Smith",
            font=("Arial", 24, "bold"),
            bg=Theme.PRIMARY,
            fg=Theme.WHITE,
        ).pack(pady=(10, 5))

        tk.Label(
            info_frame,
            text="Active Client • Since Jan 2024",
            font=("Arial", 12),
            bg=Theme.PRIMARY,
            fg=Theme.WHITE,
        ).pack()
