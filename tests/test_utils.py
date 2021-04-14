import os

TABS_TO_SPACES = '''\trow1
\t\trow2\t
\trow3    

\t\trow4
'''

SPACES_TO_TABS = '''    row1
        row2\t
    row3    

        row4
'''

NO_INDENT ='''row1
row2
row3
row4

row5
row6'''


def create_test_files():
    with open('tabs_to_spaces.txt', 'w') as test_file:
        test_file.write(TABS_TO_SPACES)

    with open('spaces_to_tabs.txt', 'w') as test_file:
        test_file.write(SPACES_TO_TABS)

    with open('no_indent.txt', 'w') as test_file:
        test_file.write(NO_INDENT)


def remove_test_files():
    if os.path.exists('tabs_to_spaces.txt'):
        os.remove('tabs_to_spaces.txt')

    if os.path.exists('tabs_to_spaces1.txt'):
        os.remove('tabs_to_spaces1.txt')

    if os.path.exists('spaces_to_tabs.txt'):
        os.remove('spaces_to_tabs.txt')

    if os.path.exists('spaces_to_tabs1.txt'):
        os.remove('spaces_to_tabs1.txt')

    if os.path.exists('no_indent.txt'):
        os.remove('no_indent.txt')

    if os.path.exists('no_indent1.txt'):
        os.remove('no_indent1.txt')
