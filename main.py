def calculate_required_energy(
    average_power_w: float,
    operating_time_h: float,
    efficiency_fraction: float,
) -> dict:
    return {
        "required_energy_kwh": (
            average_power_w * operating_time_h / efficiency_fraction / 1000
        )
    }
