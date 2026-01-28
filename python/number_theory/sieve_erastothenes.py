def sieve_erastothenes(until_number):
    numbers = list(range(1, until_number + 1))
    numbers.remove(1)
    for firstIndex in numbers[:]:
        for secondIndex in numbers[:]:
            if secondIndex != firstIndex and secondIndex % firstIndex == 0:
                numbers.remove(secondIndex)
    print(numbers)


if __name__ == '__main__':
    sieve_erastothenes(10)
