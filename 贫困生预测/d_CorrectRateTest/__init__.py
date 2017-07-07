with open('studentID_test.txt', 'r') as f:
    studentIds = [line.strip() for line in f.readlines()]
    print(studentIds[0])
    f2 = open('results_ExtraTreesClassifier.csv', 'r')
#     f2 = open('results_GaussianNB.csv', 'r')
#     f2 = open('results_NearestCentroid.csv', 'r')
#     f2 = open('results_SGDClassifier.csv', 'r')
#     f2 = open('results_SVC.csv', 'r')
#     f2 = open('results_tree.csv', 'r')
    sids = [line.split(',')[0] for line in f2.readlines()]
    print(sids[0])
    f2.close()
    f2 = open('results_ExtraTreesClassifier.csv', 'a')
#     f2 = open('results_GaussianNB.csv', 'a')
#     f2 = open('results_NearestCentroid.csv', 'a')
#     f2 = open('results_SGDClassifier.csv', 'a')
#     f2 = open('results_SVC.csv', 'a')
#     f2 = open('results_tree.csv', 'a')
    t = list(set(studentIds).difference(set(sids)))
    print(len(t))
    for i in t:
        f2.write(i + ",0\n")
    f2.close()