import tkinter as tk
from tkinter import filedialog, messagebox
from theme import Theme
from PIL import Image, ImageTk
import os


class DocumentsPage:
    def __init__(self, parent):
        self.parent = parent
        self.documents = []
        self.current_view = None
        self.setup_ui()

    def setup_ui(self):
        self.create_toolbar()
        self.create_documents_grid()

    def create_toolbar(self):
        toolbar = tk.Frame(self.parent, bg=Theme.WHITE)
        toolbar.pack(fill=tk.X, padx=20, pady=20)

        # Upload button
        tk.Button(
            toolbar,
            text="Upload Document",
            bg=Theme.SECONDARY,
            fg=Theme.WHITE,
            font=Theme.BODY_FONT,
            padx=20,
            pady=10,
            command=self.upload_document,
        ).pack(side=tk.LEFT)

        # View options
        self.view_mode = tk.StringVar(value="grid")
        views = [("Grid View", "grid"), ("List View", "list")]

        view_frame = tk.Frame(toolbar, bg=Theme.WHITE)
        view_frame.pack(side=tk.RIGHT)

        for text, value in views:
            tk.Radiobutton(
                view_frame,
                text=text,
                value=value,
                variable=self.view_mode,
                command=self.toggle_view,
                bg=Theme.WHITE,
            ).pack(side=tk.LEFT, padx=10)

    def create_documents_grid(self):
        if self.current_view:
            self.current_view.destroy()

        self.current_view = tk.Frame(self.parent, bg=Theme.WHITE)
        self.current_view.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        if self.view_mode.get() == "grid":
            self._create_grid_view()
        else:
            self._create_list_view()

    def _create_grid_view(self):
        for i, doc in enumerate(self.documents):
            frame = tk.Frame(self.current_view, bg=Theme.WHITE,
                             padx=10, pady=10)
            frame.grid(row=i // 3, column=i % 3, padx=10, pady=10)

            # Document icon
            icon = tk.Label(frame, text="📄", font=("Arial", 48), 
                            bg=Theme.WHITE)
            icon.pack()

            # Document name
            name = tk.Label(
                frame,
                text=os.path.basename(doc)[:20] + "...",
                font=Theme.BODY_FONT,
                bg=Theme.WHITE,
            )
            name.pack()

    def _create_list_view(self):
        headers = ["Name", "Size", "Date Modified"]

        # Create headers
        for i, header in enumerate(headers):
            tk.Label(
                self.current_view, text=header, font=Theme.BODY_FONT, 
                bg=Theme.WHITE
            ).grid(row=0, column=i, padx=10, pady=5, sticky="w")

        # Create document entries
        for i, doc in enumerate(self.documents, start=1):
            name = tk.Label(
                self.current_view,
                text=os.path.basename(doc),
                font=Theme.BODY_FONT,
                bg=Theme.WHITE,
            )
            name.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            size = os.path.getsize(doc)
            size_label = tk.Label(
                self.current_view,
                text=f"{size / 1024:.1f} KB",
                font=Theme.BODY_FONT,
                bg=Theme.WHITE,
            )
            size_label.grid(row=i, column=1, padx=10, pady=5, sticky="w")

            modified = os.path.getmtime(doc)
            date_label = tk.Label(
                self.current_view,
                text=f"{modified}",
                font=Theme.BODY_FONT,
                bg=Theme.WHITE,
            )
            date_label.grid(row=i, column=2, padx=10, pady=5, sticky="w")

    def upload_document(self):
        file_paths = filedialog.askopenfilenames(
            title="Select documents to upload",
            filetypes=[
                ("PDF files", "*.pdf"),
                ("Word files", "*.docx"),
                ("Text files", "*.txt"),
                ("All files", "*.*"),
            ],
        )

        if file_paths:
            self.documents.extend(file_paths)

            msg = f"Successfully uploaded {len(file_paths)} document(s)"
            messagebox.showinfo("Success", msg)
            self.create_documents_grid()

    def toggle_view(self):
        self.create_documents_grid()
