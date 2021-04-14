import argparse

from logic.converter import IndentConverter


def create_parser():
    """
    creates parser object and adds required command line arguments

    :return: parser and args objects
    """
    parser = argparse.ArgumentParser(description='Indent Converter')
    parser.add_argument('-f', '--from', dest='from_', help='indent to convert from', choices=['tabs', 'spaces'])
    parser.add_argument('-r', '--replace', help='replace file flag', action='store_true')
    parser.add_argument('-t', '--tab-chars', help='amount of spaces per tab', type=int, default=4)
    parser.add_argument('-file', '--file-name', help='path to a text file to process', required=True)
    args = parser.parse_args()
    return parser, args


def convert():
    """Main function for executing script"""
    parser, args = create_parser()
    try:
        indent_conv = IndentConverter(
            file_name=args.file_name,
            convert_from=args.from_,
            space_count=args.tab_chars,
            replace=args.replace)
        modified_text = indent_conv.replace_leading_whitespace()
        if modified_text:
            indent_conv.write_to_file(modified_text=modified_text)
    except FileNotFoundError as err:
        print(err)
