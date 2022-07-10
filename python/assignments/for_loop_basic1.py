#Assignment: Core For Loop Basic 1

#1. Basic - print all integers 0 - 150

for i in range(0,150):
    # print(i)

# #2 Multiples of 5 - print all multiples of 5 from 5-1000

    for i in range(0,1000,5):
    # print(i)

#3 Counting the dojo way - print integers 1-100, if divisible by 4 print coding instead. If divisible by 10 print "coding
# dojo"

        for y in range(1,100):
            print(y)
        if y % 4:
            print("coding")
        else:
            y % 10: #not sure what I'm doing wrong here.
            print("coding dojo")

#4 whoa. that sucker's huge - add odd integers from 0 - 500,000 and print the final sum

            num = 0
            for i in range(1, 500000, 2):
                num += i
                print(num)

#5 countdown by fours - print positive numbers starting at 2018, counting down by fours
                for i in range(2018, 0, -4):
                    print(i)

#6 flexible counter - set 3 variables lowNum, highNum, mult. starting at lowNum and "
# going through highNum, print only the integers that are a multiple of mult. For ex if lowNum = 3, highNum =  and 
# mult = 3 the loop should print 3,6,9 (on successive lines"

                    lowNum = 2
                    highNum = 9
                    multNum = 3

                    for i in range(lowNum, highNum + 1):
                        if i % multNum == 0:
                            print(i)
