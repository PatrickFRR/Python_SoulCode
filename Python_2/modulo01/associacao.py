class Writer():
    def __init__(self, name):
        self.__name = name  # private
        self.__tool = None  # private


    @property
    def name(self):
        return self.__name


    @property
    def tool(self):
        return self.__tool


    @tool.setter
    def tool(self, tool):
        self.__tool = tool

class Pen():
    def __init__(self, brand):
        self.__brand = brand

    @property
    def brand(self):
        return self.__brand

    def write(self):
        print("The pen is writing...")

writer = Writer('Patrick')
pen = Pen('BIC')

writer.tool = pen
writer.tool.write()