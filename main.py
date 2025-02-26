import tkinter as tk
from theme import Theme
from login import LoginPage


def main():
    root = tk.Tk()
    root.title("Legal Case Management System")
    root.geometry("1200x800")
    root.resizable(True, True)

    Theme.apply_theme(root)
    LoginPage(root)
    root.mainloop()


if __name__ == "__main__":
    main()
