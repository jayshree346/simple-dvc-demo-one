import pytest

class NotInRange(Exception):
    def __init__(self,message="value not in range"):
        # self.input_ = input_
        self.message = message
        super().__init__(self.message)



def test_genric():
    a = 5
    with pytest.raises(NotInRange):
        if a not in range(10,20):
            raise NotInRange
    # assert a == b

def test_something():
    a = 2
    b = 2
    assert True