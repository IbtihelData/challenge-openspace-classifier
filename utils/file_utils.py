from typing import List

def read_names_from_csv(filepath: str) -> List[str]:
    """
    Reads a file containing colleague names and returns a list of names.

    :param filepath: path to the CSV file
    :return: list of colleague names
    """

    names = []

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            cleaned = line.strip()

            if cleaned:  # ignore empty lines
                names.append(cleaned)

    return names

