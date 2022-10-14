class NoiseHandle:
    def __init__(self) -> None:
        pass
    
    def __remove_list_item(self, tkslist : list, item : str) -> list:
        itemlist = item.split('=')
        for tks in tkslist:
            for tk in tks:
                if tk[0] == itemlist[0] and tk[1] == itemlist[1]:
                    tks.remove(tk)
        return tkslist

    def remove_infrequent_tks(self, files_tks : list) -> list:
        """Remove the infrequent tokens that the total number of occurrences
        is less than three

        Returns:
            list: Return the infrequent tokens.
        """
        tokens_count = dict()
        for tks in files_tks:
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
            files_tks = self.__remove_list_item(files_tks, tk)
        return files_tks