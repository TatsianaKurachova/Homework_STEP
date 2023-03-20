class Car:
   
   def __init__(self, color, type, year):
    self.color = color
    self.type = type
    self.year = year

   def start(self):
    print ("Start car")

   def mute(self):
    print ("Mute car")
       
   def year_of_release(self):
    print("Year of release:", self.year) 
             
   def set_the_type(self):
    print("Set the type:", self.type)

   def set_the_color(self):
    print("Set the color:", self.color)

car_1 = Car('red', 'Truck', 2022)
car_2 = Car('green', 'Cupe', 2000)
car_1.start()
car_1.mute()
car_1.year_of_release()
car_1.set_the_color()
car_1.set_the_type()

car_2.start()
car_2.mute()
car_2.year_of_release()
car_2.set_the_color()
car_2.set_the_type()