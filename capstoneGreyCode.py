#Basic Computer Architecture Calculations
# based off code from geeksforgeeks.org - mits, combined with code from codespeedy.com
import random

def showMenu():
    print("Choose which method of practice for calculating gray code you would like:")
    print("1 Show Example/Instructions")
    print("2 Enter Own Data")
    print("3 Test Your Knowledge")
    print("4 Exit the Program")

def exampleInstructions():
    print('''The use of binary counting sequences is common in digital applications. For
example, an n-bit binary value can be used to identify the position of a rotating shaft as 
being within one of 2n different arcs.

As the shaft turns, a sensor can detect which of the shaft's arcs it is aligned with by
reading a digital value and associating it with a specific arc. By remembering the previous
position and timing the changes between positions, a processor can also compute speed and direction.

One type of shaft position sensor uses a disk mounted to the shaft with slots cut into the
disk at different radii representing different bits. Light sources are placed on one side
of the disk while sensors on the other side of the disk detect when a hole is present, i.e.,
the sensor is receiving light.

In its current position, the slots in the disk are lined up between the second and third
light sensors, but not the first. This means that the sensor will read a value of 110 indicating
the shaft is in position number 1102 = 6.

There is a potential problem with this method of encoding. It is possible to read the sensor 
at the instant when more than one gap is opening or closing between its light source and sensor.
When this happens, some of the bit changes may be detected while others are not.

If this happens, an erroneous measurement may occur. For example, if the shaft turns clockwise toward
position 1012 = 5, but at the instant when the sensor is read, only the first bit change is detected,
then the value read will be 1112 = 7 indicating counter-clockwise rotation.

To solve this problem, alternate counting sequences referred to as the Gray code are used. These
sequences have only one bit change between values. For example, the values assigned to the arcs of the
above shaft could follow the sequence 000, 001, 011, 010, 110, 111, 101, 100. This sequence is not
correct numerically, but as the shaft turns, only one bit will change as the shaft turns from one
position to the next.

There is an algorithm to convert an n-bit unsigned binary value to its corresponding n-bit Gray code.
Begin by adding a 0 to the most significant end of the unsigned binary value. There should now be n
boundaries between the n+1 bits. For each boundary, write a 0 if the adjacent bits are the same and a 1
if the adjacent bits are different. The resulting value is the corresponding n-bit Gray code value.
                                1 0 0 0 1 1
Add 0 to the left most side:    0 1 0 0 0 1 1
Adjacent bits that are
different generate a 1.         1 1 0 0 1 0
Adjacent bits that are
the same generate a 0.

Using this method, the Gray code for any binary value can be determined. Table 2-3 presents the
full Gray code sequence for four bits. The shaded bits in third column are bits that are different
then the bit immediately to their left. These are the bits that will become ones in the Gray code
sequence while the bits not shaded are the ones that will be zeros. Notice that exactly one bit changes
in the Gray code from one row to the next and from the bottom row to the top row.

Table 2-3 Derivation of the Four-Bit Gray Code
Decimal     Binary      Binaryw/starting zero   Gray Code
0           0 0 0 0     0 0 0 0 0               0 0 0 0
1           0 0 0 1     0 0 0 0 1               0 0 0 1
2           0 0 1 0     0 0 0 1 0               0 0 1 1
3           0 0 1 1     0 0 0 1 1               0 0 1 0
4           0 1 0 0     0 0 1 0 0               0 1 1 0
5           0 1 0 1     0 0 1 0 1               0 1 1 1
6           0 1 1 0     0 0 1 1 0               0 1 0 1
7           0 1 1 1     0 0 1 1 1               0 1 0 0
8           1 0 0 0     0 1 0 0 0               1 1 0 0
9           1 0 0 1     0 1 0 0 1               1 1 0 1
10          1 0 1 0     0 1 0 1 0               1 1 1 1
11          1 0 1 1     0 1 0 1 1               1 1 1 0
12          1 1 0 0     0 1 1 0 0               1 0 1 0
13          1 1 0 1     0 1 1 0 1               1 0 1 1
14          1 1 1 0     0 1 1 1 0               1 0 0 1
15          1 1 1 1     0 1 1 1 1               1 0 0 0

(From: Computer Organization and Design Fundamentals by David Tarnoff)\n''')

def enterOwnData():
    while True:
        try:
            #Grey Code
            def toBinary():    
                n = int(input("Please enter a number: ")) 
                binary = ""
                for i in range(64, -1, -1):  
                    k = n >> i
                    if (k & 1): 
                        binary += "1"
                    else: 
                        binary += "0"
                return binary

            def convert_gray(binary):
                binary = int(binary, 2)
                binary ^= (binary >> 1)
                return bin(binary)[2:]

            binary_num = toBinary()
            gray_code = convert_gray(binary_num)
            print("Grey Code is: ",gray_code, "\n")

            def anotherMenu():
                print("Would you like to go again or exit to main menu?")
                print("1 Go again!")
                print("2 Main menu please.")

            while True:
                anotherMenu()
                choice = int(input("What is your choice? "))
                if choice == 1:
                    enterOwnData()
                elif choice == 2:
                    print("The program has ended.\n")
                    break
                else:
                    print("Invalid response")
            break
        except ValueError:
            print("No valid integer! Please try again ...")

def testKnowledge():
    def run():
        randomNum = random.randrange(1, 256, 1)

        def toBinary():    
            n = randomNum 
            binary = ""
            for i in range(64, -1, -1):  
                k = n >> i
                if (k & 1): 
                    binary += "1"
                else: 
                    binary += "0"
            return binary

        def convert_gray(binary):
            binary = int(binary, 2)
            binary ^= (binary >> 1)
            return bin(binary)[2:]

        def pad_gray_string(s):
            return s.zfill(8)

        binary_num = toBinary()
        gray_code = convert_gray(binary_num)
        stringLength = pad_gray_string(gray_code)
        print("What is the gray code for: ",randomNum)
        print("Grey Code is: ",stringLength)
        while True:
            try:
                answer = input("What is your answer in 8 bit length? ")
                if stringLength == answer:
                        print("Correct!\n")
                        break
                else:
                    print("Try again")
            except:
                continue
    run()

    def anotherMenu():
        print("Would you like to try again or exit to main menu?")
        print("1 Go again!")
        print("2 Main menu please.")

    while True:
        anotherMenu()
        choice = int(input("What is your choice? "))
        if choice == 1:
            run()
        elif choice == 2:
            print("The program has ended.\n")
            break
        else:
            print("Invalid response")

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
        print("The program has ended.")
        break
    else:
        print("Invalid response\n")