from os import path, getcwd
import sys
sys.path.append(path.join(getcwd(), 'Code'))
from parsecode.token_vec import TokenV

class FileTokens:
    """Generate the tokens vectors for the AST from the source file.
    """
    def __init__(self, filepath : str) -> None:
        self.filepath = filepath
        self.tokens = []

    def __get_filecontent(self) -> str:
        try:
            with open(self.filepath, 'r') as f:
                return f.read()
        except FileNotFoundError as _:
            return None

    def get_file_tokens(self) -> list:
        """Get tokens vectors from AST.

        Returns:
            list: Return tokens list.
        """
        filecontent = self.__get_filecontent()
        if filecontent == None:
            return []
        tokenvs = TokenV(self.filepath)
        return tokenvs.getTV()
