"""
List of conversion factors for units commonly used in aviation related calculations

source: https://www.unitconverters.net/common-converters.html
"""


from numpy import isin


class Distance:
    """
    SI-Unit: meter [m]
    """

    __mm_factor = 0.001
    __dm_factor = 0.01
    __cm_factor = 0.1
    __km_factor = 1000
    __mile_factor = 1609.34
    __n_mile_factor = 1852
    __yard_factor = 0.9144
    __ft_factor = 0.3048
    __inch_factor = 0.0254

    def __init__(self, m):
        self.m = m

    @classmethod
    def Mm(cls, mm):
        return cls(mm * cls.__mm_factor)

    @property
    def mm(self):
        return self.m / self.__mm_factor

    @classmethod
    def Dm(cls, dm):
        return cls(dm * cls.__dm_factor)

    @property
    def dm(self):
        return self.m / self.__dm_factor

    @classmethod
    def Cm(cls, cm):
        return cls(cm * cls.__cm_factor)

    @property
    def cm(self):
        return self.m / self.__cm_factor

    @classmethod
    def Km(cls, km):
        return cls(km * cls.__km_factor)

    @property
    def km(self):
        return self.m / self.__km_factor

    @classmethod
    def Mile(cls, mile):
        return cls(mile * cls.__mile_factor)

    @property
    def mile(self):
        return self.m / self.__mile_factor

    @classmethod
    def N_mile(cls, n_mile):
        return cls(n_mile * cls.__n_mile_factor)

    @property
    def n_mile(self):
        return self.m / self.__n_mile_factor

    @classmethod
    def Yard(cls, yard):
        return cls(yard * cls.__yard_factor)

    @property
    def yard(self):
        return self.m / self.__yard_factor

    @classmethod
    def Ft(cls, ft):
        return cls(ft * cls.__ft_factor)

    @property
    def ft(self):
        return self.m / self.__ft_factor

    @classmethod
    def Inch(cls, inch):
        return cls(inch * cls.__inch_factor)

    @property
    def inch(self):
        return self.inch / self.__inch_factor

    def __str__(self):
        return f"{self.m:.2f} meters"

    def __mul__(self, x):
        if isinstance(x, Distance):
            return self.m * x.m
        else:
            return self.m * x

    def __rmul__(self, x):
        return self * x

    def __truediv__(self, x):
        if isinstance(x, Distance):
            return self.m / x.m
        else:
            return self.m / x

    def __rtruediv__(self, x):
        return x / self.m

    def __add__(self, x):
        if isinstance(x, Distance):
            return self.m + x.m
        else:
            return self.m + x

    def __radd__(self, x):
        return self.m + x

    def __sub__(self, x):
        if isinstance(x, Distance):
            return self.m - x.m
        else:
            return self.m - x

    def __rsub__(self, x):
        return x - self.m


class Mass:
    """
    SI-Unit: kilogram [kg]
    """

    __lbs_factor = 0.453592
    __gram_factor = 0.001
    __m_ton_factor = 1000
    __uk_ton_factor = 1016.0469
    __us_ton_factor = 907.18474

    def __init__(self, kg):
        self.kg = kg

    @classmethod
    def Lbs(cls, lbs):
        return cls(lbs * cls.__lbs_factor)

    @property
    def lbs(self):
        return self.kg / self.__lbs_factor

    @classmethod
    def Gram(cls, gram):
        return cls(gram * cls.__gram_factor)

    @property
    def gram(self):
        return self.kg / self.__gram_factor

    @classmethod
    def M_ton(cls, m_ton):
        return cls(m_ton * cls.__m_ton_factor)

    @property
    def m_ton(self):
        return self.kg / self.__m_ton_factor

    @classmethod
    def Uk_ton(cls, uk_ton):
        return cls(uk_ton * cls.__uk_ton_factor)

    @property
    def uk_ton(self):
        return self.kg / self.__m_ton_factor

    @classmethod
    def Us_ton(cls, us_ton):
        return cls(us_ton * cls.__us_ton_factor)

    @property
    def us_ton(self):
        return self.kg / self.__us_ton_factor

    def __str__(self):
        return f"{self.kg:.2f} kilograms"

    def __mul__(self, x):
        if isinstance(x, Mass):
            return self.kg * x.kg
        else:
            return self.kg * x

    def __rmul__(self, x):
        return self * x

    def __truediv__(self, x):
        if isinstance(x, Mass):
            return self.kg / x.kg
        else:
            return self.kg / x

    def __rtruediv__(self, x):
        return x / self.kg

    def __add__(self, x):
        if isinstance(x, Mass):
            return self.kg + x.kg
        else:
            return self.kg + x

    def __radd__(self, x):
        return self.kg + x

    def __sub__(self, x):
        if isinstance(x, Mass):
            return self.kg - x.kg
        else:
            return self.kg - x

    def __rsub__(self, x):
        return x - self.kg


