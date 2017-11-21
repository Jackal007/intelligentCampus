with open('studentID_test.txt', 'r') as f:
    studentIds = [line.strip() for line in f.readlines()]
    f2 = open('results/results.csv', 'r')
    sids = [line.split(',')[0] for line in f2.readlines()]
    f2.close()
    f2 = open('results/results.csv', 'a')
    t = list(set(studentIds).difference(set(sids)))
    print(len(t))
    for i in t:
        f2.write(i + ",0\n")
    f2.close()