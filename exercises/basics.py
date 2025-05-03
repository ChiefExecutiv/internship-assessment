from typing import List


def collatz(n: int) -> List[int]:

    myList = [n]

    while n > 1:			
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        
        myList.append(n)
    
    return myList



def distinct_numbers(numbers: List[int]) -> int:

    return len(set(numbers))

