from os import path, getcwd
import sys
sys.path.append(path.join(getcwd(), 'Code'))

from noisesmap.utils import read_promise_data, get_code_file_path
from noisesmap.file_tokens import FileTokens
from noisesmap.noise_handle import NoiseHandle
from noisesmap.map_tokens import MapTokens

if __name__ == '__main__':
    filebug = read_promise_data('tomcat.csv', 0, 857, [2, 23])
    tkslist = []
    for i in filebug:
        try:
            filepath = get_code_file_path(path.join('tomcat', 'java'), i[0])
            with open(filepath, 'r') as f:
                tklist = FileTokens(filepath).get_file_tokens()
                if tklist == []:
                    filebug.remove(i)
                else:
                    tkslist.append(tklist)
        except FileNotFoundError as fnf_error:
            ## TODO
            pass
    noisehd = NoiseHandle(tkslist)
    maptk = MapTokens(noisehd.remove_infrequent_tks())
    print(maptk.map_length)
    print(maptk.get_num_vec())