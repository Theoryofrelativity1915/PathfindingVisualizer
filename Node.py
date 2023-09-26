import pygame as p
from Constants import RED, PURPLE, BLACK, TURQUOISE, ORANGE, WHITE, GREEN, NODE_WIDTH, ROWS, COLS


class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.neighbors = []
        self.color = WHITE
        self.predecessors = []
        
    def is_visited(self):
        return self.color == RED
    
    def make_visited(self):
        self.color = RED
    
    def make_visiting(self):
        self.color = GREEN
    
    def make_path(self):
        self.color = PURPLE
        
    def is_wall(self):
        return self.color == BLACK
    
    def make_wall(self):
        self.color = BLACK
        
    def is_start(self):
        return self.color == TURQUOISE
    
    def make_start(self):
        self.color = TURQUOISE
        
    def is_end(self):
        return self.color == ORANGE
    
    def make_end(self):
        self.color = ORANGE
        
    def draw(self, win):
        p.draw.rect(win, self.color, ((self.col * NODE_WIDTH + 1, self.row * NODE_WIDTH + 1), (NODE_WIDTH - 1, NODE_WIDTH - 1)))
    
    def get_neighbors(self, grid):
        #Moving up
        if self.row > 0 and not grid[self.row - 1][self.col].is_wall():
            self.neighbors.append(grid[self.row - 1][self.col])
        
        #Moving down
        if self.row < ROWS - 1 and not grid[self.row + 1][self.col].is_wall():
            self.neighbors.append(grid[self.row + 1][self.col])
        
        #Moving right
        if self.col < COLS - 1 and not grid[self.row][self.col + 1].is_wall():
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_wall():
            self.neighbors.append(grid[self.row][self.col - 1])