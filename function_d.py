def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    ascending_numbers = sorted(numbers)
    return ascending_numbers[-1]
    


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
