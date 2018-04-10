import freeze

    
class fB:
    #def fizzBuzz(self, n):
    def __init__(self, n):
               
        """
        :type n: int
        :rtype: List[str]
        """
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)

test = fB(15);
#test.fizzBuzz(15);
