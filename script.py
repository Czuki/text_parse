import re
import os


def tabs_to_spaces(space_count, file_name):
    modified_rows_count = 0
    spaces = space_count * ' '
    modified_text = ''

    with open(file_name, 'r') as file:
        line = file.readline()
        while line != '':
            leading_tabs = re.findall(r'^\t+', line)
            leading_spaces = ''.join(leading_tabs).replace('\t', spaces)
            new_line = leading_spaces + line.lstrip('\t')
            if line != new_line:
                modified_rows_count += 1
            modified_text += new_line
            line = file.readline()
    return modified_rows_count, modified_text


def get_new_file_name(file_name, number=1):
    name_split = file_name.split('.')
    new_file_suffix = f'{number}'
    new_file_name = name_split[0] + new_file_suffix + '.' + name_split[1]

    while os.path.exists(new_file_name):
        number += 1
        new_file_name = get_new_file_name(file_name, number)

    return new_file_name


def write_to_file(file_name, modified_text, replace=False):
    if not replace:
        file_name = get_new_file_name(file_name)

    with open(file_name, 'w') as new_file:
        new_file.write(modified_text)


if __name__ == '__main__':
    count, modified_text = tabs_to_spaces(space_count=2, file_name='test.py')
    write_to_file(file_name='test.py', modified_text=modified_text, replace=False)


# a = '''
# 	row1
# 		row2
# 	row3
# 			row4		row4  row4
# row5
# 		row6
# row7
# 	row8
# 				row9
#
#     row10
#
#
# '''