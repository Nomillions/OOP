import InsectClass as ic #import the .py file

def main():

    my_insect = ic.Insect(4,8,7) # use the class name 

    #print("My insect flew ",my_insect.get_flight(), " miles",sep='')
    #print("My insect has ",my_insect.get_legs(), " legs", sep='')
    #print("My insect has ",my_insect.get_wings(), " wings",sep='')
    print(my_insect.__str__())

main()