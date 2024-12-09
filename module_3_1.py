calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(a):
    count_calls()
    return len(a), a.upper(), a.lower()
def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [i.upper() for i in list_to_search]
print(string_info('Urban'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)