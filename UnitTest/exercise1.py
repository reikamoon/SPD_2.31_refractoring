def calculate_kinetic_energy(mass, velocity):
    """Returns kinetic energy of mass [kg] with velocity [ms]."""
    return 0.5 * mass * velocity ** 2


def test_calculate_kinetic_energy():
    mass = 10  # [kg]
    velocity = 4  # [m/s]
    assert calculate_kinetic_energy(mass, velocity) == 80


def get_average(list):
    sum = 0
    for num in list:
        sum += num
    mean = sum / len(list)
    return mean


def test_get_average():
    integer_list = [1, 2, 3, 4, 5, 6]
    assert get_average(integer_list) == 3.5
