# ADVANCED ***************************************************************************
# content = assignment
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************

"""
CUBE CLASS

1. CREATE an abstract class "Cube" with the functions:
   translate(x, y, z), rotate(x, y, z), scale(x, y, z) and color(R, G, B)
   All functions store and print out the data in the cube (translate, rotate, scale and color).

2. ADD an __init__(name) and create 3 cube objects.

3. ADD the function print_status() which prints all the variables nicely formatted.

4. ADD the function update_transform(ttype, value).
   "ttype" can be "translate", "rotate" and "scale" while "value" is a list of 3 floats.
   This function should trigger either the translate, rotate or scale function.

   BONUS: Can you do it without using ifs?

5. CREATE a parent class "Object" which has a name, translate, rotate and scale.
   Use Object as the parent for your Cube class.
   Update the Cube class to not repeat the content of Object.

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
       
       