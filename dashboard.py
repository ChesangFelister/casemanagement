import tkinter as tk
from tkinter import messagebox
from case_list import CaseListPage
from calendar_page import CalendarPage
from client_management import ClientManagementPage
from client_documents import ClientDocumentManager
from theme import Theme


class DashboardPage:
    def __init__(self, root):
        self.root = root

        # ✅ Define content frame before calling clear_content()
        self.container = tk.Frame(self.root, bg=Theme.BACKGROUND)
        self.container.pack(fill=tk.BOTH, expand=True)

        self.sidebar = tk.Frame(self.container, bg=Theme.PRIMARY, width=250)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar.pack_propagate(False)

        # ✅ Ensure self.content exists before calling clear_content()
        self.content = tk.Frame(self.container, bg=Theme.BACKGROUND)
        self.content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.create_sidebar(self.sidebar)
        self.show_dashboard_page()  # Show dashboard by default

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
        """Handles switching between different pages."""
        self.clear_content()

        if menu_item == "Dashboard":
            self.show_dashboard_page()
        elif menu_item == "Cases":
            CaseListPage(self.content)
        elif menu_item == "Calendar":
            CalendarPage(self.content)
        elif menu_item == "Documents":
            ClientDocumentManager(self.content, client_id=None)
        elif menu_item == "Clients":
            ClientManagementPage(self.content)
        elif menu_item == "Settings":
            self.show_settings_page()
        else:
            messagebox.showinfo(
                "Navigation", f"Feature for '{menu_item}' not yet implemented!"
            )

    def clear_content(self):
        """Clears the current content area before loading a new page."""
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_dashboard_page(self):
        """Displays the dashboard welcome page."""
        tk.Label(
            self.content,
            text="Welcome to the Dashboard",
            font=("Arial", 24, "bold"),
            bg=Theme.BACKGROUND,
            fg=Theme.TEXT_SECONDARY,
        ).pack(pady=20)

        tk.Label(
            self.content,
            text="This is the main dashboard page.",
            font=("Arial", 14),
            bg=Theme.BACKGROUND,
            fg=Theme.TEXT_SECONDARY,
        ).pack(pady=10)

    def show_settings_page(self):
        """Displays the settings page."""
        tk.Label(
            self.content,
            text="Settings",
            font=("Arial", 24, "bold"),
            bg=Theme.BACKGROUND,
            fg=Theme.TEXT_SECONDARY,
        ).pack(pady=20)

        tk.Label(
            self.content,
            text="This is the settings page.",
            font=("Arial", 14),
            bg=Theme.BACKGROUND,
            fg=Theme.TEXT_SECONDARY,
        ).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x800")
    root.title("Legal Pro - Dashboard")
    DashboardPage(root)
    root.mainloop()
