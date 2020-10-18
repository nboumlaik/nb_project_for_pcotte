import matplotlib.pyplot as plt


class Complex:
    """
    A class for complex numbers.
    """
    def __init__(self, preel: int, pimag: int):
        """ Initialisation of the class"""
        self.pimag = pimag
        self.preel = preel
        self.res_preel = None
        self.res_pimag = None

    def __str__(self) -> str:
        """
        The print of the class
        Returns
        -------
        Str
        """
        sign = "+"
        if self.pimag > 0:
            sign = '+'
        elif self.pimag < 0:
            sign = '-'
        if self.pimag == 0:
            return str(self.preel)
        else:
            return f'{self.preel} {sign} {abs(self.pimag)}i'


class ComplexOper(Complex):
    """
    A very simple class for Complex numbers operations.
    """
    def __add__(self, nb_comp: Complex) -> Complex:
        """
        Addition of two complex number
        Parameters
        ----------
        nb_comp: A complex number

        Returns
        -------
        A complex number
        """
        preel_res = self.preel + nb_comp.preel
        pimag_res = self.pimag + nb_comp.pimag
        res = Complex(preel_res, pimag_res)
        return res

    def __mul__(self, nb_comp: Complex) -> Complex:
        """
        Multiplication of two complex number
        Parameters
        ----------
        nb_comp: A complex number

        Returns
        -------
        A complex number
        """
        preel_res = self.preel * nb_comp.preel - self.pimag * nb_comp.pimag
        pimag_res = self.preel * nb_comp.pimag + nb_comp.preel * self.pimag
        res = Complex(preel_res, pimag_res)
        return res

    def __truediv__(self, nb_comp: Complex) -> Complex:
        """
        Division of two complex number
        Parameters
        ----------
        nb_comp: A complex number

        Returns
        -------
        A complex number
        """
        nb_temp = nb_comp
        nb_temp.pimag = - nb_temp.pimag
        res_1 = self * nb_temp
        denom = nb_comp.preel**2 + nb_comp.pimag**2
        preel_res = round(res_1.preel / denom, 4)
        pimag_res = round(res_1.pimag / denom, 4)
        res = Complex(preel_res, pimag_res)
        return res

    def plot(self) -> plt.figure:
        """
        Figure of a complex number
        Returns
        -------
        figure object
        """
        return plt.plot(self.preel, self.pimag, 'b.')

    def __str__(self) -> str:
        """
        The print of the class
        Returns
        -------
        Str
        """
        sign = "+"
        if self.pimag > 0:
            sign = '+'
        elif self.pimag < 0:
            sign = '-'
        if self.pimag == 0:
            return str(self.preel)
        else:
            return f'{self.preel} {sign} {abs(self.pimag)}i'
