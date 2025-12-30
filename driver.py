class Driver:
    def __init__(self,driver_id,x,y):
        self.driver_id=driver_id
        self.x=x
        self.y=y
        self.available=True

    def __str__(self):
        status="Available" if self.available else "Busy"
        return f"Driver {self.driver_id} ({status}) at ({self.x},self.y)"
    

