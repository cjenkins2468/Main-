'''
auther miguel dominguez
created 10/14/2022
version 1.0
updated 10/14/2022
bugs:
'''
def main():
    string = "COMPUTER"
    num_of_char =11
    print(leftCirc(string,num_of_char))

def leftCirc(string,num_of_char):
    # user inputs a number and a string
    #arg1 new string is were the final output will go
    #arg2 pointer is a number realting to a position in the string
    # program returns the right most x characrers to the left hand side of the string
    new_string=string
    pointer = 0                                                          #where the charcher is
    while num_of_char != 0:
        if pointer==8:
            pointer=1                                                    #resets charter if pointer goes over 7
        new_string = new_string[len(string)-1]+new_string
        new_string= new_string[0:len(new_string)-1]
        pointer = pointer + 1
        num_of_char = num_of_char - 1
    return new_string

if __name__ == "__main__":
    main()