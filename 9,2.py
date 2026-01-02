def difference(*args):
    """
    Знаходить різницю між максимумом і мінімумом серед переданих аргументів.
    """
    if not args:
        return 0

    result = max(args) - min(args)

    return round(result, 2)


if __name__ == "__main__":
    print(difference(1, 2, 3))  # 3 - 1 = 2
    print(difference(5, -5))  # 5 - (-5) = 10
    print(difference(10.2, -2.2, 0, 1.1, 0.5))  # 10.2 - (-2.2) = 12.4
    print(difference())  # 0

    print(difference(3.33, 1.11))  # 2.22