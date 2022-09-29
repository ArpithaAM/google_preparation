# String segmentation
# You are given a dictionary of words and a large input string.
# You have to find out whether the input string can be completely segmented into the words of a given dictionary.
# The following two examples elaborate on the problem further.


def canParseUtil(wordList,word):
    size = len(word)
    if(size == 0):
        return True
    tmp = ""
    for i in range(0,size):
        tmp += word[i]
        if((tmp in wordList) and canParseUtil(wordList,word[i+1:])):
            return True
    return False
        
    
words = ["mobile","samsung","sam","sung",
         "man","mango","icecream","and",
         "go","i","like","ice","cream"]
word = "cream"
print(canParseUtil(words, word))