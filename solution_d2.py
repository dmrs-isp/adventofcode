# part 1
cntr = 0
with open("puzzle_d2.txt", "r") as thefile:
  for val in thefile:
    entrylist = val.partition(" ")
    low,high = entrylist[0].split("-")
    given_pw = entrylist[2].split(":")
    givenletter = given_pw[0].strip()
    pword = given_pw[1].strip()
    letter_cnt = pword.count(givenletter)
    if (int(low) <= letter_cnt and int(high) >= letter_cnt):
        cntr = cntr + 1
thefile.close()
print(cntr)



# part 2
cntr2 = 0
with open("puzzle_d2.txt", "r") as thefile:
  for val in thefile:
    entrylist = val.partition(" ")
    pos1,pos2 = entrylist[0].split("-")
    given_pw = entrylist[2].split(":")
    givenletter = given_pw[0].strip()
    pword = given_pw[1].strip()
    # print(pword)
    if (pos1 == "1"):
        cpos1 = 0
    else:
        cpos1 = int(pos1) - 1
    cpos2 = int(pos2)

    first_cond = pword[cpos1] == givenletter
    if (len(pword) == cpos2):
        second_cond = pword[-1] == givenletter
    else:
        second_cond = pword[cpos2 - 1] == givenletter

    if (first_cond and not second_cond):
        cntr2=cntr2+1
    if (not first_cond and second_cond):
        cntr2=cntr2+1
thefile.close()
print(cntr2)