import math
from rider import rider

class RideManager:
    def __init__(self,drivers):
        self.drivers=drivers
        self.active_rides={}

    def calculate_distance(self,x1,y1,x2,y2):
        return math.sqrt((x1-x2)**2+(y1-y2)**2)
    
    
    def find_nearest_driver(self, rider):
        nearest_driver = None
        min_distance = float('inf')

        for driver in self.drivers:
            if driver.available:
                distance = self.calculate_distance(
                    driver.x, driver.y,
                    rider.x, rider.y
                )

                if distance < min_distance:
                    min_distance = distance
                    nearest_driver = driver

        return nearest_driver, min_distance
    
    def calculate_surge(self):
        available_drivers=sum(1 for d in self.drivers if d.available)
        active_requests=len(self.active_rides)

        if available_drivers==0:
            return 2.0
        
        ratio=active_requests/available_drivers

        if ratio>2:
            return 2.0
        elif ratio>1:
            return 1.5
        else:
            return 1.0
        
        
    def cancel_rides(self,rider_id):
        if rider_id not in self.active_rides:
            print("No active rides found to cancel.")
            return 
        
        ride=self.active_rides(rider_id)
        driver=rider["driver"]

        driver.available=True
        ride["status"]="CANCELLED"

        print("Ride cancelled by Rider{rider_id}, Driver {driver.driver_id} is now available")
    
        del self.active_rides[rider_id]

    def assign_driver(self,rider):
        driver,distance=self.find_nearest_driver(rider)

        if driver is None:
            print("No drivers available at the moment.")
            return None
        
        driver.available=False
        eta=distance*2 #2 minutes per unit distance

        surge_multiplier=self.calculate_surge()
        fare=distance* 10* surge_multiplier 

        self.active_rides[rider.rider_id]={
            "driver":driver,
            "distance":distance,
            "status": "ASSIGNED",
            "fare":fare
        }

        print(f"Driver {driver.driver_id} assigned to Rider {rider.rider_id}")
        print(f"Distance: {distance:.2f} units")
        print(f"Surge Multiplier: x{surge_multiplier}")
        print(f"Estimated Fare: Rs.{fare:.2f}")
        print(f"Estimated Time of Arrival(ETA): {eta:.2f} minutes")

        return driver 

        # .2 = exactly 2 digits after decimal
        # f= floating-point number 


    def ride_completion(self,rider_id):
        if rider_id not in self.active_rides:
            print("No active ride found.")
            return
        
        ride=self.active_rides[rider_id]
        driver=ride["driver"]

        driver.available=True 
        ride["status"]="COMPLETED"

        print(f"Ride completed for Rider {rider_id}. Fare: Rs.{ride['fare']:.2f}")

        del self.active_rides[rider_id]


