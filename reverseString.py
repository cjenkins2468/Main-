'''
Created on Oct 10, 2022

@author: KHarashima25
'''

def main():
    word = 'COMPUTER' # Input must be string
    para = '33' # Parameters must be string, only 2 digits, second one cannot be a 0
    result = revString(word,para) # call function with input and parameters
    print(result) # print result
    
def revString(word,para):
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
    
    while counter < len(word):                  # before the end of the word
        letter = word[counter]
        notrev = notrev + letter                # add irrelevant letters to not reversed (norev)
        counter = counter + 1
        if counter == startpoint:               # once reached starting point
            while lencount < gofor:             # if the length is smaller than distance
                letter = word[counter]
                result = letter + result        # Add letter
                lencount = lencount + 1         # add a count to the amount travelled from start point
                counter = counter + 1           # add a count to the amount travelled from start of word
    counter = 0
    stringrand = ''                             # set stringrand (just a string variable)
    while counter < len(notrev):                # before end of norev (spare letters, the ones that are not modified)        
        letter = word[counter]          
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
if __name__ == '__main__':
    main()