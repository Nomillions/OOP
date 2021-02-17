import random

class Insect: # creates the class

    def __init__(self,l,w,f):
        self.__legs = l #defining the data attributes
        self.__wings = w
        self.__flight = f

    def flight_length(self): # a method that allows the user to call the number of miles the insect flew
        self.__flight = random.randint(1,10)
        return self.__flight

    def __str__(self):
        return (
            "legs: "
            + str(self.__legs) + "\n"
            + "wings: "
            + str(self.__wings) + "\n"
            + "flight: "
            + str(self.__flight) + " miles."
        )
