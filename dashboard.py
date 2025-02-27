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

        # Main container
        container = tk.Frame(self.root, bg=Theme.BACKGROUND)
        container.pack(fill=tk.BOTH, expand=True)

        # Sidebar
        sidebar = tk.Frame(container, bg=Theme.PRIMARY, width=250)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        sidebar.pack_propagate(False)

        # Main content
        content = tk.Frame(container, bg=Theme.BACKGROUND)
        content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.create_sidebar(sidebar)
        self.create_content(content)

        # Initialize page placeholders
        self.pages = {
            "Dashboard": self.show_dashboard_page,
            "Documents": self.open_document_file,
            "Settings": self.open_settings_file,
        }

    def create_sidebar(self, parent):
        # Logo
        tk.Label(
            parent,
            text="LEGAL PRO",
            font=("Arial", 20, "bold"),
            bg=Theme.PRIMARY,
            fg=Theme.WHITE,
        ).pack(pady=30)

        # Menu items with icons
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

    def create_content(self, parent):
        # Header with welcome message and quick actions
        header = tk.Frame(parent, bg=Theme.WHITE)
        header.pack(fill=tk.X, padx=20, pady=20)

        tk.Label(
            header,
            text="Welcome back, Admin",
            font=("Arial", 24, "bold"),
            bg=Theme.WHITE,
        ).pack(side=tk.LEFT)

        # Quick action buttons
        actions_frame = tk.Frame(header, bg=Theme.WHITE)
        actions_frame.pack(side=tk.RIGHT)

        self.create_action_button(actions_frame, "Add Case", "➕")
        self.create_action_button(actions_frame, "New Client", "👤")
        self.create_action_button(actions_frame, "Schedule", "📅")

        # Statistics cards
        self.create_stats_section(parent)

        # Recent activities
        self.create_recent_activities(parent)

    def create_action_button(self, parent, text, icon):
        tk.Button(
            parent,
            text=f"{icon} {text}",
            font=("Arial", 11),
            bg=Theme.SECONDARY,
            fg=Theme.WHITE,
            padx=15,
            pady=8,
            relief="flat",
            cursor="hand2",
        ).pack(side=tk.LEFT, padx=5)

    def create_stats_section(self, parent):
        stats_frame = tk.Frame(parent, bg=Theme.BACKGROUND)
        stats_frame.pack(fill=tk.X, padx=20, pady=20)

        stats = [
            ("Total Cases", "125", "📊"),
            ("Active Cases", "42", "⚡"),
            ("Pending", "15", "⏳"),
            ("Completed", "68", "✅"),
        ]

        for title, value, icon in stats:
            card = tk.Frame(stats_frame, bg=Theme.WHITE, padx=20, pady=15)
            card.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

            tk.Label(
                card, text=f"{icon} {title}", font=("Arial", 12), bg=Theme.WHITE
            ).pack(anchor="w")

            tk.Label(card, text=value, font=("Arial", 24, "bold"), bg=Theme.WHITE).pack(
                anchor="w", pady=10
            )

    def create_recent_activities(self, parent):
        activities_frame = tk.Frame(parent, bg=Theme.WHITE, padx=20, pady=20)
        activities_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(
            activities_frame,
            text="Recent Activities",
            font=("Arial", 16, "bold"),
            bg=Theme.WHITE,
        ).pack(anchor="w", pady=(0, 20))

        # Sample activities
        activities = [
            ("New case added", "Criminal Law", "2 hours ago"),
            ("Court hearing scheduled", "Civil Case #123", "Yesterday"),
            ("Document uploaded", "Property Agreement", "2 days ago"),
        ]

        for title, desc, time in activities:
            self.create_activity_item(activities_frame, title, desc, time)

    def create_activity_item(self, parent, title, desc, time):
        item = tk.Frame(parent, bg=Theme.WHITE, pady=10)
        item.pack(fill=tk.X)

        tk.Label(item, text=title, font=("Arial", 12, "bold"), bg=Theme.WHITE).pack(
            anchor="w"
        )

        tk.Label(
            item, text=desc, font=("Arial", 11), bg=Theme.WHITE, fg=Theme.TEXT_SECONDARY
        ).pack(anchor="w")

        tk.Label(
            item, text=time, font=("Arial", 10), bg=Theme.WHITE, fg=Theme.TEXT_SECONDARY
        ).pack(anchor="w")

    def handle_menu_click(self, menu_item):
        print(f"Clicked on {menu_item}")

        # Clear existing content
        self.clear_content()

        # Load the relevant page
        if menu_item == "Cases":
            AddCasePage(self.root)
        elif menu_item == "case_list":
            CaseListPage(self.root)
        elif menu_item == "Calendar":
            CalendarPage(self.root)
        elif menu_item == "Documents":
            ClientDocumentManager(self.root, client_id=None)
        elif menu_item == "Clients":
            ClientsPage(self.root)
        elif menu_item in self.pages:
            self.pages[menu_item]()
        else:
            messagebox.showinfo(
                "Navigation", f"Feature for '{menu_item}' not yet implemented!"
            )

    def clear_content(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.destroy()

    def show_dashboard_page(self):
        print("Showing Dashboard Page")

    def open_document_file(self):
        print("Opening Document File")

    def open_settings_file(self):
        print("Opening Settings File")


# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x800")
    DashboardPage(root)
    root.mainloop()