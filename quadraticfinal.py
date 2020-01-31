
#IMPORTED MODULES
#------------------------------------------------------------------------------------#

import math


#FUNCTIONS DEFINED
#------------------------------------------------------------------------------------#

def quadform(deter, g, h):
    if deter >= 0:
        deter = deter
        imagine = 1
    else:
        deter = -deter
        imagine = 0

    if imagine == 0:
        answ_1 = "(" +  str(-h) + " + " + str(math.sqrt(deter)) + " i)" + "/" + str(2*g)
        answ_2 = "(" +  str(-h) + " - " + str(math.sqrt(deter)) + " i)" + "/" + str(2*g)
    else:
        answ_1 = (-h+(math.sqrt(deter)))/(2*g)
        answ_2 = (-h-(math.sqrt(deter)))/(2*g)
    answ_f = "    " + str(answ_1) + "    AND     " + str(answ_2)
    return (answ_f)



def determinator(m, n, o):
    det = (n*n)-(4*m*o)
    if det >= 0:
        print("\nReal Solutions\n")
    else:
        print("\nImaginery Solutions\n")
    return (det)


#PROGRAM START
#------------------------------------------------------------------------------------#

print("WELCOME TO THE QUADRATIC SOLUTION FINDER\n\nGUIDE:\nFollow the onscreen instructions to input the coefficients of each term \nin a quadratic equation.\n\nThe equation should be already reduced to the form below:\n\nax^2 + bx + c = 0\n\nwhere a, b, c are positive or negative constants you would be asked to enter.\n") 
continuecounter = 0
while continuecounter == 0:
    print("------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------")
    a = float(input("\nEnter coefficient of x^2 (a): "))
    b = float(input("Enter coefficient of x   (b): "))
    c = float(input("Enter constant           (c): "))
    determinent = determinator(a, b, c)
    answer = quadform(determinent, a, b)
    print("------------------------------------------------------------------------------------")
    print("The solutions are: " + str(answer))
    print("------------------------------------------------------------------------------------")
    continuecounter = int(input("Press '1' to end the program\nPress '0' to solve another equation\nEnter '1' or '0': "))

print("------------------------------------------------------------------------------------")
print("\n\nTHANK YOU FOR USING OUR PROGRAM.\nUNTIL NEXT TIME!\nCREDITS=ADITYA BANERJEE & YASHIKA CHHABARIA")



#PROGRAM END
#------------------------------------------------------------------------------------#
