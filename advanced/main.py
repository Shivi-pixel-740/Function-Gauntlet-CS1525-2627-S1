def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def is_between(number: float, minimum: float, maximum: float) -> bool:
    """Check whether a number is within a range."""
    return minimum <= number <= maximum

def calculate_tip(cost: float, percent: float) -> float:
    """Calculate the tip amount."""
    return cost * percent / 100

def make_initials(first_name: str, last_name: str) -> str:
    """Create initials from a first and last name."""
    return first_name[0].upper() + last_name[0].upper()


def average_three(a: float, b: float, c: float) -> float:
    """Calculate the average of three numbers."""
    return (a + b + c) / 3

def temperature_in_safe_range(
    celsius: float,
    minimum_f: float,
    maximum_f: float
) -> bool:
    """Check whether a Celsius temperature is within a safe Fahrenheit range.
    :param celsius: The temperature in Celsius.
    :param minimum_f: The minimum safe temperature in Fahrenheit.
    :param maximum_f: The maximum safe temperature in Fahrenheit.
    :return: True if the converted temperature is within the range, otherwise False.
    """
    fahrenheit = celsius_to_fahrenheit(celsius)
    return is_between(fahrenheit, minimum_f, maximum_f)


def can_afford_with_tip(
    balance: float,
    cost: float,
    tip_percent: float
) -> bool:
    """Check whether the balance covers the cost and tip.
    :param balance: The amount of money available.
    :param cost: The original cost.
    :param tip_percent: The tip percentage.
    :return: True if the balance is enough, otherwise False.
    """
    tip = calculate_tip(cost, tip_percent)
    total = cost + tip
    return balance >= total


def meets_average(
    score1: float,
    score2: float,
    score3: float,
    required_average: float
) -> bool:
    """Check whether three scores meet the required average.
    :param score1: The first score.
    :param score2: The second score.
    :param score3: The third score.
    :param required_average: The minimum average needed.
    :return: True if the average meets the requirement, otherwise False.
    """
    average = average_three(score1, score2, score3)
    return average >= required_average


def initials_match(
    first_name: str,
    last_name: str,
    expected_initials: str
) -> bool:
    """Check whether the initials match, ignoring uppercase and lowercase.
    :param first_name: The person's first name.
    :param last_name: The person's last name.
    :param expected_initials: The initials to compare against.
    :return: True if the initials match, otherwise False.
    """
    initials = make_initials(first_name, last_name)
    return initials.lower() == expected_initials.lower()

if __name__ == "__main__":
    print(temperature_in_safe_range(20, 60, 75))  # True
    print(temperature_in_safe_range(0, 60, 75))   # False

    print(can_afford_with_tip(30, 25, 20))  # True
    print(can_afford_with_tip(25, 25, 20))  # False

    print(meets_average(80, 90, 70, 80))  # True
    print(meets_average(50, 60, 70, 80))  # False

    print(initials_match("John", "Doe", "JD"))  # True
    print(initials_match("John", "Doe", "AB"))  # False