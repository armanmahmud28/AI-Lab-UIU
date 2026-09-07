"""
A* Search Assignment: Autonomous Warehouse Robot

Expected output for the supplied input.txt:
Path: S -> B -> E -> F -> G
Total cost: 15
"""

import heapq


# ============================================================
# READ INPUT FILE
# ============================================================

def read_input(filename):
    with open(filename, "r") as file:
        lines = [line.strip() for line in file if line.strip()]

    index = 0

    # Number of nodes
    n = int(lines[index])
    index += 1

    # Heuristic values
    heuristic = {}
    for _ in range(n):
        node, h = lines[index].split()
        heuristic[node] = int(h)
        index += 1

    # Number of edges
    m = int(lines[index])
    index += 1

    # Graph
    graph = {}
    for _ in range(m):
        u, v, cost = lines[index].split()
        cost = int(cost)
        graph.setdefault(u, []).append((v, cost))
        index += 1

    # Remaining information
    start = None
    goal = None
    battery = None
    charger = None
    blocked = set()

    while index < len(lines):
        parts = lines[index].split()

        if parts[0] == "START":
            start = parts[1]

        elif parts[0] == "GOAL":
            goal = parts[1]

        elif parts[0] == "BATTERY":
            battery = int(parts[1])

        elif parts[0] == "CHARGER":
            charger = parts[1]

        elif parts[0] == "BLOCKED":
            blocked.add((parts[1], parts[2]))

        index += 1

    return heuristic, graph, start, goal, battery, charger, blocked


# ============================================================
# CHECK WHETHER AN EDGE IS BLOCKED
# ============================================================

def is_blocked(current, neighbor, blocked):
    #  TASK 1:
    # Return True if the directed edge current -> neighbor is blocked.
    return (current, neighbor) in blocked



# ============================================================
# CALCULATE NEW BATTERY
# ============================================================

def new_battery(current_battery, edge_cost, destination,
                charger, maximum_battery):
    #  TASK 2:
    # Return None when the robot does not have enough battery.
     if edge_cost > current_battery:
             return None

     battery = current_battery - edge_cost

    #  TASK 3:
    # Recharge to maximum battery when the robot reaches the charger.
     if destination == charger:
            battery = maximum_battery
    

     return battery


# ============================================================
# GENERATE VALID SUCCESSORS
# ============================================================

def get_successors(state, graph, blocked, charger, maximum_battery):
    current, battery = state
    successors = []

    for neighbor, cost in graph.get(current, []):

        if is_blocked(current, neighbor, blocked):
            # TASK 4
            continue

        remaining = new_battery(
            battery,
            cost,
            neighbor,
            charger,
            maximum_battery
        )

        if remaining is not None:
            successors.append((neighbor, remaining, cost))

    return successors


# ============================================================
# HEURISTIC FUNCTION
# ============================================================

def h_value(node, heuristic):
    # TASK 5:
    # Return the heuristic value of the given node.
    return heuristic[node]

# ============================================================
# RECONSTRUCT FINAL PATH
# ============================================================

def reconstruct_path(parent, goal_state):
    path = []
    state = goal_state

    while state is not None:
        path.append(state[0])
        state = parent[state]

    #  TASK 6:
    # Reverse the path so that it starts from S and ends at G and return it
    path.reverse()

    return path
    
   


# ============================================================
# A* SEARCH
# ============================================================

def a_star_search(graph, heuristic, start, goal,
                  initial_battery, charger, blocked):

    maximum_battery = initial_battery

    # State = (location, battery)
    start_state = (start, initial_battery)

    # Priority queue entries:
    # (f, g, state)
    frontier = []

    heapq.heappush(
        frontier,
        (h_value(start, heuristic), 0, start_state)
    )

    # Best known path cost to each state
    best_cost = {start_state: 0}

    # Parent of each state
    parent = {start_state: None}

    while frontier:

        f, g, current_state = heapq.heappop(frontier)

        # Ignore an outdated queue entry
        if g != best_cost.get(current_state):
            continue

        current, battery = current_state

        # Goal test
        if current == goal:
            path = reconstruct_path(parent, current_state)
            return path, g

        for neighbor, remaining_battery, edge_cost in get_successors(
            current_state,
            graph,
            blocked,
            charger,
            maximum_battery
        ):

            next_state = (neighbor, remaining_battery)
            new_cost = g + edge_cost

            if new_cost < best_cost.get(next_state, float("inf")):

                best_cost[next_state] = new_cost
                parent[next_state] = current_state

                #  TASK 7:
                # Calculate f(n) = g(n) + h(n).
                priority = new_cost + h_value(neighbor, heuristic)

                heapq.heappush(
                    frontier,
                    (priority, new_cost, next_state)
                )

    return None, None


# ============================================================
# PRINT RESULT
# ============================================================

def print_result(path, total_cost):
    if path is None:
        print("No valid path found.")
    else:
        print("Path:", " -> ".join(path))
        print("Total cost:", total_cost)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    heuristic, graph, start, goal, battery, charger, blocked = \
        read_input("input.txt")

    path, total_cost = a_star_search(
        graph,
        heuristic,
        start,
        goal,
        battery,
        charger,
        blocked
    )

    print_result(path, total_cost)


if __name__ == "__main__":
    main()

