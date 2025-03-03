import tkinter as tk
from theme import Theme


class CaseTracker:
    def __init__(self):
        self.cases = {}
        self.hearings = {}
        self.documents = {}

    def create_case_dashboard(self, parent):
        dashboard = tk.Frame(parent, bg=Theme.WHITE)
        dashboard.pack(fill=tk.BOTH, expand=True)

        # Timeline view
        timeline = tk.Canvas(dashboard, bg=Theme.WHITE, height=200)
        timeline.pack(fill=tk.X)

        # Case statistics
        stats = tk.Frame(dashboard, bg=Theme.WHITE)
        stats.pack(fill=tk.X, pady=20)

        metrics = [
            ("Total Hearings", "42"),
            ("Documents Filed", "15"),
            ("Pending Ations", "3"),
            ("Days to Next Hearing", "7"),
        ]

        for label, value in metrics:
            stat_card = tk.Frame(stats, bg=Theme.PRIMARY, padx=20, pady=15)
            stat_card.pack(side=tk.LEFT, padx=10)

            tk.Label(
                stat_card,
                text=value,
                font=("Arial", 24, "bold"),
                fg=Theme.WHITE,
                bg=Theme.PRIMARY,
            ).pack()
            tk.Label(stat_card, text=label, fg=Theme.WHITE,
                     bg=Theme.PRIMARY).pack()
