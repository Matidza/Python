from hello import square
# Using Assert
def main():
    test_square()
def test_square():

        assert square(2) == 4

        print("2 square was not 4")    

        assert square(3) == 9

        assert square(0) == 0

        assert square(-2) == 4
 
        assert square(-3) == 9

