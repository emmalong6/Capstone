#Basic Computer Architecture Calculations
# based off code from geeksforgeeks.org - mits
import random

def showMenu():
    print("Choose which method of practice for calculating frequency you would like:")
    print("1 Show Example/Instructions")
    print("2 Enter Own Data")
    print("3 Test Your Knowledge")
    print("4 Exit the Program")

def exampleInstructions():
    print('''The result of adding an n-bit number to its one's complement is always an n-bit number
with ones in every position. If we add 1 to that result, our new value is an n-bit number with zeros
in every position and an overflow or carry to the next highest position, the (n+1)th column which corresponding
to 2n. For our 8-bit example above, the result of adding 100101102 to 011010012 is 111111112. Adding 1 to
this number gives us 000000002 with an overflow carry of 1 to the ninth or 28 column. If we restrict
ourselves to 8 bits, this overflow carry can be ignored.

This gives us a method for coming up with the additive complement called the 2's complement representation.
The 2's complement of a value is found by first taking the 1's complement, then incrementing that result
by 1. For example, in the previous section, we determined that the 1's complement of 100101112 is 011010002.
If we add 1 to this value, we get:
                                        0 1 1 0 1 0 0 0
                                    +               1
                                    -------------------
                                        0 1 1 0 1 0 0 1

Therefore, the 2's complement of 100101112 is 011010012. Let's see what happens when we try to add the value to its 2's complement.
                                      1 1 1 1 1 1 1 1
                                        1 0 0 1 0 1 1 1
                                      + 0 1 1 0 1 0 0 1
                                      -------------------
                                        0 0 0 0 0 0 0 0

The result is zero! Okay, so most of you caught the fact that I didn't drop down the last carry which would've
made the result 1000000002. This is not a problem, because in the case of signed arithmetic, the carry has
a purpose other than that of adding an additional digit representing the next power of two. As long as we
make sure that the two numbers being added have the same number of bits, and that we keep the result to that
same number of bits too, then any carry that goes beyond that should be discarded.

Actually, discarded is not quite the right term. In some cases we will use the carry as an indication of a
possible mathematical error. It should not, however, be included in the result of the addition. This is simply
the first of many "anomalies" that must be watched when working with a limited number of bits.

Two more examples of 2's complements are shown below:
                                Original value (1010)   0 0 0 0 1 0 1 0
                                1's complement          1 1 1 1 0 1 0 1
                                2's complement (-1010)  1 1 1 1 0 1 1 0

                                Original value (8810)   0 1 0 1 1 0 0 0
                                1's complement          1 0 1 0 0 1 1 1
                                2's complement (-8810)  1 0 1 0 1 0 0 0

Now let's see if the 2's complement representation stands up in the face of addition. If 8810 = 010110002 
and -1010 = 111101102, then the addition of these two numbers should equal 7810 = 010011102.
                                          1 1 1 1
                                            0 1 0 1 1 0 0 0
                                          + 1 1 1 1 0 1 1 0
                                          -------------------
                                            0 1 0 0 1 1 1 0

There is also a "short-cut" to calculating the 2's complement of a binary number. This trick can be used if you
find the previous way too cumbersome or if you'd like a second method in order to verify the result you got from
using the first.
1. The trick works by copying the zero bit values starting with the least significant bit until
   you reach your first binary 1. Copy that 1 too. If the least significant bit is a one, then only copy that bit.
2. Next, invert all of the remaining bits. 
                                           For 10101000:
                                        1 0 1 0     1 0 0 0 
                                        | | | |     | | | |
                                        0 1 0 1     1 0 0 0
                                        STEP 2      STEP 1

This result matches the result for the previous example. In decimal, the negative of 5 is -5. If we take the negative a second
time, we return to the original value, e.g., the negative of -5 is 5. Is the same true for taking the 2's complement of a 2's
complement of a binary number? Well, let's see. The binary value for 4510 is 001011012. Watch what happens when we take the 2's complement twice.
                                Original value = 45         0 0 1 0 1 1 0 1
                                1's complement of 45        1 1 0 1 0 0 1 0
                                2's complement of 45 = -45  1 1 0 1 0 0 1 1
                                1's complement of -45       0 0 1 0 1 1 0 0
                                2's complement of -45 = 45  0 0 1 0 1 1 0 1

It worked! The second time the 2's complement was taken, the pattern of ones and zeros returned to their original values. It turns out
that this is true for any binary number of a fixed number of bits.

(From: Computer Organization and Design Fundamentals by David Tarnoff)\n''')

