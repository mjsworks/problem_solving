class Eshopcart:
    def __init__(self, item):
        if isinstance(item, list):
            self.item = item
        else:
            self.item = [item]
        
    def __str__(self):
        return (f"the items passed is a list. It looks like -> {self.item}")
    
    def __repr__(self):
        return (f"list -> {self.item}")
    
    def __len__(self):
        return len(self.item)
    
    def __getitem__(self, index):
        return self.item[index]