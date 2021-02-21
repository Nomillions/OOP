# Class HW Assignment
# MIS 4322 - MW 1:00 - 2:15
# Noah Miller

class Car:
    def __init__(self, year_model,make,speed):
        self.__year_model = year_model
        self.__make       = make
        self.__speed      = speed

    def accelerate(self,speed_change_accelerate):
        self.__speed += speed_change_accelerate

    def brake(self,speed_change_brake):
        self.__speed -= speed_change_brake

    def get_speed(self):
        return self.__speed


################################################################
#Use the class

import CarClass as cc

def main():
    car_info()


def car_info():
    print("Hello! Please input your vehicle's information below.")
    year_model = input("What is your vehicle's YEAR and MODEL? (Format: 'YYYY, MODEL') ")
    make       = input("What is your vehicle's MAKE? ")
    speed      = 0
    car_info   = cc.Car(year_model,make,speed)
    car_speed_montoring(year_model, make, speed, car_info)
    
def car_speed_montoring(year_model, make, speed, car_info):
    accumulator             = 5
    speed_change_accelerate = 5
    speed_change_brake      = 5
    print("")
    print("Now we will find your vehicle's acceleration!")
    print("---------------------------------------------")
    for increase_change in range(accumulator):
        car_info.accelerate(speed_change_accelerate)
        print("Your ",year_model,make, " is currently traveling ", 
        car_info.get_speed(), " miles per hour!", sep=''
        )
        print()
    print()
    print("Now we will find your vehicle's decceleration!")
    print("---------------------------------------------")
    for decrease_change in range(accumulator):
        car_info.brake(speed_change_brake)
        print("Your ",year_model,make, " is currently traveling ", 
        car_info.get_speed(), " miles per hour!", sep=''
        )
        print()
    


main()