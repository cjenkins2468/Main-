




from turtle import right
'''
Created on Oct 10, 2022
@author: NSokol25
'''


def leftShift(word, moveleft):
    '''
        Shifts a word x characters to the left
    
    Args:
    
        word - the word you would like to shift left - str
    
        moveleft - how many characters to move left - int
    
    Returns:
    
        output: your word shifted to the left - str
    
    '''
    output = word[moveleft:]
    maxcounter = len(word) - len(output) 
    while maxcounter > 0:
        output = output + '#'
        maxcounter -= 1
       
    return output

'''
Created on Oct 24, 2022
Last edited 10/28/22
@author: Noah Sokol
'''
'''
    Creates a substring then moves certain letters inside that substring
#Arg:
 
    word - the word that is being changed
    s - starting position of substring
    l - length of substring
    x - how many characters are being moved from D
    d - which direction the characters come from
    
#returns:
    output - the word with the parameters acted on
'''
def mC(word, s,l,x,d):
    s = int(s)
    l = int(l)
    x = int(x)
    substring = word[s-1:s+l-1]                             #Creates the substring
    if d == 'L' or d == 'l':
        moving = substring[:x]                              #which characters are moving
        notmoving = substring[x:]
        newsubstring = notmoving + moving
        output = word.replace(substring,newsubstring)       #gets the output
        return output
    if d == 'R' or d == 'r':
        moving = substring[l- x:]                           #moving is gotten by substring how many characters 
        notmoving = substring[:l-x:]                        # are being moved starting from the length of the substring
        newsubstring = moving + notmoving
        output = word.replace(substring,newsubstring)
        return output

'''
Created on Oct 14, 2022
submitted: 10/13/22
@author: NSokol25
'''


def rightShift(word, moveright):
    '''
    
    
    shifts a word x characters right and replaces empties with #s to return word to original length
    Arg:
    
        word - word shifted right
        
        moveright - how many characters to move right
        
    Return:
    
        output: your word shifted right
    '''
    empties=''
    maxcounter = len(word) - moveright
    if maxcounter > 0:
        new_word = word[:maxcounter]
        counter = len(word) - len(new_word)
    else: 
        new_word = ''
        counter = len(word)
    while counter > 0:
        empties = empties + '#'
        counter -= 1
    output = empties + new_word 
    return output

'''
auther miguel dominguez
created 10/11/2022
version 1.1
updated 10/14/2022
bugs:
'''


def leftCirc(string,num_of_char):
    # user inputs a number and a string
    #arg1 string is the string that will be afcted by the program
    #arg2 fliped_char is the vaible were the final string will be returned
    #arg3 pointer is a number realting to a position in the string
    # program returns the lef most x characrers to the right hand side of the string
    new_string=string
    pointer = 0  # where the charcher is
    while num_of_char != 0:
        if pointer==8:
            pointer=1
        new_string = new_string+new_string[0] 
        new_string= new_string[1:len(new_string)]
        pointer = pointer + 1
        num_of_char = num_of_char - 1
    return new_string


'''
auther miguel dominguez
created 10/14/2022
version 1.0
updated 10/14/2022
bugs:
'''

def rightCirc(string,num_of_char):
    # user inputs a number and a string
    #arg1 new string is were the final output will go
    #arg2 pointer is a number realting to a position in the string
    # program returns the right most x characrers to the left hand side of the string
    new_string=string
    pointer = 0                                                          #where the charcher is
    while num_of_char != 0:
        if pointer==8:
            pointer=1                                                    #resets charter if pointer goes over 7
        new_string = new_string[len(string)-1]+new_string                #takes last charecter and moves it to the frount of the string
        new_string= new_string[0:len(new_string)-1]                      #removes the last charecter in the string
        pointer = pointer + 1
        num_of_char = num_of_char - 1
    return new_string


