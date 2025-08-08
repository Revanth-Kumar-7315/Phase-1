# 3. Write a TemperatureConverter class that converts Celsius to Fahrenheit and vice versa.

class TemperatureConverter:
    
    def __init__(self,temp):
        self.temp = temp
        
    def c_to_f(self):
        return (self.temp*(9/5)) + 32
    
    def f_to_c(self):
        return (self.temp - 32)*(5/9)