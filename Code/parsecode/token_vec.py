import javalang

class TokenV:
    """Generate the tokens list of a JAVA source file.
    """
    def __init__(self, filepath : str) -> None:
        self.filecontent = self.__read_file(filepath)
        self.__nodecategories = (
            # 1.method invocations and class instance creations
            (javalang.tree.MethodInvocation, javalang.tree.ClassCreator),
            # 2.declaration nodes
            (javalang.tree.MethodDeclaration, javalang.tree.EnumDeclaration, javalang.tree.TypeDeclaration),
            # 3.control flow nodes
            (javalang.tree.IfStatement, javalang.tree.WhileStatement, javalang.tree.ForStatement, javalang.tree.ForControl, javalang.tree.TryStatement, javalang.tree.CatchClause, javalang.tree.ThrowStatement)
        )

    def __read_file(self, filepath : str) -> str:
        with open(filepath, 'r') as f:
            return f.read()

    def getTV(self) -> list:
        """Get tokens from ASTs of the one source file.

        Returns:
            list: Return tokens list.
        """
        tree = javalang.parse.parse(self.filecontent)
        tokenslist = []
        for _, node in tree:
            if isinstance(node, self.__nodecategories[0]):
                if hasattr(node, 'member'):
                    tokenslist.append((node.member, node.__class__.__name__))
                else:
                    tokenslist.append((node.type.name, node.__class__.__name__))
            elif isinstance(node, self.__nodecategories[1]):
                tokenslist.append((node.name, node.__class__.__name__))
            elif isinstance(node, self.__nodecategories[2]):
                tokenslist.append((node.__class__.__name__))
        return tokenslist
