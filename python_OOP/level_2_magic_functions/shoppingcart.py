class Shoppingcart:
    def __init__(self, item):
        self.item = item
    
    def __len__(self):
        return len(self.item)
    
    def __repr__(self):
        return (f"Objects:{self.item}")