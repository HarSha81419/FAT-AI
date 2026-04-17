def and_or_search(state, goal):
    print("Current State: ", state)

    if state["has_banana"]:
        print("Goal Reached!")
        return True

    if state["monkey_pos"] != state["box_pos"]:
        print("OR: Move monkey to Box")
        new_state = state.copy()
        new_state["monkey_pos"] = new_state["box_pos"]
        return and_or_search(new_state, goal)
    
    print("AND: Performing sequence actions")

    if state["box_pos"] != state["banana_pos"]:
        print("-> push box to banana")
        state["box_pos"] = state["banana_pos"]
        state["monkey_pos"] = state["banana_pos"]

    if not state["on_box"]:
        print("-> Climb the Box")
        state["on_box"] = True
    
    if state["on_box"] and state["monkey_pos"] == state["banana_pos"]:
        print("-> Grab Banana")
        state["has_banana"] = True

    return and_or_search(state, goal)

state = {
    "monkey_pos" : "A",
    "box_pos" : "B",
    "banana_pos" : "C",
    "on_box" : False,
    "has_banana" : False
}

goal = True

result = and_or_search(state, goal)

if result:
    print("Monkey got the banana!")
else:
    print("Failed")