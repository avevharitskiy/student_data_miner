import itertools

test = [x for x in range(124)]

while test:
    print(test[:100])
    test = test[100:]