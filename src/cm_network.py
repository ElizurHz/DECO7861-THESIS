import csv

with open('gugudan_ioi_dia_modClass.csv', 'r') as csvfile:
    reader1 = csv.reader(csvfile)
    mod_class = [row[2] for row in reader1]

with open('gugudan_ioi_dia_expClass.csv', 'r') as csvfile:
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
print('The accuracy computed from confusion matrix is ' + str(accuracy))