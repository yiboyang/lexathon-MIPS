# this is the version that allows duplicate letters in the grid 
# the preprocessed dictionaries should be updated accordingly
# make sure you're using python3
# By Yibo Yang

import random as r

lowerChars='abcdefghijklmnopqrstuvwxyz'

# given a character set and center letter, output all the possible solutions by examing the dictionary file corresponding to center character
# this is probably not the most efficient approach; since we now allow repetitive letters (but they have to all come from the grid),
# we'll have to also consider the number of occurences of each letter in an entry. The most straightforward solution is to use the list
# of grid chars and remove letters from it as we scan each entry letter by letter in dictionary; we skip that entry once a remove fails; 
# otherwise we accept it as a solution
def solutions(chars, center):
    assert center in chars
    sol=[] # assuming the dictionary files are nice and contain no duplicates; otherwise we have to use a set
    f=open("../lib/"+center+'.txt','r') # open the preprocessed file for searching
    for line in f:
        pool=chars[:] # make a deep copy; this could be inefficient; instead, next time use a boolean array for this operation (reset everytime)
        goodLine=True
        for ch in line.rstrip(): # get rid of the newline at the end
            try:
                pool.remove(ch) # throws exception when can't remove (removes one entered at a time)
            except ValueError: # if even one of them is not in our pool
                goodLine=False
                break # in previous versions this was 'continue'--wrong wrong wrong!
        if (goodLine):
            sol.append(line[:-1]) # every char from this line is good? : solution
    f.close()
    return sol

# print list of 9 chars in a grid
def printGrid(chars): 
    assert len(chars)==9
    print("------")
    for j in range(9):
        print(chars[j]+" ", end="") # force print without newline in py3
        if (j%3==2):
            print()
    print("------")

# main
def game():
    print("--------Lexathon!!!!--------")
    while (True):
        print("----------------------------")
        quit=input("enter 'q' to quit, or anything else to start a new round: ")
        if (quit=='q' or quit=='Q'):
            break;
        # randomly select 9 unique chars to play the game; 4th char is the center
        idx=[r.randrange(26) for _ in range(9)] # generate 9 non-unique random numbers in [0, 25]
        chars=[lowerChars[i] for i in idx[:9]] # index into lowerChars to get random letters list
        center=chars[4] # get char at the center of the grid that determines solutions
        
        soln=solutions(chars, center)
        ans=[]
        while (True):
            print()
            printGrid(chars)
            entered=input("enter your word (4-9 char lower case, must use the letter at the centerof the grid); [enter 'S' for all solutions, 'D' to be done with this round]: ")
            print()
            if (entered=='S'):
                print(soln)
                continue
            elif (entered=='D'):
                break
            elif (len(entered)<4 or len(entered)>9): # minimal input validation :)
                print("Make sure your entry has 4-9 chars!")
                continue
            elif (entered in soln and entered not in ans):
                print("Right on!")
                ans.append(entered)
            elif (entered in ans):
                print("You already found it!")
            else:
                print("Nope...")
            print("Words found so far: ",ans)
            print(str(len(ans))+" out of "+str(len(soln)))
    
    print("bye")


if __name__ == "__main__":
    game()