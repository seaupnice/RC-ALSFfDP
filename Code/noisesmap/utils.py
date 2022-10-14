from os import path, getcwd
from pandas import read_csv

def read_promise_data(filename : str, minrow : int, maxrow : int, collist : list) -> list:
    """Read the csv file which contains Promise data.

    Args:
        filename (str): The file which contains Promise Data.
        minrow (int): The min row line of promise data file.
        maxrow (int): The max row line of promise data file.
        collist (list): The need column list.

    Returns:
        list: The class name of the file and label of bug.
    """
    assert minrow >= 0 and minrow < maxrow, "the range of table is error!"
    filepath = path.join(getcwd(), 'Data', filename)
    df = read_csv(filepath, usecols=collist)
    ans = df.loc[minrow : maxrow].values.tolist()
    for val in ans:
        val[1] = True if val[1] > 0 else False
    return ans

def get_code_file_path(relativepath : str, classname : str) -> str:
    """Get the file absolute path.

    Args:
        relativepath (str): The relative path to the project path.
        classname (str): The class name from promise data.

    Returns:
        str: The absolute path of file.
    """
    filepath = path.join(getcwd(), 'Data', relativepath)
    namelist = classname.split('.')
    for i in namelist:
        filepath = path.join(filepath, i)
    return filepath + '.java'
