class Point:
    
    def __init__(self,x,y):
        self.x_cod = x
        self.y_cod = y
        
    def __str__(self):
        return f'({self.x_cod},{self.y_cod})'
    
    def euclidean_distance(self,other):
        return ((self.x_cod-other.x_cod)**2 + (self.y_cod-other.y_cod)**2)**0.5
    
    def distance_from_origin(self):
        return ((self.x_cod)**2 + (self.y_cod)**2)**0.5
        #return self.euclidean_distance(Point(0,0))
        

class Line:
    
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
        
    def __str__(self):
        return f'{self.A}x + {self.B}y + {self.C} = 0'
    
    def point_on_line(line,point):
        if (line.A*point.x_cod) + (line.B*point.y_cod) + line.C == 0:
            return f'Point {point} lies on Line {line}'
        else:
            return f'Point {point} does not lie on Line {line}'
    
    def shortest_distance(line,point):
        return abs(line.A*point.x_cod + line.B*point.y_cod + line.C)/((line.A)**2 + (line.B)**2)**0.5
    
    def intersection_checker(self, other):
        D = self.A * other.B - self.B * other.A
        if D != 0:
            return f'Lines {self} and {other} intersect at a single point.'
        else:
            # Optional: check if lines are coincident
            ratio_A = self.A / other.A if other.A != 0 else None
            ratio_B = self.B / other.B if other.B != 0 else None
            ratio_C = self.C / other.C if other.C != 0 else None

            if ratio_A == ratio_B == ratio_C:
                return f'Lines {self} and {other} are coincident.'
            else:
                return f'Lines {self} and {other} are parallel (do not intersect).'