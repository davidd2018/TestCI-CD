from sum import sum
    

def test_sum_basic():
    return sum(5, 3) == 8

if(test_sum_basic() == True):
    print("Test passed")
else:
    print("fail")