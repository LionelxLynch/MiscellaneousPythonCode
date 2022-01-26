def counter(s,l):
    string = str(s)
    letter = str(l)
    count = 1
    for item in string:
        if item == letter:
            print(count)
            count = count + 1

counter('apple','p')