class Time:
    """
    SI-Unit: second [s]
    """

    __min_factor = 60
    __hour_factor = 3600
    __day_factor = 86400
    __year_factor = 31557600

    def __init__(self, s):
        self.s = s

    @classmethod
    def Min(cls, min):
        return cls(min * cls.__min_factor)

    @property
    def min(self):
        return self.s / self.__min_factor

    @classmethod
    def Hour(cls, hour):
        return cls(hour * cls.__hour_factor)

    @property
    def hour(self):
        return self.s / self.__hour_factor

    @classmethod
    def Day(cls, day):
        return cls(day * cls.__day_factor)

    @property
    def day(self):
        return self.s / self.__day_factor

    @classmethod
    def Year(cls, year):
        return cls(year * cls.__year_factor)

    @property
    def year(self):
        return self.s / self.__year_factor

    def __str__(self):
        return f"{self.s:.2f} seconds"

    def __mul__(self, x):
        if isinstance(x, Time):
            return self.s * x.s
        else:
            return self.s * x

    def __rmul__(self, x):
        return self * x

    def __truediv__(self, x):
        if isinstance(x, Time):
            return self.s / x.s
        else:
            return self.s / x

    def __rtruediv__(self, x):
        return x / self.s

    def __add__(self, x):
        if isinstance(x, Time):
            return self.s + x.s
        else:
            return self.s + x

    def __radd__(self, x):
        return self.s + x

    def __sub__(self, x):
        if isinstance(x, Time):
            return self.s - x.s
        else:
            return self.s - x

    def __rsub__(self, x):
        return x - self.s


class Temperature:
    """
    SI-Unit: kelvin [K]
    """

    __celsius_factor = 273.15

    def __init__(self, kelvin):
        self.kelvin = kelvin

    @classmethod
    def Celsius(cls, celsius):
        return cls(celsius + cls.__celsius_factor)

    @property
    def celsius(self):
        return self.kelvin - self.__celsius_factor

    @classmethod
    def Fahrenheit(cls, fahrenheit):
        return cls((fahrenheit - 32) * 5 / 9 + cls.__celsius_factor)

    @property
    def fahrenheit(self):
        return (self.kelvin - self.__celsius_factor) * 9 / 5 + 32

    def __str__(self):
        return f"{self.kelvin:.2f} K"

    def __mul__(self, x):
        if isinstance(x, Temperature):
            return self.kelvin * x.kelvin
        else:
            return self.kelvin * x

    def __rmul__(self, x):
        return self * x

    def __truediv__(self, x):
        if isinstance(x, Temperature):
            return self.kelvin / x.kelvin
        else:
            return self.kelvin / x

    def __rtruediv__(self, x):
        return x / self.kelvin

    def __add__(self, x):
        if isinstance(x, Temperature):
            return self.kelvin + x.kelvin
        else:
            return self.kelvin + x

    def __radd__(self, x):
        return self.kelvin + x

    def __sub__(self, x):
        if isinstance(x, Temperature):
            return self.kelvin - x.kelvin
        else:
            return self.kelvin - x

    def __rsub__(self, x):
        return x - self.kelvin


