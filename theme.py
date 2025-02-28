class Theme:
    # Primary colors
    PRIMARY = "#2B3674"
    PRIMARY_HOVER = "#374291"
    SECONDARY = "#4318FF"
    SECONDARY_HOVER = "#5428FF"
    BACKGROUND = "#F4F7FE"
    BACKGROUND_HOVER = "#E9EDF9"
    WHITE = "#FFFFFF"

    # Text colors
    TEXT_PRIMARY = "#1B2559"
    TEXT_SECONDARY = "#A3AED0"

    # Accent colors
    SUCCESS = "#05CD99"
    SUCCESS_HOVER = "#06B588"
    WARNING = "#FFB547"
    WARNING_HOVER = "#FFA522"
    ERROR = "#FF5B5B"
    ERROR_HOVER = "#FF4242"
    INFO = "#4318FF"
    INFO_HOVER = "#3614CC"

    # Font definitions
    HEADING_FONT = ("DM Sans", 24, "bold")
    SUBHEADING_FONT = ("DM Sans", 18, "bold")
    BODY_FONT = ("DM Sans", 14)
    SMALL_FONT = ("DM Sans", 12)

    # Component-specific styles with hover states
    BUTTON_STYLES = {
        "primary": {
            "default": {"bg": PRIMARY, "fg": WHITE,
                        "font": ("DM Sans", 12, "bold")},
            "hover": {
                "bg": PRIMARY_HOVER,
                "fg": WHITE,
                "font": ("DM Sans", 12, "bold"),
            },
        },
        "secondary": {
            "default": {"bg": SECONDARY, "fg": WHITE, "font": ("DM Sans", 12)},
            "hover": {"bg": SECONDARY_HOVER, "fg": WHITE,
                      "font": ("DM Sans", 12)},
        },
    }

    @staticmethod
    def apply_theme(root):
        style = {
            "background": Theme.BACKGROUND,
            "highlightthickness": 0,
            "borderwidth": 0,
        }
        root.configure(**style)

    @staticmethod
    def apply_button_hover(button, style_type="primary"):
        styles = Theme.BUTTON_STYLES[style_type]

        def on_enter(e):
            button.configure(**styles["hover"])

        def on_leave(e):
            button.configure(**styles["default"])

        button.configure(**styles["default"])
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

    @staticmethod
    def apply_input_style(widget):
        default_style = {
            "bg": Theme.WHITE,
            "fg": Theme.TEXT_PRIMARY,
            "font": Theme.BODY_FONT,
            "relief": "flat",
            "highlightthickness": 1,
            "highlightbackground": Theme.TEXT_SECONDARY,
            "highlightcolor": Theme.PRIMARY,
        }

        def on_enter(e):
            widget.configure(highlightbackground=Theme.PRIMARY)

        def on_leave(e):
            widget.configure(highlightbackground=Theme.TEXT_SECONDARY)

        widget.configure(**default_style)
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)
