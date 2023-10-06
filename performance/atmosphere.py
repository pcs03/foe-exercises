from constants import Atmosphere, Earth


def get_temp_at_height(height_m: float) -> float:
    """
    Returns the temperature at a height in ft [°K]
    """

    temp_at_height_k = Atmosphere.Sealevel.temp - Atmosphere.lapse_rate * height_m

    return temp_at_height_k


def get_pressure_at_temp(temp_k: float) -> float:
    """
    Returns the pressure at a given atmospheric temperature [Pa]
    """

    pressure_at_temp = Atmosphere.Sealevel.pressure * (temp_k / Atmosphere.Sealevel.temp) ** (
        Earth.gravity / (Atmosphere.lapse_rate * Atmosphere.r_air)
    )

    return pressure_at_temp


def get_density_at_height(height_m: float) -> float:
    """
    Returns the pressure at a given height in ft [kg / m^3]
    """

    temp_at_height = get_temp_at_height(height_m)
    pressure_at_height = get_pressure_at_temp(temp_at_height)
    density_at_height = pressure_at_height / (Atmosphere.r_air * temp_at_height)

    return density_at_height