class Velocity:
    """
    SI-Unit: meter / second [m/s]
    """

    __kts_factor = 0.5144444444
    __km_p_h_factor = 0.2777777778
    __ft_p_m_factor = 0.00508
    __ft_p_s_factor = 0.3048
    __yd_p_s_factor = 0.9144
    __yd_p_m_factor = 0.01524
    __m_p_m_factor = 0.0166666667
    __mile_p_h_factor = 0.44704

    def __init__(self, m_p_s):
        self.m_p_s = m_p_s

    @classmethod
    def Kts(cls, kts):
        return cls(kts * cls.__kts_factor)

    @property
    def kts(self):
        return self.m_p_s / self.__kts_factor

    @classmethod
    def Km_p_h(cls, km_p_h):
        return cls(km_p_h * cls.__km_p_h_factor)

    @property
    def km_p_h(self):
        return self.m_p_s / self.__km_p_h_factor

    @classmethod
    def Ft_p_m(cls, ft_p_m):
        return cls(ft_p_m * cls.__ft_p_m_factor)

    @property
    def ft_p_m(self):
        return self.m_p_s / self.__ft_p_m_factor

    @classmethod
    def Ft_p_s(cls, ft_p_s):
        return cls(ft_p_s * cls.__ft_p_s_factor)

    @property
    def ft_p_s(self):
        return self.m_p_s / self.__ft_p_s_factor

    @classmethod
    def Yd_p_s(cls, yd_p_s):
        return cls(yd_p_s * cls.__yd_p_s_factor)

    @property
    def yd_p_s(self):
        return self.m_p_s / self.__yd_p_s_factor

    @classmethod
    def Yd_p_m(cls, yd_p_m):
        return cls(yd_p_m * cls.__yd_p_m_factor)

    @property
    def yd_p_m(self):
        return self.m_p_s / self.__yd_p_m_factor

    @classmethod
    def M_p_m(cls, m_p_m):
        return cls(m_p_m * cls.__m_p_m_factor)

    @property
    def m_p_m(self):
        return self.m_p_s / self.__m_p_m_factor

    @classmethod
    def Mile_p_h(cls, mile_p_h):
        return cls(mile_p_h * cls.__mile_p_h_factor)

    @property
    def mile_p_h(self):
        return self.m_p_s / self.__mile_p_h_factor

    def __str__(self):
        return f"{self.m_p_s:.2f} m/s"

    def __mul__(self, x):
        if isinstance(x, Velocity):
            return self.m_p_s * x.m_p_s
        else:
            return self.m_p_s * x

    def __rmul__(self, x):
        return self * x

    def __truediv__(self, x):
        if isinstance(x, Velocity):
            return self.m_p_s / x.m_p_s
        else:
            return self.m_p_s / x

    def __rtruediv__(self, x):
        return x / self.m_p_s

    def __add__(self, x):
        if isinstance(x, Velocity):
            return self.m_p_s + x.m_p_s
        else:
            return self.m_p_s + x

    def __radd__(self, x):
        return self.m_p_s + x

    def __sub__(self, x):
        if isinstance(x, Velocity):
            return self.m_p_s - x.m_p_s
        else:
            return self.m_p_s - x

    def __rsub__(self, x):
        return x - self.m_p_s


class Area:
    """
    SI/Unit: square meter [m^2]
    """

    __km2_factor = 1000000
    __mm2_factor = 0.000001
    __hectare_factor = 10000
    __acre_factor = 4046.8564224
    __yard2_factor = 0.83612736
    __ft2_factor = 0.09290304
    __in2_factor = 0.00064516

    def __init__(self, m2):
        self.m2 = m2

    @classmethod
    def Km2(cls, km2):
        return cls(km2 * cls.__km2_factor)

    @property
    def km2(self):
        return self.m2 / self.__km2_factor

    @classmethod
    def Mm2(cls, mm2):
        return cls(mm2 * cls.__mm2_factor)

    @property
    def mm2(self):
        return self.m2 / self.__mm2_factor

    @classmethod
    def Hectare(cls, hectare):
        return cls(hectare * cls.__hectare_factor)

    @property
    def hectare(self):
        return self.m2 / self.__hectare_factor

    @classmethod
    def Acre(cls, acre):
        return cls(acre * cls.__acre_factor)

    @property
    def acre(self):
        return self.m2 / self.__acre_factor

    @classmethod
    def Yard2(cls, yard2):
        return cls(yard2 * cls.__yard2_factor)

    @property
    def yard2(self):
        return self.m2 / self.__yard2_factor

    @classmethod
    def Ft2(cls, ft2):
        return cls(ft2 * cls.__ft2_factor)

    @property
    def ft2(self):
        return self.m2 / self.__ft2_factor

    @classmethod
    def In2(cls, in2):
        return cls(in2 * cls.__in2_factor)

    @property
    def in2(self):
        return self.m2 / self.__in2_factor

    def __str__(self):
        return f"{self.m2:.2f} m²"

    def __mul__(self, x):
        if isinstance(x, Area):
            self.m2 * x.m2
        else:
            self.m2 * x

    def __rmul__(self, x):
        self * x

    def __truediv__(self, x):
        if isinstance(x, Area):
            self.m2 / x.m2
        else:
            self.m2 / x

    def __rtruediv__(self, x):
        x / self.m2

    def __add__(self, x):
        if isinstance(x, Area):
            self.m2 + x.m2
        else:
            self.m2 + x

    def __radd__(self, x):
        self.m2 + x

    def __sub__(self, x):
        if isinstance(x, Area):
            self.m2 - x.m2
        else:
            self.m2 - x

    def __rsub__(self, x):
        x - self.m2


