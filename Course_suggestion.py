def course_suggestion():
    Name = input("Enter your name: ")
    percentage = float(input("Enter your percentage: "))
    Stream = input("Enter your stream (Science/Commerce/Arts): ").lower()

    if Stream == "science":
        if percentage >= 90:
            print(" you can pursue Engineering or Medical courses.")
        elif percentage <= 75 and percentage >= 35  :
            print(" you can pursue B.Sc or B.Tech courses or diploma courses.")
        else:
            print("attempt the exam of 12th.")

    elif Stream == "commerce":
        if percentage >= 90:
            print(" you can pursue CA or Business Management courses.")
        elif percentage <= 75 and percentage >= 35:
            print(" you can pursue B.Com or BBA courses or diploma courses.")
        else:
            print("attempt the exam of 12th.")

    elif Stream == "arts":
        if percentage >= 90:
            print("you can pursue courses in Fine Arts, Literature, or Social Sciences.")
        elif percentage <= 75 and percentage >= 35:
            print("you can pursue Diploma courses in Arts.")
        else:
            print("attempt the exam of 12th.")

    elif percentage < 0 or percentage > 100:
        print("Invalid percentage entered. Please enter a value between 0 and 100.")

    else:
        print("Invalid stream entered. Please enter Science, Commerce, or Arts.")

course_suggestion()