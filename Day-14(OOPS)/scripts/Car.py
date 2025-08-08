# 5. Encapsulate attributes in a Car class and allow controlled access using getter/setter methods.

class Car:
    
    def __init__(self,brand,year,speed):
        self.__brand = brand
        self.__year  = year
        self.__speed = speed
        
    def get_brand(self):
        return self.__brand
    
    def set_brand(self,new_val):
        self.__brand = new_val
        return self.__brand
    
    def get_year(self):
        return self.__year
    
    def set_year(self,new_val):
        self.__year = new_val
        return self.__year
    
    def get_speed(self):
        return self.__speed
    
    def set_speed(self,new_val):
        self.__speed = new_val
        return self.__speed
    
    def accelerate(self,acceleration_val):
        new_speed = self.get_speed() + acceleration_val
        if new_speed > 200:
            return 'Not Possible'
        else:
            self.set_speed(new_speed)
            
    def decelerate(self,deceleration_val):
        new_speed = self.get_speed() - deceleration_val
        if new_speed < 0:
            return 'Not Possible'
        else:
            self.set_speed(new_speed)