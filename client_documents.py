import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from theme import Theme
from pathlib import Path
import shutil
import os
from datetime import datetime


class ClientDocumentManager:
    def __init__(self, parent, client_id):
        self.parent = parent
        self.client_id = client_id
        self.documents = []
        self.current_view = "grid"

        # Main container with modern styling
        self.main_container = tk.Frame(self.parent, bg=Theme.BACKGROUND)
        self.main_container.pack(fill=tk.BOTH, expand=True)

        # Create header section
        self.create_header()

        # Create search bar
        self.create_search_bar()

        # Create toolbar with modern buttons
        self.create_toolbar()

        # Create main content area
        self.content_frame = tk.Frame(self.main_container, bg=Theme.BACKGROUND)
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Initialize the grid frame
        self.grid_frame = tk.Frame(self.content_frame, bg=Theme.BACKGROUND)
        self.grid_frame.pack(fill=tk.BOTH, expand=True)

        self.load_documents()
        self.refresh_view()

    def create_header(self):
        header = tk.Frame(self.main_container, bg=Theme.PRIMARY)
        header.pack(fill=tk.X, padx=20, pady=(20, 0))

        title = tk.Label(
            header,
            text="Document Management",
            font=("Arial", 24, "bold"),
            fg=Theme.WHITE,
            bg=Theme.PRIMARY,
        )
        title.pack(side=tk.LEFT, pady=20)

        doc_count = tk.Label(
            header,
            text=f"Total Documents: {len(self.documents)}",
            font=("Arial", 12),
            fg=Theme.WHITE,
            bg=Theme.PRIMARY,
        )
        doc_count.pack(side=tk.RIGHT, pady=20)

    def create_search_bar(self):
        search_frame = tk.Frame(self.main_container, bg=Theme.BACKGROUND)
        search_frame.pack(fill=tk.X, padx=20, pady=10)

        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(
            search_frame, textvariable=self.search_var, font=("Arial", 12), width=40
        )
        search_entry.pack(side=tk.LEFT, pady=10)
        search_entry.insert(0, "Search documents...")
        search_entry.bind(
            "<FocusIn>",
            lambda e: search_entry.delete(0, tk.END)
            if search_entry.get() == "Search documents..."
            else None,
        )

        search_btn = tk.Button(
            search_frame,
            text="🔍 Search",
            command=self.search_documents,
            bg=Theme.SECONDARY,
            fg=Theme.WHITE,
            font=("Arial", 10),
            padx=15,
            pady=5,
        )
        search_btn.pack(side=tk.LEFT, padx=5)

    def create_toolbar(self):
        toolbar = tk.Frame(self.main_container, bg=Theme.BACKGROUND)
        toolbar.pack(fill=tk.X, padx=20, pady=10)

        # Modern upload button
        upload_btn = tk.Button(
            toolbar,
            text="📤 Upload Document",
            command=self.upload_document,
            bg=Theme.PRIMARY,
            fg=Theme.WHITE,
            font=("Arial", 12),
            padx=20,
            pady=10,
            relief=tk.FLAT,
            cursor="hand2",
        )
        upload_btn.pack(side=tk.LEFT)

        # View toggle buttons
        view_frame = tk.Frame(toolbar, bg=Theme.BACKGROUND)
        view_frame.pack(side=tk.RIGHT)

        grid_btn = tk.Button(
            view_frame,
            text="�Grid",
            command=lambda: self.set_view("grid"),
            bg=Theme.SECONDARY if self.current_view == "grid" else Theme.WHITE,
            fg=Theme.WHITE if self.current_view == "grid" else Theme.SECONDARY,
            font=("Arial", 12),
            padx=15,
            pady=5,
            relief=tk.FLAT,
            cursor="hand2",
        )
        grid_btn.pack(side=tk.LEFT, padx=5)

        list_btn = tk.Button(
            view_frame,
            text="📋List",
            command=lambda: self.set_view("list"),
            bg=Theme.SECONDARY if self.current_view == "list" else Theme.WHITE,
            fg=Theme.WHITE if self.current_view == "list" else Theme.SECONDARY,
            font=("Arial", 12),
            padx=15,
            pady=5,
            relief=tk.FLAT,
            cursor="hand2",
        )
        list_btn.pack(side=tk.LEFT)

    def search_documents(self):
        search_term = self.search_var.get().lower()
        if search_term and search_term != "search documents...":
            self.filtered_documents = [
                doc for doc in self.documents if search_term in doc["name"].lower()
            ]
            self.refresh_view(self.filtered_documents)
        else:
            self.refresh_view(self.documents)

    def set_view(self, view_type):
        self.current_view = view_type
        self.refresh_view()
