stringList = []
for i in range(1, 65):
    with open('dailyFiles/' + str(i) + '.txt', 'r') as file:
        stringList.append(file.read())
with open('stringList.cpp', 'w') as file:
    file.write('#include <string>\nusing namespace std;\nstring stringList[64] = {\n')
    for a in stringList:
        a = a.replace('\n', '\\n')
        file.write('\t"' + a[:-2] + '",\n')
    file.write('};')
