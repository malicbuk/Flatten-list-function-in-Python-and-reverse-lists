def reverse_lists(reversen):
    a=[]
    reversen.reverse()
    final_list= []
    for element in reversen:
        if type(element) is list:
            element.reverse()

    return reversen


print(reverse_lists([[1, 2], [3, 4], [5, 6, 7]]))


def flatten_lists(flatten):
    straight = []
    for element in flatten:
        if type(element) is list:
            for atom in element:
                if type(atom) is list:
                    for small in atom:
                        if type(small) is list:
                            for smallest in small:
                                straight.append(smallest)
                        else:
                            straight.append(small)
                else:
                    straight.append(atom)
        else:
            straight.append(element)
        return straight

print(flatten_lists([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5])


































































































































































































