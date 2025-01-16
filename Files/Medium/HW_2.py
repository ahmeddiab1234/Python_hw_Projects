# HW - 2 - Files - Medium - Compute Differences V1

from datetime import datetime
import re


def parse_numbers(string):
    return map(int, string.split(' '))


def compute_daily_increment(rows):
    previous_row = rows[0].split('\t')
    for i in range(1, len(rows)):
        current_row = rows[i].split('\t')
        date = current_row[0]

        new_line = [date]  
        for j in range(1, len(current_row)):
            prev_rating, prev_students = parse_numbers(previous_row[j])
            cur_rating, cur_students = parse_numbers(current_row[j])

            diff = max(0, cur_students - prev_students)
            new_line.append(f"{cur_rating} {cur_students} +{diff}")

        rows[i] = '\t'.join(new_line)
        previous_row = current_row
    return rows


def filter_and_group_lines(file_path):
    with open(file_path) as file:
        lines = [line for line in file.read().splitlines() if 'NA' not in line]

    grouped = {}
    for line in lines:
        date = line.split('\t')[0].split(' ')[0]  
        grouped[date] = line 

    return list(grouped.values())


def generate_output(input_file, output_file):
    filtered_lines = filter_and_group_lines(input_file)
    updated_lines = compute_daily_increment(filtered_lines)

    with open(output_file, 'w') as file:
        file.write('\n'.join(updated_lines) + '\n')


if __name__ == '__main__':
    input_file = r'E:\Python_live\Python_HW\Files\Medium\courses.txt'
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = fr'E:\Python_live\Python_HW\Files\Medium\courses-output-{now}.txt'

    generate_output(input_file, output_file)
    print(f"Output saved to: {output_file}")