def revString(string,para):
    result = ''                                 # define result
    notrev = ''                                 # define what is not-reversed (notrev)
    counter = 0                                 # define counter for all loops
    lencount = 0                                # define specific length count
    while True:                                 # loop to split starting point and travelling distance
        if counter == 0:                        # if at first digit, then define as starting point
            startpoint = para[counter]
        elif counter == 1:                      # if at second digit, then define as distance to go for
            gofor = para[counter]
        else:                                   # break when done
            break
        counter = counter + 1

    startpoint = int(startpoint)                # convert to integers
    gofor = int(gofor)            
    counter = 0                                 # reset counter
    
    while counter < len(string):                  # before the end of the word
        letter = string[counter]
        notrev = notrev + letter                # add irrelevant letters to not reversed (norev)
        counter = counter + 1
        if counter == startpoint:               # once reached starting point
            while lencount < gofor:             # if the length is smaller than distance
                letter = string[counter]
                result = letter + result        # Add letter
                lencount = lencount + 1         # add a count to the amount travelled from start point
                counter = counter + 1           # add a count to the amount travelled from start of word
    counter = 0
    stringrand = ''                             # set stringrand (just a string variable)
    while counter < len(notrev):                # before end of norev (spare letters, the ones that are not modified)        
        letter = string[counter]          
        stringrand = stringrand + letter        # add letters before the reversed clip to stringrand
        counter = counter + 1
        if counter >= len(notrev):              # if done, then break
            break
        elif counter == startpoint:             # once reach starting point
            result = stringrand + result        # add stringrand before the reversed clip
            stringrand = '' 
        if counter >= startpoint and counter < len(notrev):     # once after the starting point, add remaining letters to the end of the reversed clip
            letter = notrev[counter]
            result = result + letter           
    return(result)


 
def main():  #defining the main
    run = True 

    while run == True: #making a run = True loop

        counter = 0                                                  # variable that creates/ helps the while loop below 
        operations = input("")                             #starting the main by asking their input
        operations = operations.split("/")                           #spliting varible "operations" into sections
        data = operations[len(operations) -1]                        #defining those sections
        while counter < len(operations)-1:                           #making a while loop
            action_number = operations[counter].split("-")           #spliting the zones into two zone inside each zone
            
            if action_number[0] == 'LS':                             #making it call this function if the "..." is the same 
                data = str(data)                                     #making the variables into strings or intergers 
                repeat = int(action_number[1])                       #making the variables into strings or intergers 
                data = leftShift(data,repeat)                        # calling this function

            elif action_number[0] == 'RS':                           #making it call this function if the "..." is the same 
                data = str(data)                                     #making the variables into strings or intergers 
                repeat = int(action_number[1])                       #making the variables into strings or intergers 
                data = rightShift(data,repeat)                       # calling this function

            elif action_number[0] == 'LC':                           #making it call this function if the "..." is the same 
                data = str(data)                                     #making the variables into strings or intergers 
                repeat = int(action_number[1])                       #making the variables into strings or intergers 
                data = leftCirc(data,repeat)                         # calling this function

            elif action_number[0] == 'RC':                           #making it call this function if the "..." is the same 
                data = str(data)                                     #making the variables into strings or intergers 
                repeat = int(action_number[1])                       #making the variables into strings or intergers 
                data = rightCirc(data,repeat)                        # calling this function
            
            elif action_number[0] == 'REV':                          #making it call this function if the "..." is the same 
                repeat = int(action_number[1])                       #making the variables into strings or intergers 
                if (repeat >= 1 and repeat < 10) or (repeat >= 11 and repeat < 20) or (repeat >= 21 and repeat < 30) or (repeat >= 31 and repeat < 40) or (repeat >= 41 and repeat < 50) or (repeat >= 51 and repeat < 60) or (repeat >= 61 and repeat < 70) or (repeat >= 71 and repeat < 80) or (repeat >= 81 and repeat < 90) or (repeat >= 91 and repeat < 100): # making sure that they plugged in the right number
                    REV = ('true')
                    repeat = str(repeat)                             #making the variables into strings or intergers 
                    data = str(data) #making the variables into strings or intergers 
                    data = revString(data,repeat)# calling this function
                if REV != ('true'): # anti BRAKE method
                    print("cannot do that number of reverse") 
                    run = False #ending main if this happens

            elif action_number[0] == 'MC':#making it call this function if the "..." is the same 
                MC_DATA = list(action_number[1]) #making a list so I can split it up
                S = int(MC_DATA[0]) #making the variables into strings or intergers 
                L = int(MC_DATA[1]) #making the variables into strings or intergers 
                X = int(MC_DATA[2]) #making the variables into strings or intergers 
                D = str(MC_DATA[3]) #making the variables into strings or intergers 
                data = str(data) #making the variables into strings or intergers 
                data = mC(data,S,L,X,D)# calling this function
            else:
                print("wrong")
            counter+=1
        print(data) # final print
        
if __name__ == '__main__': # ending main loop
    main()