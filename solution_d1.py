intlist = []
idx = 0
foundit = 0
ans = 0

with open("inputdata.txt", "r") as thefile:
  for val in thefile:
    intval = int(val)
    intlist.append(intval)    
thefile.close()

# for day1
for num1 in intlist:
    idx = intlist.index(num1)
    for num2 in intlist:
        if idx != intlist.index(num2) and foundit == 0:
             if (num1 + num2 == 2020):
                ans = num1 * num2
                print("The answer for day 1 is " + str(ans))
                foundit = 1
                break
# for day 2
idx = 0
idx2 = 0
foundit = 0
ans = 0
for num1 in intlist:
    idx = intlist.index(num1)
    for num2 in intlist:
        if idx != intlist.index(num2) and foundit == 0:
          idx2 = intlist.index(num2)
          for num3 in intlist:
             if idx != intlist.index(num3) and idx2 != intlist.index(num3) and foundit == 0:
                if (num1 + num2 + num3 == 2020):
                  ans = num1 * num2 * num3
                  print("The answer for day 2 is " + str(ans))
                  foundit = 1
                  break