def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges =[]
    for name in names:
        badges.append(f"Hello, my name is {name}.")
    return badges

def assign_rooms(names):
    room_assignments = []
    for i in range(len(names)):
        room_number = i + 1
        room_assignments.append(f"Hello, {names[i]}! You'll be assigned to room {room_number}!")
    return room_assignments


def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)
    room_assignments = assign_rooms(names)
    for assignment in room_assignments:
        print(assignment)
