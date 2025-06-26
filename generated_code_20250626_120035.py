            from typing import List

def get_permutations(string: str) -> List[str]:
    """
    Generates all permutations of a given string.

    Args:
        string: The input string.

    Returns:
        A list of all unique permutations of the string.
    """

    if len(string) == 0:
        return [""]

    if len(string) == 1:
        return [string]

    permutations = []
    for i in range(len(string)):
        char = string[i]
        remaining_string = string[:i] + string[i+1:]
        sub_permutations = get_permutations(remaining_string)
        for sub_permutation in sub_permutations:
            permutations.append(char + sub_permutation)

    return permutations


def main():
    """
    Demonstrates the usage of the get_permutations function.
    """

    input_string = "abc"
    result = get_permutations(input_string)
    print(f"Permutations of '{input_string}': {result}")

    input_string = ""
    result = get_permutations(input_string)
    print(f"Permutations of '{input_string}': {result}")

    input_string = "a"
    result = get_permutations(input_string)
    print(f"Permutations of '{input_string}': {result}")


if __name__ == "__main__":
    main()

