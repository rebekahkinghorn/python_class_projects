# Name: Rebekah Kinghorn
# Friend Tracker: 
    #this will allow you to input friends and their hobbies
    #search for friends, etc

# set up the dictionary, initialize response, and type up the menu
friendDict = {}
response = None
menu = "Menu:\n1. Add a Friend\n2. Find a Friend's Hobby\n3. Quit"

# this is the start of the while loop. it goes while repsonse is not 3


# if they didn't enter "3" then continue the loop
while response != "3":
    print(menu)
    response = input("Enter an option (1, 2, or 3):")

    # if response is not 1 2 or 3 then it's invalid
    if not response =="1" and not response =="2" and not response =="3":
        print("Invalid choice. Please choose a valid option.")
        continue

    #if it is 1 2 or 3 then we'll convert it to an int
    numResponse = int(response)

    #if response is 1, prompt them to enter the name to add them
    if numResponse == 1:
        friendName = str(input("Enter friend's name:"))
        #if the name exists, print message
        if friendName in friendDict:
            print(f"{friendName} is already in your dictionary.")
        #if the name is not in dict already, take the hobby and put in a new key/value
        else:
            friendHobby = str(input(f"Enter {friendName}'s hobby:"))
            friendDict[friendName] = friendHobby
            print(f"{friendName} added to your dictionary!")
    
    #if response is 2, prompt them to enter the name to find the hobby
    if numResponse == 2:
        nameFind = input("Enter a friend's name to find their hobby:")
        #if the name is in the dict, print the hobby
        if nameFind in friendDict:
            print(f"{nameFind}'s hobby is {friendDict[nameFind]}.")
        #if the name is not in the dict, print message
        else:
            print(f"{nameFind} is not in the dictionary.")
    
    #if response is 3, print message and exit loop
    if numResponse == 3:
        print("Exiting the program. Goodbye!")
        break


#print(friendDict)
