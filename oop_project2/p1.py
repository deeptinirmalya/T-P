class Vehicle:
    def __init__(self, number):
        self.number = number


class ParkingLot:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.available_spots = total_spots
        self.vehicles = {}

    def entry(self, vehicle_number, entry_time):
        if self.available_spots == 0:
            print("Parking Full")
            return
        v = Vehicle(vehicle_number)
        self.vehicles[vehicle_number] = entry_time
        self.available_spots -= 1
        print("Vehicle Parked")

    def exit(self, vehicle_number, exit_time):
        if vehicle_number not in self.vehicles:
            print("Vehicle Not Found")
            return
        entry_time = self.vehicles[vehicle_number]
        hours = exit_time - entry_time
        fee = hours * 20
        del self.vehicles[vehicle_number]
        self.available_spots += 1
        print("Parking Fee:", fee)

    def show_spots(self):
        print("Available Spots:", self.available_spots)


p = ParkingLot(5)

p.entry("OD01A1234", 2)
p.entry("OD02B5678", 3)

p.show_spots()

p.exit("OD01A1234", 6)

p.show_spots()