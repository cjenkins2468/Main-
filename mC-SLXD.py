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
