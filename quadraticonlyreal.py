
#IMPORTED MODULES
#------------------------------------------------------------------------------------#

import math


#FUNCTIONS DEFINED
#------------------------------------------------------------------------------------#

def quadform(deter, g, h):
    answ_1 = (-h+(math.sqrt(deter)))/(2*g)
    answ_2 = (-h-(math.sqrt(deter)))/(2*g)
    answ_f = "    " + str(answ_1) + "    AND     " + str(answ_2)
    return (answ_f)

def determinator(m, n, o):
    det = (n*n)-(4*m*o)
    if det >= 0:
        print("\nValid equation\nReal Solutions\n")
        return (det)
    else:
        print("\nInvalid equation\nImaginery Solutions\nTry Again\n\n")
        return (-1)


#PROGRAM START
#------------------------------------------------------------------------------------#

print("WELCOME TO THE QUADRATIC SOLUTION FINDER\n\nGUIDE:\nFollow the onscreen instructions to input the coefficients of each term \nin a quadratic equation.\n\nThe equation should be already reduced to the form below:\n\nax^2 + bx + c = 0\n\nwhere a, b, c are positive or negative constants you would be asked to enter.\n\nDISCLAIMER: \nEQUATIONS WITH IMAGINERY SOLUTIONS CANNOT BE SOLVED USING THIS PROGRAM\n\n")
determinent = -1
while determinent <= -1:
    print("------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------")
    a = float(input("Enter coefficient of x^2 (a): "))
    b = float(input("Enter coefficient of x   (b): "))
    c = float(input("Enter constant           (c): "))
    determinent = determinator(a, b, c)

answer = quadform(determinent, a, b)
print("------------------------------------------------------------------------------------")
print("The solutions are: " + str(answer))
print("------------------------------------------------------------------------------------")
print("\n\nTHANK YOU FOR USING OUR PROGRAM.\nUNTIL NEXT TIME!\n\nCREDITS: \nAditya Banerjee :)")


#PROGRAM END
#------------------------------------------------------------------------------------#
