def word_smith(forbidden_alphabets):     #1  0
    # You can start from here 
    def chopper(input_string):           #1  0
        newstr=''                        #1  1
        for i in input_string:           #n  1
            if i not in forbidden_alphabets:     #n  0
                newstr+=i                        #n  n
        return newstr                            #1  0
        
    return chopper                               #1  0

# Tc = 5+3n-----?O(n)      S = 2+n-----> O(n)

### Do not change anything below this line.
if __name__ == "__main__":
    alphabets = [i for i in input().split(' ')]
    input_string = input()
    chopper = word_smith(alphabets)
    print(chopper(input_string))