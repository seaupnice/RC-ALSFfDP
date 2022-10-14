class MapTokens:
    def __init__(self, tokenslist : list) -> None:
        """Build a mapping between integers and tokens, and encode token vectors to integer vectors.
        Since our integer vectors may have different lengths, we append 0 to the integer vectors 
        to make all the lengths consistent and equal to the length of the longest vector.

        Args:
            tokenslist (list): _description_
        """
        self.tokens_vecs = tokenslist
        self.numerical_vecs = [] # numerical vectors: one-to-one correspondence tokens_vec
        self.map_length = 0
        self.token_map = [] # sorted token vectors
    
    def __get_map(self) -> None:
        """Get Map length and sort tokens list.
        """
        tokenset = set()
        for tks in self.tokens_vecs:
            for tk in tks:
                tokenset.add(tk[0] + '=' + tk[1])
        self.token_map = list(tokenset)
        self.map_length = len(self.token_map)
        self.token_map.sort()

    def get_num_vec(self) -> None:
        """Get numerical vectors.
        """
        self.__get_map()
        for tks in self.tokens_vecs:
            num_vec = []
            for tk in tks:
                flag = tk[0] + '=' + tk[1]
                num_vec.append(self.token_map.index(flag))
            num_vec.extend([0] * (self.map_length - len(num_vec)))
            self.numerical_vecs.append(num_vec)
