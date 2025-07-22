#prompt task details
task = input("Enter your task:")
priority = input(Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): "))
# provide reminder based on task details
match priority = priority.lower()
    case "high":    
    if time_bound == "yes":
              print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to get it done as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Schedule it within the next few days.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task but still needs attention today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level entered. Please use high, medium, or low.")









