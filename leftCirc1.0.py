'''
auther miguel dominguez
created 10/11/2022
version 1.1
updated 10/14/2022
bugs:
'''
def main():
    string = "COMPUTER"
    num_of_char =9
    print(leftCirc(string,num_of_char))

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

if __name__ == "__main__":
    main()
