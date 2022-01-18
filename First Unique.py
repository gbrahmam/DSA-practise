# your code goes here
from collections import defaultdict
from collections import Counter

def first_unique(svar):
    
    char_count = Counter(svar)
    
    for each in char_count:
        if char_count[each]==1:
            return svar.find(each)
            
    return -1
    
for i in range(int(input())):
    print(first_unique(input()))