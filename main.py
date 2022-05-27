# function to check if two strings are
# anagram or not
def check(s1, s2):
     
    # the sorted strings are checked
    if(sorted(s1)== sorted(s2)):
        print("True.")
    else:
        print("False.")        
         
# driver code 
print( "Check if these words are anagram")
s1 = input("Enter the First word: ")
s2 = input("Enter Second word: ")
check(s1, s2)