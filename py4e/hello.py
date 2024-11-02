score = input("Enter Score: ")
fscore = float(score)
if fscore > 1 or fscore < 0:
    print('out of range')
else:
    if fscore >= 0.9:
        print('A')
    elif fscore >= 0.8:
        print('B')
    elif fscore >= 0.7:
        print('C')
    elif fscore >= 0.6:
        print('D')
    elif fscore < 0.6:
        print('F')