def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    # badge_greetings = []
    # for name in names:
    #     badge_greetings.append(f"Hello, my name is {name}.")
    # return badge_greetings

    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    # room_assignments = []
    # room_number = 1

    # for name in names:
    #     message = f"Hello, {name}! You'll be assigned to room {room_number}!"
    #     room_assignments.append(message)
    #     room_number += 1

    # return room_assignments

    return [f"Hello, {names[i]}! You'll be assigned to room {i + 1}!" for i in range(len(names))]



    

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)

    for room in assign_rooms(names):
        print(room)
