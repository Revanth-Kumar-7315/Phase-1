# 4. Write a class Point in 2D space with methods to calculate distance from origin and from another point.

class Point:
    
    def __init__(self,x,y):
        self.x_cod = x
        self.y_cod = y
        
    def __str__(self):
        return f'{(self.x_cod,self.y_cod)}'
    
    def distance_between_points(self,other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    
    def distance_from_origin(self):
        return ((self.x_cod)**2 + (self.y_cod)**2)**0.5