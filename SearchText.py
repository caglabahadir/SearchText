searchWord = input("aranacak kelimeyi giriniz:")
roundSize = 0
wordSize = []
searchText = open("SearchText.txt","r")
file = searchText.read()
file = file.lower()
searchWord = searchWord.lower()
wordList= file.split()
for i in wordList:
    roundSize += 1
    if i == searchWord:
        wordSize.append(roundSize)
print("Location: ", wordSize)
print("Word Count: ", len(wordSize))