class Volume:
    """
    SI/Unit: cubic meter [m^3]
    """

    __liter_factor = 0.001
    __mliter_factor = 0.000001
    __gallon_factor = 0.0037854118
    __quart_factor = 0.0009463529
    __yard3_factor = 0.764554858
    __ft3_factor = 0.0283168466
    __in3_factor = 0.0000163871

    def __init__(self, m3):
        self.m3 = m3

    @classmethod
    def Liter(cls, liter):
        return cls(liter * cls.__liter_factor)

    @property
    def liter(self):
        return self.m3 / self.__liter_factor

    @classmethod
    def Mliter(cls, mliter):
        return cls(mliter * cls.__mliter_factor)

    @property
    def mliter(self):
        return self.m3 / self.__mliter_factor

    @classmethod
    def Gallon(cls, gallon):
        return cls(gallon * cls.__gallon_factor)

    @property
    def gallon(self):
        return self.m3 / self.__gallon_factor

    @classmethod
    def Quart(cls, quart):
        return cls(quart * cls.__quart_factor)

    @property
    def quart(self):
        return self.m3 / self.__quart_factor

    @classmethod
    def Yard3(cls, yard3):
        return cls(yard3 * cls.__yard3_factor)

    @property
    def yard3(self):
        return self.m3 / self.__yard3_factor

    @classmethod
    def Ft3(cls, ft3):
        return cls(ft3 * cls.__ft3_factor)

    @property
    def ft3(self):
        return self.m3 / self.__ft3_factor

    @classmethod
    def In3(cls, in3):
        return cls(in3 * cls.__in3_factor)

    @property
    def in3(self):
        return self.m3 / self.__in3_factor

    def __str__(self):
        return f"{self.m3:.2f} m³"

    def __mul__(self, x):
        if isinstance(x, Volume):
            self.m3 * x.m3
        else:
            self.m3 * x

    def __rmul__(self, x):
        self * x

    def __truediv__(self, x):
        if isinstance(x, Volume):
            self.m3 / x.m3
        else:
            self.m3 / x

    def __rtruediv__(self, x):
        x / self.m3

    def __add__(self, x):
        if isinstance(x, Volume):
            self.m3 + x.m3
        else:
            self.m3 + x

    def __radd__(self, x):
        self.m3 + x

    def __sub__(self, x):
        if isinstance(x, Volume):
            self.m3 - x.m3
        else:
            self.m3 - x

    def __rsub__(self, x):
        x - self.m3


class Pressure:
    """
    SI/Unit: pascal [Pa />  N/m^2]
    """

    __gpa_factor = 1000000000
    __mpa_factor = 1000000
    __kpa_factor = 1000
    __hpa_factor = 100
    __bar_factor = 10000
    __atm_factor = 101325
    __psi_factor = 0.0689475729
    __inhg_factor = 3386.38

    def __init__(self, pa):
        self.pa = pa

    @classmethod
    def Gpa(cls, gpa):
        return cls(gpa * cls.__gpa_factor)

    @property
    def gpa(self):
        return self.pa / self.__gpa_factor

    @classmethod
    def Mpa(cls, mpa):
        return cls(mpa * cls.__mpa_factor)

    @property
    def mpa(self):
        return self.pa / self.__mpa_factor

    @classmethod
    def Kpa(cls, kpa):
        return cls(kpa * cls.__kpa_factor)

    @property
    def kpa(self):
        return self.pa / self.__kpa_factor

    @classmethod
    def Hpa(cls, hpa):
        return cls(hpa * cls.__hpa_factor)

    @property
    def hpa(self):
        return self.pa / self.__hpa_factor

    @classmethod
    def Bar(cls, bar):
        return cls(bar * cls.__bar_factor)

    @property
    def bar(self):
        return self.pa / self.__bar_factor

    @classmethod
    def Atm(cls, atm):
        return cls(atm * cls.__atm_factor)

    @property
    def atm(self):
        return self.pa / self.__atm_factor

    @classmethod
    def Psi(cls, psi):
        return cls(psi * cls.__psi_factor)

    @property
    def psi(self):
        return self.pa / self.__psi_factor

    @classmethod
    def Inhg(cls, inhg):
        return cls(inhg * cls.__psi_factor)

    @property
    def inhg(self):
        return self.pa / self.__inhg_factor

    def __str__(self):
        return f"{self.pa:.2f} Pa"

    def __mul__(self, x):
        if isinstance(x, Pressure):
            self.pa * x.pa
        else:
            self.pa * x

    def __rmul__(self, x):
        self * x

    def __truediv__(self, x):
        if isinstance(x, Pressure):
            self.pa / x.pa
        else:
            self.pa / x

    def __rtruediv__(self, x):
        x / self.pa

    def __add__(self, x):
        if isinstance(x, Pressure):
            self.pa + x.pa
        else:
            self.pa + x

    def __radd__(self, x):
        self.pa + x

    def __sub__(self, x):
        if isinstance(x, Pressure):
            self.pa - x.pa
        else:
            self.pa - x

    def __rsub__(self, x):
        x - self.pa


