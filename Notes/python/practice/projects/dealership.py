class Vehicle:
    def __init__(self, name, speed, mileage, capacity):
        self.speed = speed
        self.mileage = mileage
        self.name = name
        self.capacity = capacity


class Bus(Vehicle):
    def seating(self):
        return f'the seating capacity of {self.name} is {self.capacity}'


tesla = Vehicle("tesla", 200, 50_000, 5)
school_bus = Bus("school bus", 180, 12, 50)
print(f"Vehicle name: {school_bus.name} speed: {school_bus.speed} Mileage: {school_bus.mileage}")
print(tesla.speed, tesla.mileage)

print(school_bus.seating())