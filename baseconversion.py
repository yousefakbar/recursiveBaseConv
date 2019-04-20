# python recursive base conversion.

# A = ord(65) -- Z = 90 -- subtract 55 from all ord() values for DEC

def validateNum(inputNum):
    '''validates input number. each digit must be number, letter, or dot'''
    for digit in inputNum:
        if (digit.isdigit()) or (digit.isalpha()) or (digit=="."):
            continue
        else:
            print("Invalid Input. Try Again (Must be letter, digit, or period")
            exit()

def convertToB10(inputNum, inputBase):
    '''converts input number to base 10 using iterative sigma expansion'''
    numDigits = len(inputNum)
    B10num = 0

    for i in range(0, numDigits):
        if inputNum[i].isalpha(): 
            coeff = ord(inputNum[i].upper()) - 55
        else:
            coeff = inputNum[i]
        
        exp = (numDigits-1) - i
        nextDigit = int(coeff) * (inputBase**exp)
        B10num += nextDigit

    return str(B10num)

def recursiveConvert(B10num, outputBase):
    '''recursive function that converts any base 10 number to a specified base'''
    remainder = B10num % outputBase
    if remainder >= 10:
        remainder = chr(55 + remainder)

    if B10num < outputBase:
        return remainder
    else:
        return str(recursiveConvert(int(B10num/outputBase), outputBase)) + str(remainder)

def convert(inputNum, inputBase, outputBase):
    '''validates input number, converts to B10, and to outputBase if need be'''
    validateNum(inputNum)
    B10num = convertToB10(inputNum, inputBase)

    if outputBase == 0:
        return B10num

    return recursiveConvert(int(B10num), outputBase)

def main():
    '''main function'''
    userNum = input("Input your number (1 digit or longer): ")
    userBase = int(input("What base is your number: "))
    outBase = int(input("What base do you want to convert to: "))
    outNum = 0

    outNum = convert(userNum, userBase, outBase)

    print("("+ str(userNum)+ ")."+ str(userBase)+ " = ("+ str(outNum)+ ")."+ str(outBase)+ "\n")
    input("")

main()
