#find highest,lowest score and winner's position without using 
scores = [40, 80, 65, 95, 70]
highest = scores[0]
lowest = scores[0]
winner_position = 0
for i in range(len(scores)):
    if scores[i] > highest:
        highest = scores[i]
        winner_position = i
    if scores[i] < lowest:
        lowest = scores[i]
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Winner is at position", winner_position + 1)