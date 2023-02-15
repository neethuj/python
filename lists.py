class_roster = ["Durga","Iswarya","Neethu","Yaman"]
test_scores = [99,98,97,96]
zipcode = ["plano","75038"]
print(class_roster)
print(test_scores)
print(zipcode)

for student in class_roster:
    print(student)

for score in test_scores:
    print(score)


for i in range(len(class_roster)):
    student = class_roster[i]
    score = test_scores[i]
    print(student , score ) 


