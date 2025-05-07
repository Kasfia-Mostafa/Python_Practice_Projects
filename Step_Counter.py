print("Step Counter -")
daily_goal = int(input("What is your daily step goal?\n"))
current_steps = int(input("How may steps you have taken today?\n"))

remaining = daily_goal - current_steps
if remaining > 0:
  print(f"You need {remaining} more steps to reach your goal!")
else:
  print(f"Congratulaion! You've exceeded your goal by {-remaining} steps!")

  
