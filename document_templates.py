import tkinter as tk
from tkinter import messagebox


class DocumentTemplateSystem:
    def __init__(self):
        self.templates = {
            "Legal Notice": self.create_legal_notice,
            "Court Petition": self.create_petition,
            "Agreement": self.create_agreement,
            "Affidavit": self.create_affidavit,
        }

    def create_template_selector(self, parent):
        """Creates a UI section for selecting document templates."""
        selector_frame = tk.Frame(parent)
        selector_frame.pack(fill=tk.X, pady=20)

        for template_name in self.templates.keys():
            template_card = tk.Frame(selector_frame, padx=15, pady=15)
            template_card.pack(side=tk.LEFT, padx=10)

            tk.Label(
                template_card, text=template_name, font=("Arial", 12, "bold")
            ).pack()

            tk.Button(
                template_card,
                text="Use Template",
                command=lambda t=template_name: self.use_template(t),
                padx=10,
                pady=5,
            ).pack(pady=10)
    def use_template(self, template_name):
        """Handles the selection of a document template."""
        if template_name in self.templates:
            self.templates[template_name]()  # Call the appropriate method
        else:
            messagebox.showerror("Error", f"Template '{template_name}' not found!")




    def create_legal_notice(self):
        """Placeholder function for creating a legal notice."""
        messagebox.showinfo("Legal Notice", "Generating a Legal Notice template...")

    def create_petition(self):
        """Placeholder function for creating a court petition."""
        messagebox.showinfo("Court Petition", "Generating a Court Petition template...")

    def create_agreement(self):
        """Placeholder function for creating an agreement."""
        messagebox.showinfo("Agreement", "Generating an Agreement template...")

    def create_affidavit(self):
        """Placeholder function for creating an affidavit."""
        messagebox.showinfo("Affidavit", "Generating an Affidavit template...")
