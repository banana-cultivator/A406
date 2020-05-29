
def fizz_buzz(length):
    '''
    fizz_buzz takes in an integer, length
    It returns a list of strings that is 'length' strings long
    For the each entry in the returned list: 
        - if the index is a multiple of three, the list element will be 'Fizz'
        - if the index is a multiple of five, the list element will be 'Buzz'
        - if the index is a multiple of both three and five, the list element will be 'FizzBuzz'
        - otherwise, the list element will be a string of the value of the index
    '''
 
    return   [
            "FizzBuzz" * (i % 5 == 0 and i % 3 == 0)
            or "Buzz" * (i % 5 == 0)
            or "Fizz" * (i % 3 == 0)
            or str(i)
            for i in range(length)
        ]

