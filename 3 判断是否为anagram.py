word1 = input("Enter a word: ")
word2 = input("Enter another word: ")
list1 = list(word1)
list2 = list(word2)
i = 0
list1.sort()
list2.sort()
a = len(word1)

if len(word1) != len(word2):
    T = 0
else:
    for i in range(0,a):
        if list1[i] != list2[i]:
            T = 0
            break
        else:
            T=1
if T == 1 :
    print(word1,"and",word2,"are anagrams of each other.")
else :
    print(word1,"and",word2,"are not anagrams of each other.")
