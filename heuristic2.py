def h(start,goal):
  targets = [(i,goal.index(start[i])) for i in range(len(start)) if start[i] != goal[i] and start[i]!=' ']
  counter = 0
  for strt,end in targets:
    moves = abs(strt-end)
    if moves == 1:
      counter += 1
    elif moves == 2:
      counter += 2
    else:
      counter += moves//2
  return counter
