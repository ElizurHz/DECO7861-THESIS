import csv

with open('gugudan_ioi_dia-modularity.csv', 'r') as csvfile:
    reader1 = csv.reader(csvfile)
    mod_class = [row[2] for row in reader1]

with open('gugudan_ioi_dia-modularity.csv', 'r') as csvfile:
    reader2 = csv.reader(csvfile)
    exp_class = [row[4] for row in reader2]

del mod_class[0]
del exp_class[0]
correct_count = 0.
total = 0.

for i in range(len(mod_class)):
    for j in range(i+1, len(mod_class)):
        total += 1.
        if mod_class[i] == mod_class[j] and exp_class[i] == exp_class[j]:
            correct_count += 1.
        if mod_class[i] != mod_class[j] and exp_class[i] != exp_class[j]:
            correct_count += 1.

accuracy = correct_count/total
print('The accuracy computed from confusion matrix is ' + str(accuracy))