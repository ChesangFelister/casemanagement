import tkinter as tk
from tkinter import ttk
from theme import Theme
from dashboard import DashboardPage


class LoginPage:
    def __init__(self, root):
        self.root = root
        self.email_entry = None
        self.password_entry = None
        self.error_label = None
        self.setup_ui()

    def setup_ui(self):
        """Creates the login UI."""
        self.root.title("Login - Nimble Group")
        self.root.geometry("900x600")

        container = tk.Frame(self.root, bg=Theme.WHITE)
        container.pack(fill=tk.BOTH, expand=True)

        left_frame = tk.Frame(container, bg=Theme.PRIMARY, width=400)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        brand_label = tk.Label(
            left_frame,
            text="Nimble Group",
            font=("Arial", 32, "bold"),
            bg=Theme.PRIMARY,
            fg=Theme.WHITE,
        )
        brand_label.pack(pady=50)

        # Right Section (Login Form)
        right_frame = tk.Frame(container, bg=Theme.WHITE, padx=60)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.create_login_form(right_frame)

    def create_login_form(self, parent):
        """Creates the login form elements."""
        tk.Label(
            parent, text="Welcome Back", font=("Arial", 24, "bold"),
            bg=Theme.WHITE
        ).pack(pady=(100, 20))

        tk.Label(
            parent,
            text="Sign in to continue",
            font=("Arial", 12),
            fg=Theme.TEXT_SECONDARY,
            bg=Theme.WHITE,
        ).pack(pady=(0, 40))

        tk.Label(parent, text="Email", font=("Arial", 11),
                 bg=Theme.WHITE).pack(
            anchor="w"
        )

        self.email_entry = tk.Entry(
            parent, font=("Arial", 12),
            bg=Theme.BACKGROUND, relief="flat", width=30
        )
        self.email_entry.pack(pady=(5, 20), ipady=8)

        tk.Label(parent, text="Password", font=("Arial", 11),
                 bg=Theme.WHITE).pack(
            anchor="w"
        )

        self.password_entry = tk.Entry(
            parent,
            font=("Arial", 12),
            bg=Theme.BACKGROUND,
            relief="flat",
            width=30,
            show="•",
        )
        self.password_entry.pack(pady=(5, 20), ipady=8)

        self.error_label = tk.Label(
            parent, text="", fg="red", bg=Theme.WHITE, font=("Arial", 10)
        )
        self.error_label.pack(pady=(0, 10))

        tk.Button(
            parent,
            text="Sign In",
            bg=Theme.SECONDARY,
            fg=Theme.WHITE,
            font=("Arial", 12, "bold"),
            padx=40,
            pady=10,
            relief="flat",
            cursor="hand2",
            command=self.handle_login,
        ).pack(pady=30)

    def handle_login(self):
        """Validates login credentials and redirects to the dashboard."""
        email = self.email_entry.get()
        password = self.password_entry.get()

        if email == "admin@legal.com" and password == "admin123":
            self.redirect_to_dashboard()
        else:
            self.error_label.config(text="Invalid email or password")

    def redirect_to_dashboard(self):
        """Destroys the login UI and initializes the dashboard."""
        for widget in self.root.winfo_children():
            widget.destroy()
        DashboardPage(self.root)


from ttkthemes import ThemedTk

if __name__ == "__main__":
    root = ThemedTk(theme="plastik")  
    app = LoginPage(root)
    root.mainloop()
