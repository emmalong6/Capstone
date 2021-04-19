#Basic Computer Architecture Calculations
import random
from random import randint
import math
#Frequency

def showMenu():
    print('''Choose which method of practice for calculating frequency you would like,
please enter the number associate with your choice:''')
    print("1 Show Example/Instructions")
    print("2 Enter Own Data")
    print("3 Test Your Knowledge")
    print("4 Exit the Program")

def exampleInstructions():
    print('''\nFrequency is the representation of the rate of the pulses in a periodic pulse train.
It is the inverse measurement of the frequency.
                            1
        Frequency = -----------------
                    Period in seconds\n
For example: ''')
    pulse = random.randrange(10,100,10)
    pause = random.randrange(10,100,10)
    print("If you have a pulse of ",pulse," and a pause of ",pause,"\n")
    period = pulse + pause
    dutyCycle = (pulse / period) * 100 #needs to be percentage
    print("The duty cycle measures to: "+ str(round(dutyCycle, 2)) + "%")
    print('''The duty cycle is the last measurement of a periodic waveform.
It represents the percentage of time that a periodic signal is a logic '1'.
                        pulse
        Duty Cycle = ----------- x 100%
                        period\n''')
    freq = 1000 / period #change to measure in Kilo Hz
    f = round(freq,2)
    print("While the frequency in this problem would be ", f,"Hz rounded to two decimal places.\n")
    print("From: Computer Organization and Design Fundamentals by David Tarnoff)\n")

def enterOwnData():

    def measurementsMenu():
        print('''Choose which unit of measurement you would like to view,
please enter the number associate with your choice:''')
        print("1 Milliseconds")
        print("2 Microseconds")
        print("3 Nanoseconds")
        print("4 Exit")

    def milliFreq():
        while True:
            try:
                pulse = int(input("Please enter a pulse: "))
                pause = int(input("Please enter a pause: "))
                period = pulse + pause
                print("The period is: " + str(period))
                dutyCycle = (pulse / period) * 100 #needs to be percentage
                print("The duty cycle is: "+ str(round(dutyCycle, 2)) + "%")
                freq = 1000 / period #measures in Hz
                print("The frequency is: " + str(round(freq, 2)) + "Hz\n")
                break
            except ValueError:
                print("No valid integer! Please try again ...")

        def anotherMenu():
            print("Would you like to go again or choose another unit of measurment?")
            print("1 Go again!")
            print("2 New unit of measurement please.")

        while True:
            anotherMenu()
            choice = input("What is your choice? ")
            if choice == '1':
                milliFreq()
            elif choice == '2':
                #print("The program has ended.\n")
                break
            else:
                print("Invalid response\n")
                
    def microFreq():
        while True:
            try:
                pulse = int(input("Please enter a pulse: "))
                pause = int(input("Please enter a pause: "))
                period = pulse + pause
                print("The period is: " + str(period))
                dutyCycle = (pulse / period) * 100 #needs to be percentage
                print("The duty cycle is: "+ str(round(dutyCycle, 2)) + "%")
                freq = 1000000 / period #change to measure in Kilo Hz
                print("The frequency is: " + str(round(freq, 2)) + "Hz or " + str(round((freq/1000), 2)) + "kHz\n")
                break
            except ValueError:
                print("No valid integer! Please try again ...")
                
        def anotherMenu():
            print("Would you like to go again or choose another unit of measurment?")
            print("1 Go again!")
            print("2 New unit of measurement please.")

        while True:
            anotherMenu()
            choice = input("What is your choice? ")
            if choice == '1':
                microFreq()
            elif choice == '2':
                #print("The program has ended.\n")
                break
            else:
                print("Invalid response\n")

    def nanoFreq():
        while True:
            try:
                pulse = int(input("Please enter a pulse: "))
                pause = int(input("Please enter a pause: "))
                period = pulse + pause
                print("The period is: " + str(period))
                dutyCycle = (pulse / period) * 100 #needs to be percentage
                print("The duty cycle is: "+ str(round(dutyCycle, 2)) + "%")
                freq = 1000000000 / period #change to measure in Mega Hz
                print("The frequency is: " + str(round(freq, 2)) + "Hz or " + str(round((freq/1000000), 2)) + "MHz\n")
                break
            except ValueError:
                print("No valid integer! Please try again ...")
                
        def anotherMenu():
            print("Would you like to go again or choose another unit of measurment?")
            print("1 Go again!")
            print("2 New unit of measurement please.")

        while True:
            anotherMenu()
            choice = input("What is your choice? ")
            if choice == '1':
                nanoFreq()
            elif choice == '2':
                #print("The program has ended.\n")
                break
            else:
                print("Invalid response\n")
    
    while True:
        measurementsMenu()
        choice = input("What is your choice?\n")
        if choice == '1':
            milliFreq()
        elif choice == '2':
            microFreq()
        elif choice == '3':
            nanoFreq()
        elif choice == '4':
            print("Back to main menu.\n")
            break
        else:
            print("Invalid response\n")

