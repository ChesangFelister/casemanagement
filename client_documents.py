import tkinter as tk
from tkinter import filedialog, messagebox
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
        self.setup_ui()
        self.load_documents()

    def setup_ui(self):
        # Placeholder for UI setup
        pass
    def load_documents(self):
        # Create client document directory if it doesn't exist
        self.doc_dir = Path(f"client_documents/{self.client_id}")
        self.doc_dir.mkdir(parents=True, exist_ok=True)

        # Load existing documents
        for file_path in self.doc_dir.glob("*.*"):
            doc_info = {
                "name": file_path.name,
                "type": file_path.suffix[1:].upper(),
                "date": datetime.fromtimestamp(file_path.stat().st_mtime).strftime(
                    "%Y-%m-%d"
                ),
                "path": str(file_path),
            }
            self.documents.append(doc_info)

        self.refresh_view()

    def upload_document(self):
        file_paths = filedialog.askopenfilenames(
            title="Select Documents",
            filetypes=[
                ("All Files", "*.*"),
                ("PDF Files", "*.pdf"),
                ("Word Documents", "*.doc;*.docx"),
                ("Images", "*.jpg;*.jpeg;*.png"),
            ],
        )

        for file_path in file_paths:
            source_path = Path(file_path)
            dest_path = self.doc_dir / source_path.name

            try:
                shutil.copy2(source_path, dest_path)
                doc_info = {
                    "name": source_path.name,
                    "type": source_path.suffix[1:].upper(),
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "path": str(dest_path),
                }
                self.documents.append(doc_info)
                messagebox.showinfo(
                    "Success", f"Document {source_path.name} uploaded successfully"
                )
            except Exception as e:
                messagebox.showerror(
                    "Error", f"Failed to upload {source_path.name}: {str(e)}"
                )

        self.refresh_view()

    def toggle_view(self):
        self.current_view = "grid" if self.current_view == "list" else "list"
        self.refresh_view()

    def refresh_view(self):
        # Clear existing view
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        if self.current_view == "grid":
            self.create_grid_view()
        else:
            self.create_list_view()

    def create_grid_view(self):
        for doc in self.documents:
            self.create_document_card(doc)

    def create_list_view(self):
        # Create headers
        headers = tk.Frame(self.frame, bg=Theme.BACKGROUND)
        headers.pack(fill=tk.X, pady=(0, 10))

        tk.Label(headers, text="Name", width=30, anchor="w", bg=Theme.BACKGROUND).pack(
            side=tk.LEFT, padx=5
        )
        tk.Label(headers, text="Type", width=10, bg=Theme.BACKGROUND).pack(
            side=tk.LEFT, padx=5
        )
        tk.Label(headers, text="Date", width=15, bg=Theme.BACKGROUND).pack(
            side=tk.LEFT, padx=5
        )

        # Create list items
        for doc in self.documents:
            item = tk.Frame(self.frame, bg=Theme.WHITE)
            item.pack(fill=tk.X, pady=2)

            tk.Label(item, text=doc["name"], width=30, anchor="w").pack(
                side=tk.LEFT, padx=5
            )
            tk.Label(item, text=doc["type"], width=10).pack(
                side=tk.LEFT, padx=5)
            tk.Label(item, text=doc["date"], width=15).pack(
                side=tk.LEFT, padx=5)

            self.bind_hover_effects(item)
    def bind_hover_effects(self, widget):
        widget.bind("<Enter>", lambda event: widget.configure(bg=Theme.HOVER_COLOR))
        widget.bind("<Leave>", lambda event: widget.configure(bg=Theme.WHITE))


    def open_document(self, doc_path):
        try:
            os.startfile(doc_path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open document: {str(e)}")
