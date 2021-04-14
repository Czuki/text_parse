import os
import re


class IndentConverter:
    """Converts leading spaces to tabs or tabs to spaces"""
    def __init__(self, file_name, convert_from=None, space_count=4, replace=False):
        if os.path.exists(file_name):
            self.file_name = file_name
        else:
            raise FileNotFoundError('File not found')
        self.replace = replace
        self.convert_from = convert_from
        self.space_count = space_count if convert_from == 'tabs' else 4

    @staticmethod
    def get_new_file_name(file_name, number=1):
        """
        :param str file_name: base to generate new non-conflicting name
        :param int number: to add at the end of new file name

        creates new non-conflicting file name
        if file replace is not desired

        :return: str new_file_name: new non-conflicting file name
        """
        name_split = file_name.split('.')
        new_file_suffix = f'{number}'
        new_file_name = name_split[0] + new_file_suffix + '.' + name_split[1]
        while os.path.exists(new_file_name):
            number += 1
            new_file_name = IndentConverter.get_new_file_name(file_name, number)
        return new_file_name

    @staticmethod
    def replace_line(line, spaces, pattern):
        """
        :param str spaces: spaces to replace each tab
        :param str line: line from a text file
        :param pattern: regex pattern to match tabs or spaces

        replaces tabs to spaces or
        spaces to tabs in provided line in file

        :return: str new_line: line with replaced indentation to write in new file:
        """
        new_line = ''
        to_replace = pattern.findall(line)
        if to_replace:
            if pattern == re.compile(r'^\t+'):
                replaced = ''.join(to_replace).replace('\t', spaces)
                new_line = replaced + line.lstrip('\t')
            elif pattern == re.compile(r'^ +'):
                replaced = ''.join(to_replace).replace(spaces, '\t')
                new_line = replaced + line.lstrip(' ')
        else:
            new_line = line
        return new_line

    def set_pattern(self):
        """sets pattern for regex to find leading spaces or tabs"""
        pattern = None
        if self.convert_from == 'tabs':
            pattern = re.compile(r'^\t+')
        elif self.convert_from == 'spaces':
            pattern = re.compile(r'^ +')
        elif self.convert_from is None:
            pattern = self.check_indent_type()
        return pattern

    def replace_leading_whitespace(self):
        """
        opens file, iterates over each line and replaces
        leading whitespaces using replace_line method

        :return: str modified_text: text file content after replacing indentation
        """
        modified_rows_count = 0
        spaces = self.space_count * ' '
        modified_text = ''

        pattern = self.set_pattern()
        if pattern is None:
            print('No indentations in file')
            return False

        with open(self.file_name, 'r') as file:
            line = file.readline()
            while line != '':
                new_line = IndentConverter.replace_line(line, spaces, pattern)
                if new_line != line:
                    modified_rows_count += 1
                modified_text += new_line
                line = file.readline()
        print(f'Modified rows in file: {modified_rows_count}')
        return modified_text

    def check_indent_type(self):
        """
        checks indentation type in file
        if indentation type is not specified

        :return: pattern: regex pattern for matching tabs or spaces, None if no indents found
        """
        print('Indentation type not specified')
        tab_pattern = re.compile(r'^\t+')
        space_pattern = re.compile(r'^ +')
        with open(self.file_name) as file:
            line = file.readline()
            while line != '':
                if tab_pattern.match(line):
                    print('Detected indentation: tabs')
                    return tab_pattern
                elif space_pattern.match(line):
                    print('Detected indentation: spaces')
                    return space_pattern
                line = file.readline()
        return None

    def write_to_file(self, modified_text):
        """
        :param str modified_text: text file content after replacing indentation

        writes to file, uses get_new_file_name method
        to create new file name if file replace is not desired
        """
        if self.replace:
            print('File overwritten')
        else:
            self.file_name = IndentConverter.get_new_file_name(self.file_name)

        with open(self.file_name, 'w') as new_file:
            new_file.write(modified_text)
