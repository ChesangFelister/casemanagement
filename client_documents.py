import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from theme import Theme
from pathlib import Path
import os
from datetime import datetime
import shutil  # Ensure shutil is imported


class ClientDocumentManager:
    def __init__(self, parent, client_id):
        print("Initializing ClientDocumentManager")  # Debugging print
        self.parent = parent
        self.client_id = client_id
        self.documents = []  # Will hold uploaded documents
        self.current_view = "grid"

        # Main container with modern styling
        self.main_container = tk.Frame(self.parent, bg=Theme.BACKGROUND)
        self.main_container.pack(fill=tk.BOTH, expand=True)

        # Create header section
        self.create_header()
        self.create_search_bar()
        self.create_toolbar()

        # Create main content area
        self.content_frame = tk.Frame(self.main_container, bg=Theme.BACKGROUND)
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Initialize the grid frame
        self.grid_frame = tk.Frame(self.content_frame, bg=Theme.BACKGROUND)
        self.grid_frame.pack(fill=tk.BOTH, expand=True)
        
        # Debugging print to check if grid_frame is displayed
        print("Grid frame created:", self.grid_frame)

        # Add test documents to check if UI updates
        self.add_test_documents()

        self.refresh_view()

    def create_header(self):
        """Creates the header section with title and document count"""
        print("Creating header")  # Debugging print
        header = tk.Frame(self.main_container, bg=Theme.PRIMARY)
        header.pack(fill=tk.X, padx=20, pady=(20, 0))

        title = tk.Label(
            header,
            text="📄 Document Management",
            font=("Arial", 22, "bold"),
            fg=Theme.WHITE,
            bg=Theme.PRIMARY,
        )
        title.pack(side=tk.LEFT, pady=20)

        self.doc_count_label = tk.Label(
            header,
            text=f"Total Documents: {len(self.documents)}",
            font=("Arial", 12),
            fg=Theme.WHITE,
            bg=Theme.PRIMARY,
        )
        self.doc_count_label.pack(side=tk.RIGHT, pady=20)

    def create_search_bar(self):
        """Creates a search bar to filter documents"""
        print("Creating search bar")  # Debugging print
        search_frame = tk.Frame(self.main_container, bg=Theme.BACKGROUND)
        search_frame.pack(fill=tk.X, padx=20, pady=10)

        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=("Arial", 12),
            width=40
        )
        self.search_entry.pack(side=tk.LEFT, pady=10)
        self.search_entry.insert(0, "Search documents...")
        self.search_entry.bind(
            "<FocusIn>",
            lambda e: self.clear_search_placeholder()
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
            relief=tk.FLAT,
            cursor="hand2",
        )
        search_btn.pack(side=tk.LEFT, padx=5)

    def create_toolbar(self):
        """Creates the toolbar for document management actions"""
        print("Creating toolbar")  # Debugging print
        toolbar = tk.Frame(self.main_container, bg=Theme.BACKGROUND)
        toolbar.pack(fill=tk.X, padx=20, pady=10)

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
            text="🔳 Grid",
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
            text="📋 List",
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

    def refresh_view(self, doc_list=None):
        """Refreshes the document list view"""
        print("Refreshing view with documents:", self.documents)  # Debugging print

        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        documents = doc_list if doc_list is not None else self.documents

        if self.current_view == "grid":
            self.display_grid_view(documents)
        else:
            self.display_list_view(documents)

        self.doc_count_label.config(text=f"Total Documents: {len(documents)}")

    def display_grid_view(self, documents):
        """Displays documents in a grid format"""
        print("Displaying documents in grid view:", documents)
        for index, doc in enumerate(documents):
            frame = tk.Frame(self.grid_frame, bg=Theme.WHITE, bd=2,
                             relief=tk.RIDGE)
            frame.grid(row=index // 3, column=index % 3, padx=10, pady=10)

            label = tk.Label(
                frame, text=doc["name"], font=("Arial", 12), bg=Theme.WHITE
            )
            label.pack(padx=10, pady=10)

    def add_test_documents(self):
        """Adds test documents to check if UI updates"""
        print("Adding test documents")  # Debugging print
        self.documents = [
            {"name": "Test Document 1", "path": "/fake/path1.pdf"},
            {"name": "Test Document 2", "path": "/fake/path2.pdf"},
        ]
        self.refresh_view()

    def upload_document(self):
        """Handles document upload and storage"""
        print("Uploading document")  # Debugging print
        file_path = filedialog.askopenfilename(
            filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
        )
        if not file_path:
            return

        file_name = os.path.basename(file_path)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        new_file_name = f"{self.client_id}_{timestamp}_{file_name}"

        save_dir = Path("client_documents")
        save_dir.mkdir(parents=True, exist_ok=True)
        new_file_path = save_dir / new_file_name

        try:
            shutil.copy(file_path, new_file_path)
            self.documents.append({"name": new_file_name, "path": str(new_file_path)})
            messagebox.showinfo(
                "Success", f"Document '{file_name}' uploaded successfully!"
            )
            self.refresh_view()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to upload document: {e}")

