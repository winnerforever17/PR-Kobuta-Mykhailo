class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age
        self.activities = []
        self.goals = []

    def add_activity(self, activity):
        self.activities.append(activity)

    def set_goal(self, goal):
        self.goals.append(goal)

    def get_activity_statistics(self):
        total_distance = sum(activity.distance for activity in self.activities)
        total_calories = sum(activity.calories for activity in self.activities)
        return {
            "загальна відстань": total_distance,
            "всього калорій": total_calories,
            "Діяльності": len(self.activities)
        }

    def validate_unique_email(self, email):
        return email != self.email

    def validate_unique_username(self, username):
        return username != self.username


class Activity:
    def __init__(self, activity_type, duration, distance, calories):
        self.activity_type = activity_type
        self.duration = duration
        self.distance = distance
        self.calories = calories

    def validate_activity(self):
        allowed_activities = ["біг", "ходьба", "фізичні вправи"]
        return self.activity_type.lower() in allowed_activities


class Goal:
    def __init__(self, goal_type, target):
        self.goal_type = goal_type
        self.target = target


class ProgressTracker:
    def __init__(self, user):
        self.user = user

    def track_progress(self):
        progress = {}
        for goal in self.user.goals:
            if goal.goal_type == "щоденні кроки":
                steps_taken = 5000
                if steps_taken >= goal.target:
                    progress[goal.goal_type] = "Мета досягнута"
                else:
                    progress[goal.goal_type] = f"{goal.target - steps_taken} залишилося кроків"
        return progress


user1 = User("Джон", "john@example.com", 30)
activity1 = Activity("Біг", 30, 5, 200)
user1.add_activity(activity1)
goal1 = Goal("Щодені кроки", 7000)
user1.set_goal(goal1)

tracker = ProgressTracker(user1)
print(tracker.track_progress())
print(user1.get_activity_statistics())
