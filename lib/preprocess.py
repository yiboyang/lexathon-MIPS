import sys

# By Yibo Yang
# input: name of the word list file to be preprocessed, e.g.
# preprocess('linux_words.txt');
# output: 26 text files: list_a.txt, list_b.txt, list_c.txt, ... list_z.txt. Each
# lists words that contain the corresponding character, which are also 
# potentially 'valid' entries in the Lexathon game (with that particular
# character at the center), i.e. no repeated characters, length b/w 4 and 9

# define some evil global vars
lowerChars='abcdefghijklmnopqrstuvwxyz'
minCharNum=4 # default minimum number of characters
maxCharNum=9


def preprocess(wordlist):
    # First create and collect a bunch of file handles for the output files
    foutList=[]
    for char in lowerChars:
        out='list_'+char+'.txt'
        try:
            fout=open(out,'w')
            foutList.append(fout)
        except IOError:
            print("Can't create output files")
            sys.exit(1)
            
    # Now real processing
    with open(wordlist, 'r') as words:
        for word in words:
            if valid(word):
                for char in word: # append this word with appropriate handle
                    if char>'z' or char<'a': # handle weird chars or EOF newline
                        break
                    foutList[ord(char)-97].write(word)
                        
    for fout in foutList:
        fout.close()


# returns true if the given string is 'valid'
def valid(string):
    if string[0]>='A' and string[0]<='Z': # discard words starting with uppercase
        return False;
    if len(string)<minCharNum or len(string)>maxCharNum:
        return False;
    for char in lowerChars:
        if string.count(char)>1: # if any char appears more than once
            return False;
    return True;


if __name__ == '__main__':
    if (len(sys.argv)!=2):
        raise ValueError('usage: preprocess.py <inputfile>')
    preprocess(sys.argv[1])
    print('Finished!')
