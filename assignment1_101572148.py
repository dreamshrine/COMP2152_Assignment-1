"""
Author: Shayne Atkins
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton"  # datatype = string
preferred_weight = 20.5  # datatype = float
highest_reps = 25  # datatype = integer
membership_active = True  # datatype = boolean

# Step c: Create a dictionary named workout_stats
# dictionary with string keys and integer values describing workout minutes (yoga, running, weightlifting)
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (20, 30, 40),
    "Taylor": (50, 45, 30)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
#Calculate total number of workout minutes and add new key-value pairs
for friend, workouts in list(workout_stats.items()):
    total_minutes = sum(workouts)
    workout_stats[f"{friend}_Total"] = total_minutes

# Step e: Create a 2D nested list called workout_list
#2D list containing workout minutes from dictionary. Rows are friends, columns are activities.
workout_list = [
    workouts
    for friend, workouts in workout_stats.items()
    if not friend.endswith("_Total")
]

# Step f: Slice the workout_list
friends = workout_list[0:3]
yoga_run_minutes = [row[0:2] for row in friends]
print(yoga_run_minutes)

last_two = workout_list[1:3]
weight_minutes = [row[2:3] for row in last_two]
print(weight_minutes)

# Step g: Check if any friend's total >= 120
if total_minutes >= 120:
    print(f"Great job staying active, {friend}!")

# Step h: User input to look up a friend
name = input("Enter a friend's name: ")
if name in workout_stats:
    minutes = workout_stats[name]
    total = workout_stats.get(f"{name}_Total", 0)

    print(f"{name}'s Workout Stats:")
    print(f"Yoga: {minutes[0]} minutes")
    print(f"Running: {minutes[1]} minutes")
    print(f"Weightlifting: {minutes[2]} minutes")
else:
    print(f"Friend {name} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
total_workouts = {
    friend.replace("_Total", ""): minutes
    for friend, minutes in workout_stats.items()
    if friend.endswith("_Total")
}

highest_friend = max(total_workouts, key=total_workouts.get)
lowest_friend = min(total_workouts, key=total_workouts.get)

print("\nWorkout Summary:")
print(f"Highest Total Workout Minutes: {highest_friend} ({total_workouts[highest_friend]} minutes)")
print(f"Lowest Total Workout Minutes: {lowest_friend} ({total_workouts[lowest_friend]} minutes)")
