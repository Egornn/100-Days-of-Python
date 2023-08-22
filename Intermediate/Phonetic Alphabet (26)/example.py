import pandas

example_dict = {'student': ['A', "B", "C"], 'score': [55, 65, 71]}
example_dataset = pandas.DataFrame(example_dict)
print(example_dataset)
print('Iterate by columns')
for (header, values) in example_dataset.items():
    print(header)
    print(values)
    print()
print('Iterate by rows')
for (index, row) in example_dataset.iterrows():
    print(index)
    print(row)
    print(row.score)
    print()
