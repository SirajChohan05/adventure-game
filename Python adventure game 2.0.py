 #python adventure game 2.0 implementing lots of things i know at the moment

print("This is an adventure game")
print("Follow the guidelines")
while True:
    try:
     name = input("What is your name: ")
     print("Welcome", name, "Be careful in this journey")
     break
    except ValueError:
        #print("Invalid input")
     print("This is a journey through the deep misty forest BE CAREFUL!")
while True:
    forest = input("There is a forest ahead do you want to enter? (yes/no): ").lower()
    if forest == "yes":
            print("Good you are brave take the map to know the map of the forest")
            break
               

    elif forest == "no":
                 break
      
    elif forest != "yes" or "no":
                  print("Please pick yes or no")

while True:
     next_1 = input("Would you like to take the sword ahead of you (yes/no)").lower()
     if next_1 == "yes":
             print("Good choice")
             next_2 = input("There is a enemy coming towards do you want to run or defend yourself (strike,run)").lower()
     if next_2 == "strike":
                   print("That is not your level yet")
                   break

     elif next_2 == "run":
                 next_3 = input("Your humbleness is there there is talk of others in the forest do you want to search for them? (yes/no): ")
     if next_3 == "yes":
                     game = input("Do you want to run forward as there is someone in the distance: ")
                     if game == "yes":
                         talk = input("There is someone infront of you do you want to speak to him")
                         if talk == "yes":
                             print("Good you are safe now")
                             break

                         elif talk == "no":
                            print("Fair enough you have escaped")

     elif next_3 == "no":
                     break
        
                     
                     
             


    
                  

        



        

    
        


    


        

    

    
    
