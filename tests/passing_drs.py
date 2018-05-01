from expect import Expect

def test_pass():
    return Expect(2).to_equal(2)
