def loop_through_list():
    print_str = ''
    char_list = ['h','e','l','l','o']
    for char in char_list[:-1]:
        print_str = print_str + char
    return(print_str)

# TEST
# print(loop_through_list())

def iterate_over_list():
    a_list = []
    a_list = ['a','b','c','d']
    lst = []
    lst = [1,2,3,4,5,6,7,8,9]
    for element in a_list:
        print(element)
    print(a_list[-4:-1])
    print(a_list[-4:])
    print(a_list[1:4])

    print("---")   
    for x in range(len(a_list)): 
        print(a_list[x])
    print("reversed")
    for x in range(len(lst)-1,-1,-1): 
        print(lst[x])
    print("---")   
    x = 0
    while x < len(a_list): 
        print(a_list[x]) 
        x = x+1

# TEST
# print("list looping:")
# iterate_over_list()

def fun_with_sets():
    this_set = set()
    this_set = {1,2,3,4,5}
    that_set = {5,6,7,8,9}
    print(1 in this_set)
    print(this_set)
    this_set.add(6)
    this_set.add(5)
    print(this_set)
    this_set.remove(5) # raises an error if not found in set
    # this_set.remove(5)
    # this_set.discard(5) # does not raise an error if not found in set
    print(this_set)
    this_set.pop() # removes the last item - UNORDERED so you don't know which one
    this_set.add(5)
    unioned_set = this_set.union(that_set)
    print(this_set)
    print(unioned_set)

    print(this_set)
    this_set.clear()
    print(this_set)

    set1 = {"a", "b" , "c"}
    set2 = {1, 2, 3}

    set3 = set1.union(set2) # returns a union
    print("union:",set3)

    set1 = {"a", "b" , "c"}
    set2 = {1, 2, 3}
    set1.update(set2)
    print("update:",set1) # updates set 1 by adding set 2 items

    set1 = {"a","b","c","d","e"}
    set2 = {"c", "e", "q"}
    set3 = set1.intersection(set2)
    print("intersection:",set3) 

    set1 = {"a","b","c","d","e"}
    set2 = {"c", "e", "q"}
    set3 = set1.difference(set2)
    print("difference:",set3) 
    

# TEST
# fun_with_sets()

def fun_with_dictionaries():

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }  
    print(thisdict)
    x = thisdict["model"]
    print(x)
    x = thisdict.get("model")
    print(x)

    thisdict["year"] = 1994
    print(thisdict["year"])

    for x in thisdict:
        print(x) # print all the keys in thisdict

    for x in thisdict:
        print(thisdict[x]) # print all the values in thisdict
    
    for x in thisdict.values():
        print(x) # print all the values in thisdict

    for key, value in thisdict.items():
        print(key,':', value)

    x = thisdict.items() # returns a view item i.e. a pointer to the dictionary
    print(x)


# TEST
# fun_with_dictionaries()

def fun_with_tuples():
    thistuple = ("red", "white","blue","yellow","green","magenta","blue","blue")
    print(thistuple)
    print(thistuple[1])
    print(thistuple[-1])
    print(thistuple[2:5])
    print(thistuple[-4:-1])

    for x in thistuple:
        print(x)
    print("---")
    for x in thistuple[2:4]:
        print(x)

    one_item_tuple = ("just one",)
    print(type(one_item_tuple))

    print("count:",thistuple.count("blue"))

    print("index:",thistuple.index("white"))


# TEST
# fun_with_tuples()

def fun_with_math():

    print(5.0/2)
    print(-5.0/2)
    print(-5//2)
    print(5//2)

# TEST
fun_with_math()

