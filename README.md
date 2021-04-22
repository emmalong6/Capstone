# Basic Computer Architecture Scripts

### Table of Contents
1. Introduction
2. Installation
3. Usage
4. License

## Introduction
I designed three scripts to help students practice equations used in Basic Computer Architecture. I used python to program each script that calculates frequency, grey code, and twos complement. These programs run directly from the command line in the python compiler of your choice.

## Installation
* Download
* Run with any Python compiler

## Technologies
Python was used in developing these three calculating scripts. Here is a sample of code that was used in both the grey code and twos complement scripts to convert decimal numbers into binary.
```python
n = int(input("Please enter a decimal number: "))
if (n < 1025):
  binary = ""
  for i in range(16, -1, -1):  
    k = n >> i
    if (k & 1): 
      binary += "1"
    else: 
      binary += "0"
  return binary
else:
  print("Please unter a number from 0 to 1024 inclusive")
  continue
```

## Usage
1. Run the programs with the python compiler of your choosing.
2. With all three scripts, input your choices in the command line by entering the number associated with your choice.

## License
This project uses the [MIT License](https://github.com/emmalong6/Capstone/blob/main/LICENSE).
