capacity = (12, 8, 5)
initial_state = (12, 0, 0)
final_state = (6, 6, 0)

x, y, z = capacity
memory = {}
ans = []

def get_all_states(state):
    global ans
    global memory

    a, b, c = state

    if (a, b, c) == final_state:
        ans.append(state)
        return True

    if (a, b, c) in memory:
        return False

    memory[(a, b, c)] = 1
    if a > 0:
        if a+b<=y:
            if get_all_states((0, b + a, c)):
                ans.append(state)
                return True
        else:
            if get_all_states((a - (y - b), y, c)):
                ans.append(state)
                return True
        if a+c <= z :
            if get_all_states((0, b, c + a)):
                ans.append(state)
                return True
        else:
            if get_all_states((a - (z - c), b, z)):
                ans.append(state)
                return True
    if b > 0 :
        if b+a <= x:
            if get_all_states((a + b, 0, c)):
                ans.append(state)
                return True
        else:
            if get_all_states((x, b - (x - a), c)):
                ans.append(state)
                return True
        if b+c <= z:
            if get_all_states((a, 0, c + b)):
                ans.append(state)
                return True
        else:
            if get_all_states((a, b - (z - c), z)):
                ans.append(state)
                return True

    
    if c > 0:
        if c+a <= x:
            if get_all_states((a + c, b, 0)):
                ans.append(state)
                return True
        else:
            if get_all_states((x, b, c - (x - a))):
                ans.append(state)
                return True

     
     
        if c+b <= y:
            if get_all_states((a, b + c, 0)):
                ans.append(state)
                return True
        else:
            if get_all_states((a, y, c - (y - b))):
                ans.append(state)
                return True

    return False

print("Starting work...\n")
get_all_states(initial_state)

ans.reverse()

for state in ans:
    print(state)