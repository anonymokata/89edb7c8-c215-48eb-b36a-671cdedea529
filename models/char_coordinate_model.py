class CharCoordinateModel(object):
    def __init__(self, c='', row=0, col=0):
        self.__c = c
        self.__row = row
        self.__col = col

    def get_c(self):
        return self.__c

    def get_row(self):
        return self.__row

    def get_col(self):
        return self.__col

    def get_y(self):
        return self.get_row()

    def get_x(self):
        return self.get_col()

    def __str__(self):
        return "(%d,%d) %s" % (self.get_row(), self.get_col(), self.get_c())

#
# end of script
#
