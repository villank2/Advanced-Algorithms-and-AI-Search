def h(start, goal):
    # ensure that start and goal are valid positions
    assert "".join(sorted(start)) == " 12345678" and "".join(sorted(goal)) == " 12345678"
    if start == goal:
        return 0
    return len([True for i in range(len(goal)) if goal[i] != start[i]]) -1
    
    
    # Work out how many tiles are out of place
    
    