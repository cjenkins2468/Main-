'''
Created on Oct 24, 2022

@author: NSokol25
'''

def mC(word, s,l,x,d):
    s = int(s)
    l = int(l)
    x = int(x)
    substring = word[s-1:s+l-1]
    if d == 'L' or d == 'l':
        moving = substring[:x]
        notmoving = substring[x:]
        newsubstring = notmoving + moving
        output = word.replace(substring,newsubstring)
        return output
    if d == 'R' or d == 'r':
        moving = substring[l- x:]
        notmoving = substring[:l-x:]
        newsubstring = moving + notmoving
        output = word.replace(substring,newsubstring)
        return output
    
def main():
    word = input('what word would would you like to use: ')
    s = int(input('where would you like to start your substring: '))
    l = int(input('how long would you like your substring to be: '))
    x = int(input('how many characters would you like to move: '))
    d = input('which direction would you like to move from (R) or (L)')
    output = mC(word, s, l,x,d)
    print(output)
main()