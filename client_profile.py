import tkinter as tk
from tkinter import ttk
from theme import Theme

class ClientProfileView:

    def __init__(self, parent, client_id):
        self.parent = parent
        self.client_id = client_id
        self.client_data = self.load_client_data(client_id)
        self.setup_profile()
        self.apply_styles()

    def load_client_data(self, client_id):
        # Implement the logic to load client data based on client_id
        # For now, return an empty dictionary as a placeholder
        return {}

    def apply_styles(self):
        style = ttk.Style()
        style.configure("Profile.TNotebook", background=Theme.WHITE, padding=10)
        style.configure("Profile.TNotebook.Tab", padding=[20, 10], font=Theme.BODY_FONT, background=Theme.WHITE, foreground=Theme.TEXT_PRIMARY)
        style.map("Profile.TNotebook.Tab", background=[("selected", Theme.PRIMARY)], foreground=[("selected", Theme.WHITE)])

    def create_tabbed_content(self, parent):
        notebook = ttk.Notebook(parent, style="Profile.TNotebook")
        notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tabs = {
            "Overview": self.create_overview_tab,
            "Cases": self.create_cases_tab,
            "Documents": self.create_documents_tab,
            "Billing": self.create_billing_tab
        }
        
        for tab_name, create_func in tabs.items():
            tab = tk.Frame(notebook, bg=Theme.WHITE)
            create_func(tab)
            notebook.add(tab, text=tab_name)

    def create_overview_tab(self, parent):
        stats_frame = tk.Frame(parent, bg=Theme.WHITE)
        stats_frame.pack(fill=tk.X, pady=20)
        
        stats = [
            ("Active Cases", "5", Theme.PRIMARY),
            ("Pending Documents", "3", Theme.WARNING),
            ("Total Billing", "$12,500", Theme.SUCCESS)
        ]
        
        for title, value, color in stats:
            self.create_stat_card(stats_frame, title, value, color)

    def create_stat_card(self, parent, title, value, color):
        card = tk.Frame(parent, bg=Theme.WHITE, relief="ridge", bd=1)
        card.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        tk.Label(card, text=value, font=("DM Sans", 24, "bold"), fg=color, bg=Theme.WHITE).pack(pady=(15, 5))
        tk.Label(card, text=title, font=Theme.BODY_FONT, fg=Theme.TEXT_SECONDARY, bg=Theme.WHITE).pack(pady=(0, 15))

    def create_cases_tab(self, parent):
        pass

    def create_documents_tab(self, parent):
        pass

    def create_billing_tab(self, parent):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x800")
    ClientProfileView(root, client_id=1)  # Assuming a default client_id of 1
    root.mainloop()