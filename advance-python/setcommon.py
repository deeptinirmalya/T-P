# #find common element between two list.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
set1 = set(list1)
set2 = set(list2)
cn = set1 & set2
print(list(cn))
#-------------------------------------------------------------------------------------------
#remove duplicate word from sentence 
sentence = "this is a a is a advance python on advance "
words = sentence.split()
unique_words = set(words)
result = " ".join(unique_words)
print(result)


# # ------------------------------------------------------------------------------------------
# #anagram string
str1="listen"
str2="silent"
if len(str1)==len(str2):
    ss1=sorted(str1)
    ss2=sorted(str2)
    if len(ss1)==len(ss2):
        print(f"{str1} and {str2} are anagram words")
    else:
        print(f"{str1}and{str2} are not anagram words")
else:
     print(f"{str1}and{str2} are not anagram words")

#-------------------------------------------------------------------------------------------
## present in list 1 but not in list 2
lis1=[1,2,3,4,5,6,7]
lis2=[1,2,3,9,8,10]
set1=set(lis1)
set2=set(lis2)
un=set1-set2
print(list(un))
##---------------------------------------------------------------------------------------------
##all char in a set are unique
string="hello"
set10=set(string)
if string==set10:
    print("have duplicate character")
else:
    print(f"{string} is a unique character")