import csv

class Dealership:
    def __init__(self, salesmen=None, total_sales=None, capacity=None):
        self.salesmen = salesmen
        self.total_sales = total_sales
        self.capacity = capacity
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)



class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price


class NewCar(Car):
    def __init__(self, make, model, year, price):
        super().__init__(make, model, year, price)

class UsedCar(Car):
    def __init__(self, make, model, year, price, mileage):
        super().__init__(make, model, year, price)
        self.mileage = mileage

def load_cars(filename):
    dealership = Dealership()
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            car_details = row['Model'].split(' ', 2)
            make = car_details[1]
            model = car_details[2]
            car_price = row['Price'].split('$', 1)
            price = car_price[1] if len(car_price) > 1 else car_price[0]
            price = price.replace(',', '')
            car_mileage = row['Mileage'].split(' ', 1)
            mileage = car_mileage[0]
            if row['Status'] == 'New':
                car = NewCar(make, model, int(row['Year']), int(price.replace(',', '_')))
            else:
                car = UsedCar(make, model, int(row['Year']), int(price.replace(',', '_')), int(mileage.replace(',', '_')))
            dealership.add_car(car)
    return dealership

dealership = load_cars('python/practice/projects/car_data.csv')




def list_all_cars(dealership):
    for car in dealership.cars:
        print(car.make, car.model, car.year, car.price)

list_all_cars(dealership)
# class Car:
#     def __init__(self, make, model, year, status, mileage, price):
#         pass