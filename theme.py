class Theme:
    PRIMARY = "#2B3674"
    SECONDARY = "#4318FF"
    BACKGROUND = "#F4F7FE"
    WHITE = "#FFFFFF"
    TEXT_PRIMARY = "#1B2559"
    TEXT_SECONDARY = "#A3AED0"
    
    HEADING_FONT = ("DM Sans", 24, "bold")
    BODY_FONT = ("DM Sans", 14)
    
    @staticmethod
    def apply_theme(root):
        style = {"background": Theme.BACKGROUND}
        root.configure(**style)