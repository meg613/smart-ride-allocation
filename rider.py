class rider:
    def __init__ (self,rider_id,x,y):
        self.rider_id=rider_id
        self.x=x
        self.y=y
    def __str__(self):
        return f"Rider {self.rider_id} at ({self.x},{self.y})"