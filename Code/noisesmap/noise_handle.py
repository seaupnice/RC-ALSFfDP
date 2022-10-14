class NoiseHandle:
    def __init__(self, files_tks : list) -> None:
        """Handling Noise module

        Args:
            files_tks (list): Tokens vectors from AST
        """
        self.tkslist = files_tks
    
    def __remove_list_item(self, item : str) -> list:
        itemlist = item.split('=')
        for tks in self.tkslist:
            for tk in tks:
                if tk[0] == itemlist[0] and tk[1] == itemlist[1]:
                    tks.remove(tk)
        return self.tkslist

    def remove_infrequent_tks(self):
        """Remove the infrequent tokens that the total number of occurrences
        is less than three

        Returns:
            list: Return the infrequent tokens.
        """
        tokens_count = dict()
        for tks in self.tkslist:
            for tk in tks:
                newkey = tk[0] + '=' + tk[1]
                if newkey in tokens_count:
                    tokens_count[newkey] += 1
                else:
                    tokens_count[newkey] = 1
        for tk in list(tokens_count.keys()):
            if tokens_count[tk] >= 3:
                del tokens_count[tk]
        for tk in list(tokens_count.keys()):
            self.tkslist = self.__remove_list_item(tk)