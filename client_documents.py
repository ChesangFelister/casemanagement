class ClientDocumentManager:
    def __init__(self, parent, client_id):
        self.parent = parent
        self.client_id = client_id
        self.setup_document_manager()

    def setup_document_manager(self):
        container = tk.Frame(self.parent, bg=Theme.WHITE)
        container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Document toolbar
        self.create_toolbar(container)

        # Document grid
        self.create_document_grid(container)

    def create_toolbar(self, parent):
        toolbar = tk.Frame(parent, bg=Theme.WHITE)
        toolbar.pack(fill=tk.X, pady=(0, 20))

        # Upload button
        tk.Button(
            toolbar,
            text="📄 Upload Document",
            bg=Theme.SECONDARY,
            fg=Theme.WHITE,
            font=("Arial", 12),
            padx=20,
            pady=8,
            command=self.upload_document,
        ).pack(side=tk.LEFT)

        # View options
        view_frame = tk.Frame(toolbar, bg=Theme.WHITE)
        view_frame.pack(side=tk.RIGHT)

        views = [("Grid View", "grid"), ("List View", "list")]
        self.view_var = tk.StringVar(value="grid")

        for text, value in views:
            tk.Radiobutton(
                view_frame,
                text=text,
                value=value,
                variable=self.view_var,
                bg=Theme.WHITE,
                command=self.toggle_view,
            ).pack(side=tk.LEFT, padx=10)

    def create_document_grid(self, parent):
        # Sample documents
        documents = [
            {"name": "Contract.pdf", "type": "PDF", "date": "2024-01-15"},
            {"name": "ID Card.jpg", "type": "Image", "date": "2024-01-10"},
            {"name": "Agreement.docx", "type": "Word", "date": "2024-01-05"},
        ]

        for doc in documents:
            self.create_document_card(parent, doc)

    def create_document_card(self, parent, doc):
        card = tk.Frame(parent, bg=Theme.WHITE, padx=15, pady=15, relief="ridge", bd=1)
        card.pack(fill=tk.X, pady=5)

        tk.Label(
            card, text=f"📄 {doc['name']}", font=("Arial", 12, "bold"), bg=Theme.WHITE
        ).pack(side=tk.LEFT)

        tk.Label(
            card,
            text=doc["date"],
            font=("Arial", 10),
            fg=Theme.TEXT_SECONDARY,
            bg=Theme.WHITE,
        ).pack(side=tk.RIGHT)
