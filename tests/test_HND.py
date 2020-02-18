import numpy as np
import numpy.testing as npt

import HND

def test_HND_smoke():
    #Smoke test
    obj = HND.HNDobject()
    
def test_HND_fizz():
    #Test the fizz function
    obj = HND.HNDobject()
    output = obj.fizz()
    
    npt.assert_equal(output, "buzz")