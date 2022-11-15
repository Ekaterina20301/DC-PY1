from pprint import pprint

number_list = [{'bin': bin(number_), 'dec': number_, 'hex': hex(number_), 'oct': oct(number_)}
               for number_ in range(16)]

pprint(number_list)
