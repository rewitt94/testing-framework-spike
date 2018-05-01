from expect import Expect

def test_error():
    return Expect(1).to_equal(2).what
