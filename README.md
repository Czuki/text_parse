# Indenter

Converts indentation in a text file from spaces to tabs or from tabs to spaces

## Usage

Run `python3 -m indenter -h` for help in terminal

Use example with all parameters:

`python3 -m indenter --from=tabs --replace --tab-chars=2 --file-name=file.txt`

`file-name` or `-file` - required, path to a file to convert

`--from` or `-f` - optional, values: 'tabs' or 'spaces' type of indent to convert from, 
if not provided, script will 'guess' indentation type in a file

`--replace` or `-r` - optional flag, if provided, script will replace the original file,
otherwise a new file will be created

`--tab-chars` or `-t` - optional, default is 4, amount of spaces to replace each tab 
