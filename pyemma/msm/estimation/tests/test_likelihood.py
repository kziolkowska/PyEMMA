import unittest

import numpy as np
from pyemma.util.numeric import assert_allclose
import scipy.sparse

from pyemma.msm.estimation import log_likelihood

"""Unit tests for the transition_matrix module"""

class TestTransitionMatrix(unittest.TestCase):
    
    def setUp(self):
        """Small test cases"""
        self.C1=scipy.sparse.csr_matrix([[1, 3], [3, 1]])
        
        self.T1=scipy.sparse.csr_matrix([[0.8, 0.2], [0.9, 0.1]])
        
        """Zero row sum throws an error"""
        self.T0=scipy.sparse.csr_matrix([[0, 1], [0.9, 0.1]])

    def tearDown(self):
        pass

    def test_count_matrix(self):
        """Small test cases"""
        log=log_likelihood(self.C1, self.T1)
        assert_allclose(log, np.log(0.8*0.2**3*0.9**3*0.1))        
        
        
if __name__=="__main__":
    unittest.main()
