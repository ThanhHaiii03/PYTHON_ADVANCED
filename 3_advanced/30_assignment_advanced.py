# ADVANCED **************************************************************************
# content = assignment (Python Advanced)
#
# deliver = Upload the files to your git repository
#           and share it in the assignment submission form.
#
# date    = 2025-03-18
# email   = contact@alexanderrichtertd.com
#*******************************************************************************
"""

Advanced Python is about a higher and more structural level of Python.
Learning new functions, constructs and a better way of collaboration.



#*******************************************************************************
# 31. CUBE CLASS
#*******************************************************************************
Create a cube class in cube.py
"""
# 1 2 3 4

class Cube:

   def __init__(self,name):
      self.name = name
      self.translate = (0,0,0)
      self.rotate = (0,0,0)
      self.scale  = (1,1,1)
      self.color  = (1,1,1)
   
   def translate_cube(self,x,y,z):
      self.translate = (x,y,z)
      print(f"Cube translated to: {self.translate}")
      
   def rotate_cube(self,x,y,z):
      self.rotate = (x,y,z)
      print(f"Cube rotated to: {self.rotate}")
      
   def scale_cube(self,x,y,z):
      self.scale = (x,y,z)
      print(f"Cube scaled to: {self.scale}")
      
   def color_cube(self,r,g,b):
      self.color= (r,g,b)
      print(f"Cube colored to: {self.color}")
      
   def print_status(self):
       print(f"""{self.name}
             Translate: {self.translate}
             Rotate:    {self.rotate}
             Scale:     {self.scale}
             Color:     {self.color}""")
   
   def update_transform(self, ttype, value):
       update = {"translate": self.translate,
                 "rotate": self.rotate,
                 "scale" : self.scale,
                 "color" : self.color }
       
cube1 = Cube(name='Cube_001')
cube2 = Cube(name='Cube_002')
cube3 = Cube(name='Cube_003')



# 5

class Object:
   
   def __init__(self,name):
      self.name = name
      self.translate = (0,0,0)
      self.rotate = (0,0,0)
      self.scale  = (1,1,1)

   
   def translate_cube(self,x,y,z):
      self.translate = (x,y,z)
      print(f"Cube translated to: {self.translate}")
      
   def rotate_cube(self,x,y,z):
      self.rotate = (x,y,z)
      print(f"Cube rotated to: {self.rotate}")
      
   def scale_cube(self,x,y,z):
      self.scale = (x,y,z)
      print(f"Cube scaled to: {self.scale}")
      
      

       
       
class Cube(Object):
   
   def __init__(self,name):
      super().__init__(name)
      self.color  = (1,1,1)
      
   def translate_cube(self,x,y,z):
      super().translate_cube(x,y,z)
      
   def rotate_cube(self,x,y,z):
      super().rotate_cube(x,y,z)

   def scale_cube(self,x,y,z):
      super().scale_cube(x,y,z)

   def color_cube(self,r,g,b):
      self.color= (r,g,b)
      print(f"Cube colored to: {self.color}")
      
   def print_status(self):
       print(f"""{self.name}
             Translate: {self.translate}
             Rotate:    {self.rotate}
             Scale:     {self.scale}
             Color:     {self.color}""")
       
       




"""
#*******************************************************************************
# 32. DECORATOR
#*******************************************************************************
   a) Create a decorator in decorator.py

   b) Include a decorator into your own application.
"""
import time


#*********************************************************************
# DECORATOR
def print_process(func):
    def wrapper(*args, **kwargs):
        
        print(f'START {func.__name__}')
        start = time.time()

        result = func(*args, **kwargs)                  # main_function
        end = time.time()
        print(f'END - Processing time: {end - start:.2f} seconds')
        
        return result
    return wrapper


#*********************************************************************
# FUNC
@print_process
def short_sleeping(name):
    time.sleep(.1)
    print(name)

@print_process
def mid_sleeping():
    time.sleep(2)

@print_process
def long_sleeping():
    time.sleep(4)

short_sleeping("so sleepy")

mid_sleeping()
long_sleeping()



"""
#*******************************************************************************
# 31_assignment_app.py
#*******************************************************************************
"""
