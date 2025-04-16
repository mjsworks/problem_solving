# make sure that we always receive a list
class Shopcartmod:
    def __init__(self, item):
        if isinstance(item, list):
            self.item = item
        else:
            self.item = [item]
    
    def __repr__(self):
        return(f"Always a list and it is {self.item}")
    
    def __len__(self):
        return len(self.item)