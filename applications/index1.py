records = {
    ("alice", 'engineering'),
    ('bob', 'sales'),
    ('erol', 'marketing'),
    ('sandip', 'engineering'),
    ('lavonia', 'sales')
}


# 1st pass, brute force algo
def build_index(records):
    # search through list
    # iterate through the list
    # if value == engineering add to results list
# 2 next pass, greedy solution create index, as in from a book. it's a {} of indeces
# { 'key': [a,b,c], 'key': [a,b,c]}
    # build index
    index = {} 
    # build dict where k's are: depts
    # & the values are: [lists] of names
    for record in records:
        name = record[0]
        department = record[1]

        # dept might not exist yet in dict
        if department not in index:
            index[department] = [name]
        # if dept already exists
        else:
            index[department].append(name)
    return index

index_dict = build_index(records)
print(index_dict)

def print_department_using_index(dep_name):
    print(index_dict[dep_name])

print_department_using_index('engineering')


# analyze runtime of a loop by how many times the loop runs & what's in the loop
# loop is O(n) rest is O(1) so f() is O(n)