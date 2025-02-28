import tkinter as tk
from datetime import datetime
from theme import Theme
try:
    from tkcalendar import Calendar  # type: ignore
except ImportError:
    print("tkcalendar module not found. Please install it using 'pip install tkcalendar'")
    Calendar = None
class CalendarPage:

    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()              

    def setup_ui(self):
        # Main container
        self.container = tk.Frame(self.parent, bg=Theme.WHITE)
        self.container.pack(fill=tk.BOTH, expand=True)

        # Left side - Calendar
        self.calendar_frame = tk.Frame(self.container, bg=Theme.WHITE)
        self.calendar_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Right side - Events list
        self.events_frame = tk.Frame(self.container, bg=Theme.BACKGROUND)
        self.events_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create widgets
        self.create_calendar_widget()
        self.create_events_list()

    def create_calendar_widget(self):
        if Calendar:
            current_date = datetime.now()
            cal = Calendar(
                self.calendar_frame,
                selectmode="day",
                year=current_date.year,
                month=current_date.month,
                day=current_date.day,
                background=Theme.PRIMARY,
                foreground=Theme.WHITE,
                selectbackground=Theme.SECONDARY,
            )
            cal.pack(pady=20, padx=20)
    def create_events_list(self):
        # Events list header
        header = tk.Frame(self.events_frame, bg=Theme.WHITE)
        header.pack(fill=tk.X, padx=20, pady=20)

        tk.Label(
            header, text="Upcoming Events", font=("Arial", 16, "bold"), bg=Theme.WHITE
        ).pack(side=tk.LEFT)

        # Add event button
        tk.Button(
            header,
            text="+ Add Event",
            bg=Theme.PRIMARY,
            fg=Theme.WHITE,
            font=("Arial", 11),
            padx=15,
            pady=5,
            relief="flat",
            cursor="hand2",
        ).pack(side=tk.RIGHT)

        # Events list container
        events_list = tk.Frame(self.events_frame, bg=Theme.WHITE)
        events_list.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x800")
    CalendarPage(root)
    root.mainloop()