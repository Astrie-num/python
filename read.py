name = input("Enter the name of your file: ")
handle = open(name, 'r')
counts = dict()

for line in handle: 
    words = line.split()
    # print(words)
    for word in words: 
        counts[word] = counts.get(word, 0) + 1
        # print(counts)
    bigcount = None
    bigword = None
    for word, count in list(counts.items()):
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count
        print(bigword, bigcount)


        input : is to get the data from the outside world
        output : is used to play the result
        
