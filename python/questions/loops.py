# #3 Counting the dojo way - print integers 1-100, if divisible by 4 print coding instead. If divisible by 10 print "coding
# # dojo"

for y in range(1,100):
        print(y)
        if y % 4 == 0:
            print("coding")
        elif y % 10 == 0: #needed to at the == 0: because the % property just outputs the remainder not division so you need to include the == 0 so it gives the division.
            print("coding dojo")