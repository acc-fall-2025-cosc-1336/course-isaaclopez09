def get_p_distance(list1, list2):
    differences = 0
    length = len(list1)

    for i in range(length):
        if list1[i] != list2[i]:
            differences += 1
       

    p_distance =  differences / length
    return p_distance

def get_p_distance_matrix(list1):
    n=len(list1)
    p_distance_matrix = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(get_p_distance(list1[i], list1[j]))
        p_distance_matrix.append(row)
    return p_distance_matrix
