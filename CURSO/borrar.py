class Point:
      def __init__(self,x,y):
            self.__x=x
            self.__y=y
            
class Rectangle:
  def __init__(self,topLeft:Point,width,height):
        self.__topLeft=topLeft
        self.__width=width
        self.__height=height
  def calculateArea(self):
        return self.__width*self.__height
point=Point(10,20)
rectangle =  Rectangle(point, 30, 40)
area = rectangle.calculateArea()
print("Area del rectángulo: " , area)
      
      