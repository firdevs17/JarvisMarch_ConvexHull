#!/usr/bin/env python
# coding: utf-8

# In[12]:


import matplotlib.pyplot as plt
import random
import time

jarvis_time=time.time()
#point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class ConvexHull(object):
    points = []
    hull = []

    def __init__(self):
         pass


    def add(self, point):
        self.points.append(point)

    def orientation(self, origin, p1, p2):
     
        difference = (
            ((p2.x - origin.x) * (p1.y - origin.y))
            - ((p1.x - origin.x) * (p2.y - origin.y))
        )

        return difference

    def leftmost(self):
        
        points = self.points
    
        #Initial Point :
        start = points[0]
        min_x = start.x
        
        #all points analyze
        for p in points[1:]:
            if p.x < min_x:
                min_x = p.x
                start = p

        point = start
        self.hull.append(start)

        f_point = None
        
        while f_point is not start:

            
            p1 = None
            
            for p in points:
                if p is point:
                    continue
                else:
                    p1 = p
                    break

            f_point = p1

            for p2 in points:
                if p2 is point or p2 is p1:
                    continue
                else:
                    direction = self.orientation(point, f_point, p2)
                    if direction > 0:
                        f_point = p2

            self.hull.append(f_point)
            point = f_point



    def hull_points(self):
        if self.points and not self.hull:
            self.leftmost()

        return self.hull


    def display(self):
        
        # all points
        x = [p.x for p in self.points]
        y = [p.y for p in self.points]
        plt.plot(x, y,color ='r', marker='+', linestyle=':')

        # hull points
        hx = [p.x for p in self.hull]
        hy = [p.y for p in self.hull]
        plt.plot(hx, hy,'b',linestyle='-')

        plt.title('Convex Hull')
        plt.show()
        
def main():  
    conv = ConvexHull()
    for i in range(50):
        conv.add(Point(random.randint(-50, 50), random.randint(-50, 50)))

    print("Points on hull:", conv.hull_points())


    conv.display()



if __name__ == '__main__':  
    main()

print("jarvis time:",jarvis_time)


# In[ ]:




