import random


class Vehicle:

    def __init__(self):
        self.parked_vehicle = 0

    def vehicle_type(self):
        pass

    def reset(self):
        self.parked_vehicle = 0

    def vehicle_parked(self):
        return f"{self.parked_vehicle} {self.__class__.__name__}s are parked"


class Motorcycle(Vehicle):

    def __init__(self):
        super().__init__()

    def park_vehicle(self):
        ms.park_spot()
        self.parked_vehicle = ms.occupied_spots

    def unpark_vehicle(self):
        ms.unpark_spot()
        self.parked_vehicle = ms.occupied_spots


class Car(Vehicle):

    def __init__(self):
        super().__init__()

    def park_vehicle(self):
        cs.park_spot()
        self.parked_vehicle = cs.occupied_spots

    def unpark_vehicle(self):
        cs.unpark_spot()
        self.parked_vehicle = cs.occupied_spots


class Truck(Vehicle):

    def __init__(self):
        super().__init__()

    def park_vehicle(self):
        ts.park_spot()
        self.parked_vehicle = ts.occupied_spots

    def unpark_vehicle(self):
        ts.unpark_spot()
        self.parked_vehicle = ts.occupied_spots


class ParkingSpot:

    def __init__(self):
        self.available_spots = 0
        self.occupied_spots = 0

    def reset(self):
        self.available_spots = 0
        self.occupied_spots = 0

    def update_available_spots(self):
        self.available_spots += 1

    def park_spot(self):
        if self.available_spots > 0:
            self.available_spots -= 1
            self.occupied_spots += 1
            print(f"\nParked on {self.__class__.__name__}")
        else:
            print(f"\nNo available {self.__class__.__name__}")

    def unpark_spot(self):
        if self.occupied_spots > 0:
            self.available_spots += 1
            self.occupied_spots -= 1
            print(f"\nUnparked vehicle from {self.__class__.__name__}")
        else:
            print(f"\nNo vehicle parked on {self.__class__.__name__}")


class MotorcycleSpot(ParkingSpot):

    def __init__(self):
        super().__init__()
        self.spot_size = 1

    def free_spots(self):
        return f"\n{self.available_spots} motorcycle spots available"


class CarSpot(ParkingSpot):

    def __init__(self):
        super().__init__()
        self.spot_size = 2

    def free_spots(self):
        return f"{self.available_spots} car spots available"


class TruckSpot(ParkingSpot):

    def __init__(self):
        super().__init__()
        self.spot_size = 3

    def free_spots(self):
        return f"{self.available_spots} truck spots available"


ms = MotorcycleSpot()
cs = CarSpot()
ts = TruckSpot()
mc = Motorcycle()
car = Car()
truck = Truck()


def parkinglot_size():
    global combination
    ms.reset()
    cs.reset()
    ts.reset()
    mc.reset()
    car.reset()
    truck.reset()
    target_sum = int(input("Enter parking lot size: "))
    if target_sum:
        combination = random.choice(find_combinations(target_sum=target_sum, numbers=[1, 2, 3]))
        assign_combination()


def find_combinations(numbers, target_sum):
    if target_sum == 0:
        return [[]]
    if target_sum < 0:
        return None
    all_combinations = []
    for i in range(len(numbers)):
        remaining_sum = target_sum - numbers[i]
        remaining_combinations = find_combinations(numbers[i:], remaining_sum)
        if remaining_combinations is not None:
            for combi in remaining_combinations:
                all_combinations.append([numbers[i]] + combi)

    return all_combinations


def assign_combination():
    for i in combination:
        if i == ms.spot_size:
            ms.update_available_spots()
        if i == cs.spot_size:
            cs.update_available_spots()
        if i == ts.spot_size:
            ts.update_available_spots()


parkinglot_size()

while True:
    print("\nWhat would you like to do?")
    print("1. Park a vehicle")
    print("2. Unpark a vehicle")
    print("3. Check available spaces")
    print("4. Check parked vehicles")
    print("5. Reset parking lot")

    choice = input("Enter your choice (1-5 or q to quit): ")

    if choice == "1":
        while True:
            print("\n1. Park a motorcycle")
            print("2. Park a car")
            print("3. Park a truck")
            park_choice = input("Enter your choice (1-3 or q to return): ")
            if park_choice == "1":
                mc.park_vehicle()
            elif park_choice == "2":
                car.park_vehicle()
            elif park_choice == "3":
                truck.park_vehicle()
            elif park_choice == "q":
                break
            else:
                print("Invalid choice. Please try again.")
    elif choice == "2":
        while True:
            print("\n1. Unpark a motorcycle")
            print("2. Unpark a car")
            print("3. Unpark a truck")
            unpark_choice = input("Enter your choice (1-3 or q to return): ")

            if unpark_choice == "1":
                mc.unpark_vehicle()
            elif unpark_choice == "2":
                car.unpark_vehicle()
            elif unpark_choice == "3":
                truck.unpark_vehicle()
            elif unpark_choice == "q":
                break
            else:
                print("\nInvalid choice. Please try again.")

    elif choice == "3":
        print(ms.free_spots())
        print(cs.free_spots())
        print(ts.free_spots())
    elif choice == "4":
        print(mc.vehicle_parked())
        print(car.vehicle_parked())
        print(truck.vehicle_parked())
    elif choice == "5":
        parkinglot_size()
    elif choice == "q":
        break
    else:
        print("\nInvalid choice. Please try again.")
