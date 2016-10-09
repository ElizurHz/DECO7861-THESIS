import csv

def confusion_matrix(list):
    with open('output/' + list + '_modClass.csv', 'r') as csvfile:
        reader1 = csv.reader(csvfile)
        mod_class = [row[1] for row in reader1]

    with open('output/' + list + '_expClass.csv', 'r') as csvfile:
        reader2 = csv.reader(csvfile)
        exp_class = [row[1] for row in reader2]

    del mod_class[0]
    del exp_class[0]
    correct = 0.
    total = 0.

    for i in range(len(mod_class)):
        for j in range(i+1, len(mod_class)):
            total += 1.
            if mod_class[i] == mod_class[j] and exp_class[i] == exp_class[j]:
                correct += 1.
            if mod_class[i] != mod_class[j] and exp_class[i] != exp_class[j]:
                correct += 1.

    accuracy = correct/total
    return accuracy

if __name__ == '__main__':
    accuracy = confusion_matrix('rv')
    print('The accuracy computed from confusion matrix is ' + str(accuracy))
