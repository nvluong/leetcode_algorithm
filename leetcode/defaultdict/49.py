from collections import defaultdict
def_dict = defaultdict(list)
def_dict['one'] = 1
print(def_dict['missing'])
def_dict['missing1'].append(2)
print(def_dict)