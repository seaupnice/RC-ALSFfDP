from os import path, getcwd
import sys
sys.path.append(path.join(getcwd(), 'Code'))

from noisesmap.utils import read_promise_data, get_code_file_path
from noisesmap.files_tokens import FileTokens

if __name__ == '__main__':
    filebug = read_promise_data('tomcat.csv', 0, 857, [2, 23])
    for i in filebug:
        try:
            filepath = get_code_file_path(path.join('tomcat', 'java'), i[0])
            with open(filepath, 'r') as f:
                f.read()
                break
        except FileNotFoundError as fnf_error:
            ## TODO
            pass
    print(filepath)
    filetks = FileTokens(filepath).get_file_tokens()
    for i in filetks:
        print(i)