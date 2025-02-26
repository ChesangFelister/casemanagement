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
        container = tk.Frame(self.root, bg=Theme.WHITE)
        container.pack(fill=tk.BOTH, expand=True)

        # Left side with branding
        left_frame = tk.Frame(container, bg=Theme.PRIMARY, width=600)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Brand text
        brand_label = tk.Label(
            left_frame,
            text="Nimble Group",
            font=("Arial", 32, "bold"),
            bg=Theme.PRIMARY,
            fg=Theme.WHITE,
        )
        brand_label.pack(pady=50)

        # Right side with login form
        right_frame = tk.Frame(container, bg=Theme.WHITE, padx=60)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.create_login_form(right_frame)

    def create_login_form(self, parent):
        # Welcome text
        tk.Label(
            parent, text="Welcome Back", font=("Arial", 24, "bold"), bg=Theme.WHITE
        ).pack(pady=(100, 20))

        tk.Label(
            parent,
            text="Sign in to continue",
            font=("Arial", 12),
            fg=Theme.TEXT_SECONDARY,
            bg=Theme.WHITE,
        ).pack(pady=(0, 40))

        # Email field
        tk.Label(parent, text="Email", font=("Arial", 11), bg=Theme.WHITE).pack(
            anchor="w"
        )

        self.email_entry = tk.Entry(
            parent, font=("Arial", 12), bg=Theme.BACKGROUND, relief="flat", width=30
        )
        self.email_entry.pack(pady=(5, 20), ipady=8)

        # Password field
        tk.Label(parent, text="Password", font=("Arial", 11), bg=Theme.WHITE).pack(
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

        # Error message label
        self.error_label = tk.Label(
            parent, text="", fg="red", bg=Theme.WHITE, font=("Arial", 10)
        )
        self.error_label.pack(pady=(0, 10))

        # Login button
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
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Check credentials
        if email == "admin@legal.com" and password == "admin123":
            # Clear login page
            for widget in self.root.winfo_children():
                widget.destroy()

            # Create dashboard
            DashboardPage(self.root)
        else:
            self.error_label.config(text="Invalid email or password")


if __name__ == "__main__":
    root = ThemedTk(theme="plastik")  # Initialize ThemedTk with a chosen theme
    app = LoginPage(root)
    root.mainloop()