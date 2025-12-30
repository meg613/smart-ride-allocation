from driver import Driver
from rider import rider 
from ride_manager import RideManager 

drivers=[
    Driver(1,2,5),
    Driver(2,5,1),
    Driver(3,3,2)
]

ride_manager=RideManager(drivers)

rider1= rider(101,3,3)
assigned_driver=ride_manager.assign_driver(rider1)

ride_manager.assign_driver(rider1)
if assigned_driver:
    ride_manager.ride_completion(assigned_driver)

rider2=rider(102,3,4)
ride_manager.assign_driver(rider2)