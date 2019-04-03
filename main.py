"""
This is a simple script created to extract measured times
in a DTU course.
The filter.c outputs its timing in a nice format, which
this will read and extract data from. Very nice yes.!
"""
import csv

output_file = open('times.csv', 'w', newline='')

file_writer = csv.writer(output_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
file_writer.writerow(
    ['filename', 'egg seg', 'egg n', 'owl seg', 'owl n', 'pocket seg', 'pocket n', 'poppy seg', 'poppy n', 'total seg',
     'total n'])

for i in range(1, 5):
    for j in range(1, 9):
        filename = f"data/filter_{i}_{j}.log"
        temp_list = [filename]
        data_file = open(filename, 'r')
        for line in data_file:
            if '=' in line:
                line = line[line.find('=') + 1:]
                line = float(line.strip())
                temp_list.append(line)
                continue
            if 'Total' in line:
                line = line[line.find(':') + 1:]
                line = float(line.strip())
                temp_list.append(line)

        file_writer.writerow(temp_list)
