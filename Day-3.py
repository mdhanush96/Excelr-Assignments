subject_1 = int(input("Enter marks for Subject 1: "))
subject_2 = int(input("Enter marks for Subject 2: "))
subject_3 = int(input("Enter marks for Subject 3: "))
average = (subject_1 + subject_2 + subject_3) / 3
if average >= 90:
    print("Grade: A")
elif 80 <= average < 90:
    print("Grade: B")
elif 70 <= average < 80:
    print("Grade: C")
else:
    print("Grade: Fail")


# In[ ]:




