from A import A
from B import B
from C import C
class D(A,B,C):
    def __init__(self):
        print("cons D")

    def methodd(self):
        print("Class D")

d=D()
d.methoda()