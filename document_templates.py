class DocumentTemplateSystem:
    def __init__(self):
        self.templates = {
            'Legal Notice': self.create_legal_notice,
            'Court Petition': self.create_petition,
            'Agreement': self.create_agreement,
            'Affidavit': self.create_affidavit
        }
        
    def create_template_selector(self, parent):
        selector_frame = tk.Frame(parent, bg=Theme.WHITE)
        selector_frame.pack(fill=tk.X, pady=20)
        
        for template_name in self.templates.keys():
            template_card = tk.Frame(selector_frame, bg=Theme.WHITE, padx=15, pady=15)
            template_card.pack(side=tk.LEFT, padx=10)
            
            tk.Label(template_card, text=template_name, bg=Theme.WHITE, font=Theme.BODY_FONT).pack()
            tk.Button(
                template_card,
                text="Use Template",
                command=lambda t=template_name: self.use_template(t)
            ).pack(pady=10)
