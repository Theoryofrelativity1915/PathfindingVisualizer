import pygame as p
from Constants import WIDTH, ROWS, COLS, NODE_WIDTH, WHITE, BLACK, PURPLE, TURQUOISE
from Node import Node
from queue import Queue
from collections import defaultdict

#Initialize window
p.init()
WIN = p.display.set_mode((WIDTH, WIDTH))
p.display.set_caption("Dijkstra's Pathfinding Visualizer")


#Create grid
def create_grid(rows, cols):
    grid = []
    for row in range(rows):
            grid.append([])
            for col in range(cols):
                node = Node(row, col)
                grid[row].append(node)
    for row in range(rows):
        for col in range(cols):
            node = grid[row][col]
            node.get_neighbors(grid)
    return grid


def draw(rows, cols, grid):
    WIN.fill(WHITE)
    for row in range(rows):
        for col in range(cols):
            node = grid[row][col]
            p.draw.line(WIN, BLACK, (0, row * NODE_WIDTH), (WIDTH, row * NODE_WIDTH))
            p.draw.line(WIN, BLACK, (col * NODE_WIDTH, 0), (col * NODE_WIDTH, WIDTH))
            node.draw(WIN)
    p.display.update()
    
#returns mouse row and column
def get_mouse_pos(position):
    x, y = position
    col = x // NODE_WIDTH
    row = y // NODE_WIDTH
    return (row, col)


def draw_path(end, distances, draw):
    print("success!")
    for predecessor in end.predecessors:
        if predecessor.color != TURQUOISE:
            predecessor.color = PURPLE
        draw()
        p.display.update()
        

#Create algorithm
def dijkstras(draw, start, end, grid):
    distances = {node: {'cost': float('inf'), 'pred': []} for row in grid for node in row}
    queue = Queue()
    queue.put(start)
    distances[start]['cost'] = 0
    while not queue.empty():
            current = queue.get()
            for event in p.event.get():
                if event.type == p.QUIT:
                    run = False
                    p.quit()
            if current == end:
                draw_path(end, distances, lambda: draw())
                break
            for neighbor in current.neighbors:
                
                if not neighbor.is_visited() and not neighbor.is_wall():
                    if neighbor != start and neighbor != end:
                        neighbor.make_visiting()
                    #the cost to visit this nodes neighbor is the cost of this node + distance to the next node (since this is unweighted the cost is just 1)
                    cost = distances[current]['cost'] + 1
                    if cost < distances[neighbor]['cost']:
                        distances[neighbor]['cost'] = cost
                        neighbor.predecessors = set(current.predecessors)
                        neighbor.predecessors.add(current)
                    queue.put(neighbor)
                    if current != start:
                        current.make_visited()
            draw()


def main():
    grid = create_grid(ROWS, COLS)
    run = True
    start = None
    end = None
    while(run):
        draw(ROWS, COLS, grid)
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
            if p.mouse.get_pressed()[0]:
                row, col = get_mouse_pos(p.mouse.get_pos())
                if not row > ROWS - 1 and not col > COLS - 1:
                    node = grid[row][col]
                    if start == None and node != end:
                        start = node
                        start.make_start()
                    elif end == None and node != start:
                        end = node
                        end.make_end()
                    elif node != start and node != end:
                        node.make_wall()
                if p.mouse.get_pressed()[2]:
                    row, col = get_mouse_pos(p.mouse.get_pos())
                    node = grid[row][col]
                    if node.is_start():
                        start = None
                        node.color = WHITE
                    elif node.is_end():
                        end = None
                        node.color = WHITE
            if event.type == p.KEYDOWN:
                if event.key == p.K_SPACE:
                    dijkstras(lambda: draw(ROWS, COLS, grid), start, end, grid)
                elif event.key == p.K_c:
                    grid = create_grid(ROWS, COLS)
                    start = None
                    end = None
                
        p.display.update()
main()
#main loop
    #get mouse/keyboard clicks