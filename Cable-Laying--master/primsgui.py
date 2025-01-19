import tkinter as tk
import threading

# Color and font constants
BG_COLOR = "#FF0000"  # Red
LABEL_COLOR = "#333333"
BUTTON_COLOR = "#4CAF50"  # Green
FONT_STYLE = ("Arial", 12)  # Font family and font size

class MinCost:
    lock = threading.Lock()

    def __init__(self, value=0):
        with self.lock:
            self.value = value

    def get_value(self):
        with self.lock:
            return self.value

    def increment(self, value):
        with self.lock:
            self.value += value

def calculate_mst(mincost):
    n = entry_n.get()
    
    # Check if the value is empty
    if not n:
        return

    try:
        n = int(n)
    except ValueError:
        return

    distances_str = text_distances.get("1.0", "end-1c")
    distances = [[int(val) for val in row.split()] for row in distances_str.split("\n")]

    mst_set = [False] * n
    selected_vertices = [0]
    mst_cost = 0

    while len(selected_vertices) < n:
        min_edge = float('inf')
        next_vertex = None
        for u in selected_vertices:
            for v in range(n):
                if not mst_set[v] and distances[u][v] < min_edge:
                    min_edge = distances[u][v]
                    next_vertex = v
        selected_vertices.append(next_vertex)
        mst_set[next_vertex] = True
        mst_cost += min_edge

    mincost.increment(mst_cost)

def calculate_minimum_cost():
    mincost = MinCost()
    calculate_mst(mincost)
    update_min_cost_box(mincost)

def update_min_cost_box(mincost):
    min_cost_box.config(state="normal")
    min_cost_box.delete(1.0, "end")
    min_cost_box.insert(1.0, f"Minimum cost: {mincost.get_value()}")
    min_cost_box.config(state="disabled")

root = tk.Tk()
root.title("Minimum Spanning Tree Calculator")
root.configure(bg=BG_COLOR)

label_n = tk.Label(root, text="Enter the number of companies:", fg=LABEL_COLOR, bg=BG_COLOR, font=FONT_STYLE)
entry_n = tk.Entry(root, font=FONT_STYLE)

label_distances = tk.Label(root, text="Enter the distance between them (one row per company):", fg=LABEL_COLOR, bg=BG_COLOR, font=FONT_STYLE)
text_distances = tk.Text(root, height=5, width=30, font=FONT_STYLE)

calculate_button = tk.Button(root, text="Calculate MST", command=calculate_minimum_cost, bg=BUTTON_COLOR, fg="white", font=FONT_STYLE)
min_cost_box = tk.Text(root, height=1, width=20, state="disabled", bg=BG_COLOR, font=FONT_STYLE)

label_n.pack()
entry_n.pack()
label_distances.pack()
text_distances.pack()
calculate_button.pack()
min_cost_box.pack()

root.mainloop()
