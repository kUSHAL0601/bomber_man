# CREATED BY MajAK


class Person():
    def __init__(self, xcord, ycord, typ):
        self.xc = xcord
        self.yc = ycord
        self.typ = typ

    def move_right(self):
        pass

    def move_left(self):
        pass

    def move_up(self):
        pass

    def move_down(self):
        pass

    def get_xc(self):
        return self.xc

    def get_yc(self):
        return self.yc

    def update_xc(self, newxc):
        self.xc = newxc

    def update_yc(self, newyc):
        self.yc = newyc
