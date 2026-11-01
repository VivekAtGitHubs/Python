marks = {
    "math": 90,
    "sci": 85,
    "eng": 78
}
# Calculate total marks
total = 0
for mark in marks.values():
    total += mark
print("Total marks:", total)
# Find subject with highest marks
highest = 0
best_subject = ""
for subject, mark in marks.items():
    if mark > highest:
        highest = mark
        best_subject = subject
print("Highest subject:", best_subject)
print("Highest marks:", highest)