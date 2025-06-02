# Runner-Up Score Finder

# Get number of participants
n = int(input("Enter the number of participants: "))

# Get the scores
scores = list(map(int, input("Enter the scores separated by spaces: ").split()))

if len(scores) != n:
    print("Number of scores does not match number of participants.")
else:
    unique_scores = list(set(scores))
    unique_scores.sort(reverse=True)

    if len(unique_scores) < 2:
        print("Not enough distinct scores to find a runner-up.")
    else:
        print("Runner-Up Score:", unique_scores[1])
