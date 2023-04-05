import random


class Vehicle:
    parked_vehicle = 0

    def __init__(self):
        pass

    def vehicle_type(self):
        pass

    @classmethod
    def reset(cls):
        cls.parked_vehicle = 0

    @classmethod
    def __str__(cls):
        return f"{cls.parked_vehicle} {cls.__name__}s are parked"


class Motorcycle(Vehicle):
    parked_vehicle = 0

    def __init__(self):
        super().__init__()

    def vehicle_type(self):
        return "Motorcycle"

    @classmethod
    def park_vehicle(cls):
        MotorcycleSpot()
        MotorcycleSpot.park_spot()
        cls.parked_vehicle = MotorcycleSpot.occupied_spots

    @classmethod
    def unpark_vehicle(cls):
        MotorcycleSpot.unpark_spot()
        cls.parked_vehicle = MotorcycleSpot.occupied_spots


class Car(Vehicle):
    parked_vehicle = 0

    def __init__(self):
        super().__init__()

    def vehicle_type(self):
        return "Car"

    @classmethod
    def park_vehicle(cls):
        CarSpot()
        CarSpot.park_spot()
        cls.parked_vehicle = CarSpot.occupied_spots

    @classmethod
    def unpark_vehicle(cls):
        CarSpot.unpark_spot()
        cls.parked_vehicle = CarSpot.occupied_spots


class Truck(Vehicle):
    parked_vehicle = 0

    def __init__(self):
        super().__init__()

    def vehicle_type(self):
        return "Truck"

    @classmethod
    def park_vehicle(cls):
        TruckSpot()
        TruckSpot.park_spot()
        cls.parked_vehicle = TruckSpot.occupied_spots

    @classmethod
    def unpark_vehicle(cls):
        TruckSpot.unpark_spot()
        cls.parked_vehicle = TruckSpot.occupied_spots


class ParkingSpot:
    available_spots = 0
    occupied_spots = 0

    @classmethod
    def reset(cls):
        cls.available_spots = 0
        cls.occupied_spots = 0
        Motorcycle.reset()
        Car.reset()
        Truck.reset()

    @classmethod
    def update_available_spots(cls):
        cls.available_spots += 1

    @classmethod
    def park_spot(cls):
        if cls.available_spots > 0:
            cls.available_spots -= 1
            cls.occupied_spots += 1
            print(f"Parked on {cls.__name__}")
        else:
            print(f"No available {cls.__name__}")

    @classmethod
    def unpark_spot(cls):
        if cls.occupied_spots > 0:
            cls.available_spots += 1
            cls.occupied_spots -= 1
            print(f"Unparked vehicle from {cls.__name__}")
        else:
            print(f"No vehicle parked on {cls.__name__}")


class MotorcycleSpot(ParkingSpot):
    available_spots = 0
    occupied_spots = 0

    def __init__(self):
        super().__init__()
        self.spot_size = 1

    def __str__(self):
        return f"{self.available_spots} motorcycle spots available"


class CarSpot(ParkingSpot):
    available_spots = 0
    occupied_spots = 0

    def __init__(self):
        super().__init__()
        self.spot_size = 2

    def __str__(self):
        return f"{self.available_spots} car spots available"


class TruckSpot(ParkingSpot):
    available_spots = 0
    occupied_spots = 0

    def __init__(self):
        super().__init__()
        self.spot_size = 3

    def __str__(self):
        return f"{self.available_spots} truck spots available"


def parkinglot_size():
    global combination
    MotorcycleSpot.reset()
    CarSpot.reset()
    TruckSpot.reset()
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
    cs = CarSpot()
    ms = MotorcycleSpot()
    ts = TruckSpot()

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
                Motorcycle()
                Motorcycle.park_vehicle()
            elif park_choice == "2":
                Car()
                Car.park_vehicle()
            elif park_choice == "3":
                Truck()
                Truck.park_vehicle()
            elif park_choice == "q":
                break
            else:
                print("Invalid choice. Please try again.")
    elif choice == "2":
        while True:
            print("1. Unpark a motorcycle")
            print("2. Unpark a car")
            print("3. Unpark a truck")
            unpark_choice = input("Enter your choice (1-3 or q to return): ")

            if unpark_choice == "1":
                Motorcycle.unpark_vehicle()
            elif unpark_choice == "2":
                Car.unpark_vehicle()
            elif unpark_choice == "3":
                Truck.unpark_vehicle()
            elif unpark_choice == "q":
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == "3":
        print(MotorcycleSpot())
        print(CarSpot())
        print(TruckSpot())
    elif choice == "4":
        print(Motorcycle())
        print(Car())
        print(Truck())
    elif choice == "5":
        parkinglot_size()
    elif choice == "q":
        break
    else:
        print("Invalid choice. Please try again.")
