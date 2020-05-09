n = int(raw_input())
integer_list = map(int, raw_input().split())
tuplex=()
for i in integer_list:
    tuplex = tuplex + (i,)

print hash(tuplex)