def testKnowledge():

    def measurementsMenu():
        print('''Choose which unit of measurement you would like to view,
please enter the number associate with your choice:''')
        print("1 Milliseconds")
        print("2 Microseconds")
        print("3 Nanoseconds")
        print("4 Exit")

    def milliFreq():
        pulse = random.randrange(10,100,10)
        pause = random.randrange(10,100,10)
        print("The pulse is: ", pulse)
        print("The pause is: ", pause)
        period = pulse + pause
        freq = 1000 / period #measures in Hz
        f = round(freq,2)
        #print(f)

        def test():
            while True:
                try:
                    answer = float(input("What is your answer rounded to two decimal places in Hz? "))
                    if f == answer:
                        print("Correct!\n")
                        break
                    else:
                        def loopAnswer():
                            print("Would you like to try again or see answer?")
                            print("1 Try again")
                            print("2 Let's see the answer")
            
                        while True:
                            loopAnswer()
                            choice = input("What is your choice? ")
                            if choice == '1':
                                test()
                            elif choice == '2':
                                print(f)
                                break
                            else:
                                print("Invalid response\n")
                except:
                    continue
        test()

        def anotherMenu():
            print("Would you like to go again or choose another unit of measurment?")
            print("1 Go again!")
            print("2 New unit of measurement please.")

        while True:
            anotherMenu()
            choice = input("What is your choice? ")
            if choice == '1':
                milliFreq()
            elif choice == '2':
                break
            else:
                print("Invalid response\n")

    def microFreq():
        pulse = random.randrange(10,100,10)
        pause = random.randrange(10,100,10)
        print("The pulse is: ", pulse)
        print("The pause is: ", pause)
        period = pulse + pause
        freq = 1000 / period #change to measure in Kilo Hz
        f = round(freq,2)
        #print(f)
        def test():
            while True:
                try:
                    answer = float(input("What is your answer rounded to two decimal places in Hz? "))
                    if f == answer:
                        print("Correct!\n")
                        break
                    else:
                        def loopAnswer():
                            print("Would you like to try again or see answer?")
                            print("1 Try again")
                            print("2 Let's see the answer")
            
                        while True:
                            loopAnswer()
                            choice = input("What is your choice? ")
                            if choice == '1':
                                test()
                            elif choice == '2':
                                print(f)
                                break
                            else:
                                print("Invalid response\n")
                except:
                    continue
        test()

        def anotherMenu():
            print("Would you like to go again or choose another unit of measurment?")
            print("1 Go again!")
            print("2 New unit of measurement please.")

        while True:
            anotherMenu()
            choice = input("What is your choice? ")
            if choice == '1':
                microFreq()
            elif choice == '2':
                print("The program has ended.\n")
                break
            else:
                print("Invalid response\n")

    def nanoFreq():
        pulse = random.randrange(10,100,10)
        pause = random.randrange(10,100,10)
        print("The pulse is: ", pulse)
        print("The pause is: ", pause)
        period = pulse + pause
        freq = 1000 / period #change to measure in Mega Hz
        f = round(freq,2)
        #print(f)
        def test():
            while True:
                try:
                    answer = float(input("What is your answer rounded to two decimal places in Hz? "))
                    if f == answer:
                        print("Correct!\n")
                        break
                    else:
                        def loopAnswer():
                            print("Would you like to try again or see answer?")
                            print("1 Try again")
                            print("2 Let's see the answer")
            
                        while True:
                            loopAnswer()
                            choice = input("What is your choice? ")
                            if choice == '1':
                                test()
                            elif choice == '2':
                                print(f)
                                break
                            else:
                                print("Invalid response\n")
                except:
                    continue
        test()

        def anotherMenu():
            print("Would you like to go again or choose another unit of measurment?")
            print("1 Go again!")
            print("2 New unit of measurement please.")

        while True:
            anotherMenu()
            choice = input("What is your choice? ")
            if choice == '1':
                nanoFreq()
            elif choice == '2':
                print("The program has ended.\n")
                break
            else:
                print("Invalid response\n")

    while True:
        measurementsMenu()
        choice = input("What is your choice?\n")
        if choice == '1':
            milliFreq()
        elif choice == '2':
            microFreq()
        elif choice == '3':
            nanoFreq()
        elif choice == '4':
            print("Back to main menu.\n")
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



