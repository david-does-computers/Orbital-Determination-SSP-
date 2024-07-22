import numpy as np
from Observation import Observation
from OrbitDetermination import OrbitDetermination
from GaussMethod import GaussMethod

class MonteCarlo:
    def __init__(self, RA: np.ndarray[np.float64], DEC: np.ndarray[np.float64], time: np.ndarray[np.float64], sigma_RA: np.ndarray[np.float64], sigma_DEC: np.ndarray[np.float64]):
        self.RA = RA
        self.DEC = DEC
        self.time = time
        self.sigma_RA = sigma_RA
        self.sigma_DEC = sigma_DEC

    def iterative_error_calculation(self, n):
        elements = np.zeros((n, 6))
        counter = 0
        for i in range(n):
            gauss_run = GaussMethod((
                Observation(self._random_RA(0), self._random_DEC(0), self.time[0]),
                Observation(self._random_RA(1), self._random_DEC(1), self.time[1]),
                Observation(self._random_RA(2), self._random_DEC(2), self.time[2])
            ))
            gauss_run.iterative_honing()
            elements[i] = OrbitDetermination(*gauss_run.get_ecplitic_vectors(), gauss_run.corrected_times[1]).get_orbital_elements()
            counter += 1
            print(f"{counter} done out of {n}")
        

        return elements
                
            
    
    def _random_RA(self, index: np.int8):
        return np.random.normal(self.RA[index], self.sigma_RA[index])
    
    def _random_DEC(self, index: np.int8):
        return np.random.normal(self.DEC[index], self.sigma_DEC[index])
