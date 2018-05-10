import random
import pickle

queryLists = []
# create 20 sets of queryLists
for _ in range(100):
    # create the queries
    queryCount = random.randint(50, 100)
    queryList = []
    insertedSoFar = set()
    val = random.randint(-queryCount, queryCount)
    queryList.append(("insert", val))
    insertedSoFar.add(val)
    for _ in range(queryCount):
        if random.random() > 0.2:
            val = random.randint(-queryCount, queryCount)
            insertedSoFar.add(val)
            queryList.append(("insert", val))
        else:
            val = random.sample(insertedSoFar, 1)[0]
            queryList.append(("search", val))
    queryLists.append(queryList)

cases = {"queryLists": queryLists}
pickle.dump(cases, open("cases.dat", "wb"))
