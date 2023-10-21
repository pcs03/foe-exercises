from constants import Atmosphere, Earth


def get_temp(height: float) -> float:
    """
    Returns the temperature at a height in meter [°K]
    """

    temp_at_height_k = Atmosphere.Sealevel.temp - Atmosphere.lapse_rate * height

    return temp_at_height_k


def get_pressure(temp: float) -> float:
    """
    Returns the pressure at a given atmospheric temperature in Kelvin [Pa]
    """

    pressure_at_temp = Atmosphere.Sealevel.pressure * (temp / Atmosphere.Sealevel.temp) ** (
        Earth.gravity / (Atmosphere.lapse_rate * Atmosphere.r_air)
    )

    return pressure_at_temp


def get_density(height: float) -> float:
    """
    Returns the pressure at a given height in meter [kg / m^3]
    """

    temp_at_height = get_temp(height)
    pressure_at_height = get_pressure(temp_at_height)
    density_at_height = pressure_at_height / (Atmosphere.r_air * temp_at_height)

    return density_at_height
