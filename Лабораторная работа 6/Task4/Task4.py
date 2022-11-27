import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str, delimiter: str = ",", new_line: str = "\n") -> list[dict]:
    """
   This function converts data from csv to json format
   :param filename: this is input file name
   :param delimiter: separator between values, default is ",".
   :param new_line: line separator, "\n" by default.
   :return: list of dictionaries (column - value)
   """

    with open(filename, 'rt') as f:
        header = f.readline().replace(new_line, '').split(delimiter)
        rows = []
        for row in range(1, 5):
            rows.append(f.readline().replace(new_line, '').split(delimiter))

        list_ = []
        for row in rows:
            dict_ = dict(zip(header, row))
            list_.append(dict_)

    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
