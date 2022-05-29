class Dir02:
    """This is the module for studying Packaging of Python."""
    #コンストラクタ
    def __init__(self):
        self.name = ""

    #getNameメソッド
    def getName(self):
        return "Dir02:" + self.name

    #setNameメソッド
    def setName(self, name):
        self.name = name
