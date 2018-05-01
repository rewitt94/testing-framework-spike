from expect import Expect

def test_fail():
    return Expect(1).to_equal(2)
