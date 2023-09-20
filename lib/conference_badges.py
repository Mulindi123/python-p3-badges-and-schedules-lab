def badge_maker(name):
    return (f"Hello, my name is {name}.")
print(badge_maker("Moris Okanda"))

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(badge_maker(name))
    return badges
speakers = ["Andrea", "Alicia", "Ariella"]
badges = batch_badge_creator(speakers)
print(badges)


def assign_rooms(names):
    room_assignments = []
    for i, name in enumerate(names, start=1):
        room_assignment = f"Hello, {name}! You'll be assigned to room {i}!"
        room_assignments.append(room_assignment)
    return room_assignments
speakers = ["Andrea", "Alicia", "Ariella"]
room_assignments = assign_rooms(speakers)
print(room_assignments)

def printer(names):
    for badge in badges:
        print(badge)
    for assignment in room_assignments:
        print(assignment)
printer(speakers)
