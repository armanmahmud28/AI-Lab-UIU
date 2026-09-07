import math
from queue import PriorityQueue

def heuristic(node, goal, coords):
    x1, y1 = coords[node]
    x2, y2 = coords[goal]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

class State:
    def __init__(self, node_id, parent, g, f):
        self.node_id = node_id
        self.parent = parent
        self.g = g
        self.f = f

    def __lt__(self, other):
        return self.f < other.f

print("Enter the graph information:")
print()

V = int(input().strip())

coords = {}
adjlist = {}

for _ in range(V):
    node, x, y = input().split()
    coords[node] = (int(x), int(y))
    adjlist[node] = []

E = int(input().strip())

for _ in range(E):
    node1, node2, cost = input().split()
    cost = int(cost)
    adjlist[node1].append((node2, cost))

start_node = input().strip()
goal_node = input().strip()

minQ = PriorityQueue()

g = 0
h = heuristic(start_node, goal_node, coords)
f = g + h

start_state = State(
    start_node,
    None,
    g,
    f
)

minQ.put(start_state)

goal_state = None

while not minQ.empty():
    curr_state = minQ.get()

    if curr_state.node_id == goal_node:
        goal_state = curr_state
        break

    for neighbor, edge_cost in adjlist[curr_state.node_id]:
        g = curr_state.g + edge_cost

        h = heuristic(
            neighbor,
            goal_node,
            coords
        )

        f = g + h

        new_state = State(
            neighbor,
            curr_state,
            g,
            f
        )

        minQ.put(new_state)

if goal_state is not None:
    path = []

    current_state = goal_state

    while current_state is not None:
        path.append(current_state.node_id)
        current_state = current_state.parent

    path.reverse()

    print()
    print("Solution path", " -> ".join(path))
    print("Solution cost: ", goal_state.g)

else:
    print()
    print("No solution path found")

