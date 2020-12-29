class Background:
    def __init__(self, col, p):
        self.panel = p
        self.col = col
    
    def update(self):
        self.panel.setBackground(self.col)
        
