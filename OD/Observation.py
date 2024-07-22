import numpy as np
from astroquery.jplhorizons import Horizons


class Observation:
    def __init__(self, right_asc: np.float64, dec: np.float64, time: np.float64, object: str = None) -> None:
        """
        Initializes the observation object with the specificed parameters

        :param  right_asc: right ascension of observation [rad]
        :param dec: declination of observation [rad]
        :param time: time of observation [JD]
        """
        self.right_asc = right_asc
        self.dec = dec
        self.time = time
        self.rho_hat = np.array([np.cos(dec)*np.cos(right_asc), np.cos(dec)*np.sin(right_asc), np.sin(dec)])

        sun_vecs = Horizons(id='@sun', location='500', epochs=time).vectors(refplane="earth")
        self.sun_vector = np.array([float(sun_vecs["x"]), float(sun_vecs["y"]), float(sun_vecs["z"])], dtype=np.float64)

    def get_rho_hat(self) -> np.ndarray:
        """
        Returns the unit vector originating at the center of the earth pointing towards the observed object
        """
        return self.rho_hat
    
    def get_sun_vector(self) -> np.ndarray:
        """
        Gets the sun vector from the center of the earth

        """
        return self.sun_vector
    
    def get_time(self) -> np.float64:
        """
        Retruns the time of the observations in Julian date
        """
        return self.time