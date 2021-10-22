tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = []
elems = [non_empty_tuples.append(i) for i in tuples if len(i) > 0]
print(non_empty_tuples)