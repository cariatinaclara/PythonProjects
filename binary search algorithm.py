# Create a function that takes a list and a target parameter
def binary_search(list, element):
    # Initalizing parameters
    Middle = 0
    Start = 0
    # The parameter End gets the length of the input list
    End = len(list) 
    Steps = 0
   
   # The While Loop checks if the element provided by the user is less, greater or equal to the middle element of the list
   # If the element is equal to the to element in the middle of the list it returns that element and the element is found
   # If it is not equal to the middle element the while loop will split the list to make the pool of choice is halved
   # If the element is less than the middle of the list then the list will start from Start and end at Middle - 1
   # If the element is greater than the middle then the list will start with Middle + 1 and end with End
    
    while(Start<=End):
        print("Step",Steps, ":", str(list[Start:End + 1]))

        Steps = Steps + 1
        Middle = (Start + End) // 2

        if element == list[Middle]:
            return Middle
        if element < list[Middle]:
            End = Middle - 1

        else:
            Start = Middle + 1

    return -1
            
my_list = [1, 2 , 3, 4, 5, 6, 7, 8, 9]
Target = 9

# Invoking the function
binary_search(my_list, Target)  