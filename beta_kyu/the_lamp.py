Define a class called Lamp. It will have attributes for color and state. Both attributes will be strings and pass into constructor as above 
# order. Color will refer to the color of the lamp and state will be the string "on" if the lamp is on and "off" if the lamp is off. 
# You'll need a way to construct a new instance of the class as well as ways to get and set the two attributes it has.

class Lamp:
    def __init__(self,color,state):
        self.color = color
        self.state = state
    
    def getColor(self):
        return self.color
    
    def getState(self):
        return self.state
