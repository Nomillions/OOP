import CoinClass as c


# The main function.
def main():
       # Create an object from the Coin class.
       my_coin = c.Coin()
       your_coin = c.Coin()   # this creates an instance called 'my_coin' of the class 'Coin()'
       # this is instance 1 for the Coin class

       # Display the side of the coin that is facing up.
      # print('This side is up:', my_coin.get_sideup())    # notice you do not have to supply the argument/parameter

       # Toss the coin.
       #print('I am going to toss the coin ten times:')
       #for count in range(10):
        #   my_coin.toss()
           
           # Display the side of the coin that is facing up.
         #  print('This side is up:', my_coin.get_sideup())
       show_coin_status(my_coin)
       flip(my_coin)
       show_coin_status(my_coin)

       show_coin_status(your_coin)
       flip(your_coin)
       show_coin_status(your_coin)
           

def show_coin_status(coin_obj):
    print("this side of the coin is up: ",coin_obj.get_sideup())

def flip(coin_obj):
    coin_obj.toss()



       

# Call the main function.

main()
