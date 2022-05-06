class Flow:

    class SUM:
        X=5

    class DIV:
        y=10

    class SUB:
        def test(self):
            print(Flow.DIV.y)


o=Flow.SUB()
o.test()