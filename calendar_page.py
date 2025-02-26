import tkinter as tk
try:
    from tkcalendar import Calendar
except ImportError:
    print("tkcalendar module not found. Please install it using 'pip install tkcalendar'")
    Calendar = None
from datetime import datetime


class CalendarPage:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        # Split view layout
        self.container = tk.Frame(self.parent, bg=Theme.WHITE)
        self.container.pack(fill=tk.BOTH, expand=True)

        # Left side - Calendar
        self.calendar_frame = tk.Frame(self.container, bg=Theme.WHITE)
        self.calendar_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Right side - Events list
        self.events_frame = tk.Frame(self.container, bg=Theme.BACKGROUND)
        self.events_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.create_calendar_widget()
        self.create_events_list()

    def create_calendar_widget(self):
        cal = Calendar(
            self.calendar_frame,
            selectmode="day",
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day,
            background=self.Theme.PRIMARY,
            foreground=self.Theme.WHITE,
            selectbackground=self.Theme.SECONDARY,
        )
        cal.pack(pady=20, padx=20)
