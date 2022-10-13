from os import path, getcwd
from pandas import read_csv

def read_promise_data(filename : str, minrow : int, maxrow : int, collist : list) -> list:
    """Read the csv file which contains Promise data

    Args:
        filename (str): The file which contains Promise Data.
        minrow (int): The min row line of promise data file.
        maxrow (int): The max row line of promise data file.
        collist (list): The need column list.

    Returns:
        list: The file name and label of bug.
    """
    assert minrow >= 0 and minrow < maxrow, "the range of table is error!"
    filepath = path.join(getcwd(), 'Data', filename)
    df = read_csv(filepath, usecols=collist)
    ans = df.loc[minrow : maxrow].values.tolist()
    for val in ans:
        val[1] = True if val[1] > 0 else False
    return ans

def get_code_file_path(relativepath : str, classname : str) -> str:
    filepath = path.join(getcwd(), 'Data', relativepath)
    

if __name__ == '__main__':
    filebug = read_promise_data('tomcat.csv', 0, 857, [2, 23])
    for i in filebug:
        print(get_code_file_path(path.join('tomcat', 'java'), i[0]))
        break
