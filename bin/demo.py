import random as r
lowerChars='abcdefghijklmnopqrstuvwxyz'
idx=list(range(26)) # indices into the lowerChars string; explicitly cast as list for it to work in python3


# given a character set and center letter, output all the possible solutions
# this is the brute-force approach; optimization later
def solutions(chars, center):
    assert center in chars
    sol=[]
    f=open("../lib/"+center+'.txt','r') # open the preprocessed file for searching
    for line in f:
        goodLine=True
        for ch in line[:-1]: # get rid of the newline at the end
            if ch not in chars: # if even one of them is not desired
                goodLine=False
                continue
        if (goodLine):
            sol.append(line[:-1]) # if every char from this line is good: solution
    f.close()
    return sol


print("--------Lexathon!!!!--------")

while (True):
    print("----------------------------")
    quit=input("enter 'q' to quit, or anything else to start a new round: ")
    if (quit=='q' or quit=='Q'):
        break;
    # randomly select 9 chars to play the game; 4th char is the center
    r.shuffle(idx)
    chars=[lowerChars[i] for i in idx[:9]]
    center=chars[4]
    # print the grid
    for j in range(9):
        print(chars[j]+" ", end="") # force print without newline in py3
        if (j%3==2):
            print()
    soln=solutions(chars, center)
    ans=[]
    while (True):
        print()
        entry=input("enter your word (4-9 char lower case, must use the letter at the centerof the grid): ")
        if (entry in soln and entry not in ans):
            print("Right on!")
            ans.append(entry)
        elif (entry in ans):
            print("You already found it!")
        else:
            print("Nope...")
        print("Words found so far: ",ans)
        print(str(len(ans))+" out of "+str(len(soln)))
        todo=input("enter 'S' for all solutions, 'D' to be done with this round, or anything else to keep playing: ")
        if (todo=='S'):
            print(soln)
        elif (todo=='D'):
            break

print("bye")