class Force:
    """
    SI/Unit: newton [N /> kg*m/s^2]
    """

    __kn_factor = 1000
    __mn_factor = 1000000
    __kg_factor = 9.80665
    __gram_factor = 0.00980665
    __lbf_factor = 4.4482216153

    def __init__(self, n):
        self.n = n

    @classmethod
    def Kn(cls, kn):
        return cls(kn * cls.__kn_factor)

    @property
    def kn(self):
        return self.n / self.__kn_factor

    @classmethod
    def Mn(cls, mn):
        return cls(mn * cls.__mn_factor)

    @property
    def mn(self):
        return self.n / self.__mn_factor

    @classmethod
    def Kg(cls, kg):
        return cls(kg * cls.__kg_factor)

    @property
    def kg(self):
        return self.n / self.__kg_factor

    @classmethod
    def Gram(cls, gram):
        return cls(gram * cls.__gram_factor)

    @property
    def gram(self):
        return self.n / self.__gram_factor

    @classmethod
    def Lbf(cls, lbf):
        return cls(lbf * cls.__lbf_factor)

    @property
    def lbf(self):
        return self.n / self.__lbf_factor

    def __str__(self):
        return f"{self.n:.2f} Newtons"

    def __mul__(self, x):
        if isinstance(x, Force):
            return self.n * x.n
        else:
            return self.n * x

    def __rmul__(self, x):
        return self * x

    def __truediv__(self, x):
        if isinstance(x, Force):
            return self.n / x.n
        else:
            return self.n / x

    def __rtruediv__(self, x):
        return x / self.n

    def __add__(self, x):
        if isinstance(x, Force):
            return self.n + x.n
        else:
            return self.n + x

    def __radd__(self, x):
        return self.n + x

    def __sub__(self, x):
        if isinstance(x, Force):
            return self.n - x.n
        else:
            return self.n - x

    def __rsub__(self, x):
        return x - self.n


class Power:
    """
    SI/Unit: watt [W /> J/s]
    """

    __kw_factor = 1000
    __mw_factor = 1000000
    __gw_factor = 1000000000
    __hp_metric_factor = 735.49875
    __hp_uk_factor = 745.69987158

    def __init__(self, w):
        self.w = w

    @classmethod
    def Mw(cls, mw):
        return cls(mw * cls.__mw_factor)

    @property
    def mw(self):
        return self.w / self.__mw_factor

    @classmethod
    def Kw(cls, kw):
        return cls(kw * cls.__kw_factor)

    @property
    def kw(self):
        return self.w / self.__kw_factor

    @classmethod
    def Gw(cls, gw):
        return cls(gw * cls.__gw_factor)

    @property
    def gw(self):
        return self.w / self.__gw_factor

    @classmethod
    def Hp_metric(cls, hp_metric):
        return cls(hp_metric * cls.__hp_metric_factor)

    @property
    def hp_metric(self):
        return self.w / self.__hp_metric_factor

    @classmethod
    def Hp_uk(cls, hp_uk):
        return cls(hp_uk * cls.__hp_uk_factor)

    @property
    def hp_uk(self):
        return self.w / self.__hp_uk_factor

    def __str__(self):
        return f"{self.w:.2f} Watts"

    def __mul__(self, x):
        if isinstance(x, Power):
            return self.w * x.w
        else:
            return self.w * x

    def __rmul__(self, x):
        return self * x

    def __truediv__(self, x):
        if isinstance(x, Power):
            return self.w / x.w
        else:
            return self.w / x

    def __rtruediv__(self, x):
        return x / self.w

    def __add__(self, x):
        if isinstance(x, Power):
            return self.w + x.w
        else:
            return self.w + x

    def __radd__(self, x):
        return self.w + x

    def __sub__(self, x):
        if isinstance(x, Power):
            return self.w - x.w
        else:
            return self.w - x

    def __rsub__(self, x):
        return x - self.w
