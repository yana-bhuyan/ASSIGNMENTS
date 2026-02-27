n = int(input("Enter number of students: "))
scores = list(map(int, input("Enter scores: ").split()))

max_score = max(scores)

while max_score in scores:
    scores.remove(max_score)

print("Runner-up score:", max(scores))