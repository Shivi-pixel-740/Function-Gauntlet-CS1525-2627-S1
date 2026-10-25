def is_even(number:int)->bool:
    """ Return True if number is even and False if it is odd.

    :param number: integer to check
    :return: True if even, False if odd
    """
    return number %2 == 0


def count_vowels(text:str)->int:
    """Count how many vowels (a, e, i, o, u) are in text.
    Uppercase and lowercase vowels should both count.

    :param text: the string to check
    :return:number of vowels in the text
    """
    count = 0
    for letter in text:
        if letter.lower () in 'aeiou':
            count += 1
    return count


def celsius_to_fahrenheit(celsius:float)->float:
    """Convert a Celsius temperature to Fahrenheit.

    :param celsius:temperature in Celsius
    :return:Fahrenheit
    """
    return (celsius * 9 / 5) + 32


def reverse_text(text:str)->str:
    """Return the characters in text in reverse order.

    Example:
        "robot" becomes "tobor"

    :param text:the string to reverse
    :return: the text is in return order
    """
    return text[::-1]


def larger_number(a: int, b:int) -> int:
    """Return whichever of the two integers is larger.
    If they are equal, return either value.

    :param a:the first integer
    :param b:second integer
    :return:last integer
    """
    if a > b:
        return a
    else:
        return b


def average_two(a: int, b: int) -> float:
    """Calculate and return the average of two integers.

    :param a: first integer
    :param b:last integer
    :return: average of the two integers
    """
    return (a + b) / 2


def can_afford(balance: float, cost: float)->bool:
    """Return True if balance is greater than or equal to cost.
    Otherwise, return False.

    :param balance:amount of money available
    :param cost:amount of money needed
    :return:True if balance covers the cost, else False
    """
    return balance >=cost


def repeat_text(text: str, times: int) ->str:
    """Return one string containing text repeated the given
    number of times.

    Example:
        repeat_text("Go!", 3) returns "Go!Go!Go!"

    :param text: string to repeat
    :param times:number of repetitions
    :return:repeated string
    """
    return text*times


def contains_word(sentence: str, word: str) -> bool:
    """Return True if word appears somewhere inside sentence.
    Otherwise, return False.

    :param sentence:sentence to check
    :param word: word to search for
    :return: True if found, false else
    """
    return word in sentence


def calculate_tip(cost: float, percent: float)->float:
    """Calculate and return the amount of tip.

    Example:
        A cost of 20.0 and percent of 15 returns 3.0.

    :param cost:cost of the meal
    :param percent: tip percentage
    :return:amount of money for tip
    """
    return cost * percent/100


def make_initials(first_name: str, last_name: str) -> str:
    """Return the uppercase first letters of the two names.

    Example:
        "Ada" and "Lovelace" returns "AL".

    :param first_name:person's first name
    :param last_name:person's last name
    :return: two intials in uppercase
    """
    initials = first_name[0].upper() + last_name[0].upper()
    return initials


def percent_score(points: float , possible: float)->float | None:
    """Calculate what percentage of the possible points
    were earned. Return None if possible is less than 1.

    Example:
        18 out of 20 returns 90.0.

    :param points: points earned
    :param possible: total possible points
    :return: percentage score
    """
    return points * 100 / possible


def is_between(number: float, minimum: float, maximum: float) -> bool:
    """Return True if number is between minimum and maximum,
    including the minimum and maximum values.

    :param number:number to check
    :param minimum:lowest allowed number
    :param maximum: high allowed number
    :return:True if number is between minimum and maximum, else False
    """
    return minimum <= number <= maximum


def all_different(a: str, b: str, c: str)->bool:
    """Check if three strings are different.
    Return True if all three strings are different.
    Otherwise,return False.

    :param a:first string
    :param b:second string
    :param c:thrid string
    :return:True if they all are different, else False
    """
    if a == b or  a == c or a == b:
        return False
    else:
        return True


def average_three(a: float, b: float, c: float)->float:
    """Calculate and return the average of three integers.

    :param a:first number
    :param b:second number
    :param c:third number
    :return: 3 integers average
    """
    return (a + b + c)/3


def describe_temperature(temperature: float, cold_limit: float, hot_limit: float)->str:
    """Returns a string describing the temperature.
    Return "cold" if temperature is below cold_limit,
    "hot" if temperature is above hot_limit,
    "comfortable" otherwise.

    :param temperature:temperature to check
    :param cold_limit:temperature below cold_limit
    :param hot_limit:temperature above hot_limit
    :return:'cold', 'hot' or 'comfortable'
    """
    if temperature < cold_limit:
        return "cold"
    elif temperature > hot_limit:
        return "hot"
    else:
        return "comfortable"


if __name__ == "__main__":
    """
    If you want to test any of your code manually
    you can place function calls down here.
    Additionally, there is a test file loaded into
    this folder that you can run a test on your code.
    """


