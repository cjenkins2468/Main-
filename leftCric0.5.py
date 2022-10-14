'''
auther miguel dominguez
created 10/11/2022
bugs
when inputs a number higher then the len of the string code breaks
need to change string and num_of char
'''
def leftCirc():
    # user inputs a number and a string
    #arg1 string is the string that will be afcted by the program
    #arg2 fliped_char is the vaible were the final string will be returned
    #arg3 pointer is a number realting to a position in the string
    # program returns the lef most x characrers to the right hand side of the string
    string = "COMPUTER"
    filped_char = ""
    num_of_char = 3
    pointer = 0                                                                 # where the charcher is
    while num_of_char != 0:
        filped_char = filped_char + (string[pointer])                           #add one charcher to fliped_char
        pointer = pointer + 1
        num_of_char = num_of_char - 1
    new_string = string[pointer:len(string)] + filped_char
    return new_string
def main():
    print(leftCirc())

if __name__ == "__main__":
    main()
