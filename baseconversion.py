# python recursive base conversion

symbolDict = {
    "A": "10",
    "B": "11",
    "C": "12",
    "D": "13",
    "E": "14",
    "F": "15"
}

def validateNum(inputNum):
    #accept if each digit is either:
    #   ~ a number
    #   ~ a character ie isalpha()
    #   ~ a decimal point
    #otherwise reject

    for digit in inputNum:
        if (digit.isdigit()) or (digit.isalpha()) or (digit=="."):
            continue
        else:
            print("Invalid Input. Try Again (Must be letter, digit, or period")
            exit()        

def convertToB10(inputNum, inputBase):
    numDigits = len(inputNum)
    B10num = 0

    for i in range(0, numDigits):
        if inputNum[i].isalpha():
            coeff = symbolDict[inputNum[i].upper()]
        else:
            coeff = inputNum[i]
        
        exp = (numDigits-1) - i
        nextDigit = int(coeff) * (inputBase**exp)
        B10num += nextDigit

    return str(B10num)
        

def convert(inputNum, inputBase, outputBase):
    validateNum(inputNum)

    B10num = convertToB10(inputNum, inputBase)

    if outputBase == 10:
        return B10num

    return convertTo(inputNum, inputBase, outputBase)

def main():
    #def.
    userNum = input("Input your number (1 digit or longer): ")
    userBase = int(input("What base is your number: "))
    outBase = int(input("What base do you want to convert to: "))
    outNum = 0

    outNum = convert(userNum, userBase, outBase)

    print("("+ str(userNum)+ ")."+ str(userBase)+ " = ("+ str(outNum)+ ")."+ str(outBase)+ "\n")
    input("")

main()
