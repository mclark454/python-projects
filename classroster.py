#project needs exception handling ex: if user inputs any character other than y, absentCounter will increment
pupils = ["Joe","Sonny","Yassine","Emma","Ines","Satveer","Lily","Reuben","Lucy","Tom"]
counter = 0
presentCounter = 0
for name in pupils:
    print(name)
    counter = counter + 1
    present = input("Is this student present? (y or n)")
    if present == "y":
      presentCounter = presentCounter +1
    print("Total number of students: " + str(counter))
    print("Present: " + str(presentCounter))
    absentCounter = counter - presentCounter
    print("Absent: " + str(absentCounter))
  