import random
import pickle

#create word list
wordCount = random.randint(1000, 10000)
wordList = set()
for _ in range(wordCount):
    newWordLength = random.randint(5, 10)
    newWord = "".join([random.choice("abc") for _ in range(newWordLength)])
    wordList.add(newWord)

#create the queries
queryCount = random.randint(1000, 10000)
queryList = []
for _ in range(queryCount):
    if random.random() > 0.5:
        word = list(random.sample(wordList, 1)[0])
        random.shuffle(word)
        word = "".join(word)
        queryList.append(word)
    else:
        newWordLength = random.randint(5, 10)
        newWord = "".join([random.choice("abc") for _ in range(newWordLength)])
        queryList.append(newWord)

#create initialization key value pair list
keySet = set()
keyCount = random.randint(10, 50)
for _ in range(keyCount):
    keySet.add(random.randint(-5, 5))
initialList = []
for key in keySet:
    value = random.randint(1,10)
    initialList.append((key, value))

#create queries
treeQueryList = []
queryCount = random.randint(1000, 10000)
for _ in range(queryCount):
    if random.random() > 0.3:
        treeQueryList.append(("insert", random.randint(-5, 5)))
    else:
        treeQueryList.append(("count", random.randint(-5, 5)))

cases = {"wordList": wordList, "queryList": queryList, "initialList": initialList, "treeQueryList": treeQueryList}
pickle.dump(cases, open("cases.dat", "wb"))
