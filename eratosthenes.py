# coding=utf-8
import time

# Define main method
from collections import Set


def crible_era(up_to):
    # type: (int) -> Set[int]

    time_to_start_exec = time.time()  # type: float
    # Optional

    prime_numbers = {2}  # type: Set[int]
    # List of prime numbers

    actual_number = 3  # type: int
    # We start with 3, then continue in the odd numbers.
    # This number is the current number tested.

    list_checker = [False] * up_to
    # This list allows us to check if the number to be eliminated or not.
    # (Eliminate = No prime number)
    # (Eliminate = True)

    # this loop allows us to test all the numbers starting from x (continuing x + 2 at each turn) as long as
    # It's less than to the defined maximum number.
    while actual_number < up_to:
        if not list_checker[actual_number]:  # this checks if the number isn't eliminated

            prime_numbers.add(actual_number)  # adding to the list of prime numbers.
            deletion_of_multiple = actual_number  # type: int
            # create a temporary variable,
            # which will be used to delete all the multiples of the number we trained in the if loop.

            # this loop allows us to delete all multiples of the current number,
            # until It's less than to the maximum number defined.
            while deletion_of_multiple < up_to:
                list_checker[deletion_of_multiple] = True  # It eliminates the multiples in question,
                # by setting them to True in the checklist.
                deletion_of_multiple += actual_number  # It adds the current number of deletion
                # by the current number of test. (Continue the table)

        actual_number += 2
    # End of while loop

    time_to_end_exec = time.time() - time_to_start_exec  # type: float
    # Optional

    print("\nExecution time : " + str(time_to_end_exec) + " seconds.")
    # Optional

    return prime_numbers  # Return the list of prime numbers.


# Exec
choose_number = int(input("Choose a number to define how far to display prime numbers.\n-> Value = "))  # type: int

prime_number = crible_era(choose_number + 1)  # type: Set[int]

print("\nPrime Numbers (up to " + str(choose_number) + ") : (" + str(len(prime_number)) + " display)")
print("Tips: The numbers aren't arranged in order.")

# This for a loop allows us to dissect each of the numbers present in the list.
for number in prime_number:  # type: int
    print("-> " + str(number))
