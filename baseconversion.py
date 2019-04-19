# python recursive base conversion

def convertToB10(inputNum, inputBase):
    numDigits = len(inputNum)
    B10num = 0

    for i in range(0, numDigits):
        exp = (numDigits-1) - i
        print(int(inputNum[i])*(inputBase**exp))
        nextDigit = int(inputNum[i]) * (inputBase**exp)
        B10num += nextDigit

    return str(B10num)
        

def convert(inputNum, inputBase, outputBase):
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
