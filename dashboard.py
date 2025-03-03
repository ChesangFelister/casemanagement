import tkinter as tk
from tkinter import messagebox
from add_case import AddCasePage
from case_list import CaseListPage
from calendar_page import CalendarPage
from clients_page import ClientsPage
from client_documents import ClientDocumentManager


class Theme:
    BACKGROUND = "#f0f0f0"
    PRIMARY = "#4CAF50"
    SECONDARY = "#2196F3"
    WHITE = "#FFFFFF"
    TEXT_SECONDARY = "#666666"


class DashboardPage:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

        def setup_ui(self):
            self.clear_content()

            container = tk.Frame(self.root, bg=Theme.BACKGROUND)
            container.pack(fill=tk.BOTH, expand=True)

            sidebar = tk.Frame(container, bg=Theme.PRIMARY, width=250)
            sidebar.pack(side=tk.LEFT, fill=tk.Y)
            sidebar.pack_propagate(False)

            content = tk.Frame(container, bg=Theme.BACKGROUND)
            content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            self.create_sidebar(sidebar)
            self.create_content(content)

            self.pages = {
                "Dashboard": self.show_dashboard_page,
                "Cases": lambda: CaseListPage(self.root),
                "Calendar": lambda: CalendarPage(self.root),
                "Documents": lambda: ClientDocumentManager(self.root, client_id=None),
                "Clients": lambda: ClientsPage(self.root),
                "Settings": self.show_settings_page,
            }
    def create_sidebar(self, parent):
        tk.Label(
            parent,
            text="LEGAL PRO",
            font=("Arial", 20, "bold"),
            bg=Theme.PRIMARY,
            fg=Theme.WHITE,
        ).pack(pady=30)

        menu_items = [
            ("Dashboard", "📊"),
            ("Cases", "📁"),
            ("Calendar", "📅"),
            ("Documents", "📄"),
            ("Clients", "👥"),
            ("Settings", "⚙️"),
        ]

        for text, icon in menu_items:
            btn = tk.Button(
                parent,
                text=f" {icon} {text}",
                font=("Arial", 12),
                bg=Theme.PRIMARY,
                fg=Theme.WHITE,
                bd=0,
                padx=20,
                pady=15,
                anchor="w",
                cursor="hand2",
                command=lambda t=text: self.handle_menu_click(t),
            )
            btn.pack(fill=tk.X)

    def handle_menu_click(self, menu_item):
        if hasattr(self, 'clear_content'):
            self.clear_content()

        if menu_item in self.pages:
            self.pages[menu_item]()
        else:
            messagebox.showinfo(
                "Navigation", f"Feature for '{menu_item}' not yet implemented!"
            )

    # ... [rest of the methods remain the same]


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x800")
    DashboardPage(root)
    root.mainloop()