def enterOwnData():
    def run():
        while True:
            try:
                #2's complement
                def toBinary():    
                    # Size of an integer is assumed to be 8 bits 
                    # Function that convert Decimal to binary 
                    while True:  
                            n = int(input("Please enter a number: ")) 
                            if (n < 257):
                                binary = ""
                                for i in range(7, -1, -1):  
                                    k = n >> i
                                    if (k & 1): 
                                        binary += "1"
                                    else: 
                                        binary += "0"
                                return binary
                            else:
                                print("Please unter a number from 0 to 256 inclusive")
                                continue

                # Print 2's complement of binary number 
                def printTwosComplement(b):
                    n = len(b)  
                    flipping = "" 
                    twos = ""
                    # Returns '0' for '1' and '1' for '0'  
                    def flip(c): 
                        return '1' if (c == '0') else '0'

                    # This for loop here flips every number.
                    for i in range(n): 
                        flipping += flip(b[i])  
                    # The second step to 2s complement is to increment our binary string by 1.        
                    flipping = list(flipping.strip("")) 
                    twos = list(flipping) 
                    # Count down from the end of the list to the beginning
                    for i in range(n - 1, -1, -1): 
                        # Flipping all 1s to zeroes.
                        if (flipping[i] == '1'):
                            twos[i] = '0'   
                        # but if we reach a zero, we flip it to a 1 and then exit the loop
                        else:          
                            twos[i] = '1'
                            break
                
                    i -= 1    #subtracts and reassigns
                    # If No break : all are 1 as in 111 or 11111 in such case, add extra 1 at beginning  
                    if (i == -1): 
                        twos.insert(0, '1')  

                    twos_string = ""
                    for car in twos:
                        twos_string += car
                            
                    #print("2's complement: " + twos_string)
                    return twos_string
                        
                binary_num = toBinary()
                result = printTwosComplement(binary_num)
                print("2's complement is ",result,"\n")
                break
            except ValueError:
                print("Not a valid input, try again.")
    run()

    def anotherMenu():
        print("Would you like to try again or exit to main menu?")
        print("1 Go again!")
        print("2 Main menu please.")

    while True:
        anotherMenu()
        choice = input("What is your choice? ")
        if choice == '1':
            run()
        elif choice == '2':
            print("The program has ended.\n")
            break
        else:
            print("Invalid response")

def testKnowledge():
    def run():
        while True:
            try:
                randomNum = random.randrange(1, 170, 1)
                #2's complement
                def toBinary():    
                    # Size of an integer is assumed to be 8 bits 
                    # Function that convert Decimal to binary   
                    n = randomNum 
                    binary = ""
                    for i in range(7, -1, -1):  
                        k = n >> i
                        if (k & 1): 
                            binary += "1"
                        else: 
                            binary += "0"
                    return binary 

                # Print 2's complement of binary number 
                def printTwosComplement(b):
                    n = len(b)  
                    flipping = "" 
                    twos = "" 
                    # Returns '0' for '1' and '1' for '0'  
                    def flip(c): 
                        return '1' if (c == '0') else '0'

                    # This for loop here flips every number.
                    for i in range(n): 
                        flipping += flip(b[i])  
                    # The second step to 2s complement is to increment our binary string by 1.        
                    flipping = list(flipping.strip("")) 
                    twos = list(flipping) 
                    # Count down from the end of the list to the beginning
                    for i in range(n - 1, -1, -1): 
                        # Flipping all 1s to zeroes.
                        if (flipping[i] == '1'):
                            twos[i] = '0'   
                        # but if we reach a zero, we flip it to a 1 and then exit the loop
                        else:          
                            twos[i] = '1'
                            break

                    i -= 1    #subtracts and reassigns
                    # If No break : all are 1 as in 111 or 11111 in such case, add extra 1 at beginning  
                    if (i == -1): 
                        twos.insert(0, '1')  

                    twos_string = ""
                    for char in twos:
                        twos_string += char
                            
                    #print("2's complement: " + twos_string)
                    return twos_string
                        
                binary_num = toBinary()
                result = printTwosComplement(binary_num)

                print("What is 2's complement for: ",randomNum)
                while True:
                    try:
                        #print(result)
                        answer = input("What is your answer? ")
                        if result == answer:
                                print("Correct!\n")
                                break
                        else:
                            print("Try again")
                    except:
                        continue
                break
            except ValueError:
                print("Not valid input")
    run()

    def anotherMenu():
        print("Would you like to try again or exit to main menu?")
        print("1 Go again!")
        print("2 Main menu please.")

    while True:
        anotherMenu()
        choice = input("What is your choice? ")
        if choice == '1':
            run()
        elif choice == '2':
            print("The program has ended.\n")
            break
        else:
            print("Invalid response\n")

while True:
    showMenu()
    choice = input("What is your choice?\n")
    if choice == '1':
        exampleInstructions()
    elif choice == '2':
        enterOwnData()
    elif choice == '3':
        testKnowledge()
    elif choice == '4':
        print("The program has ended.\n")
        break
    else:
        print("Invalid response\n")

