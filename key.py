import numpy as np
import sys
sys.setrecursionlimit(10000) #wth cant live without recursion

class Key:
    def __init__(self, frame):
        self.frame = frame
        self.height, self.width = frame.shape
        self.visited = np.zeros(self.frame.shape, dtype = 'b')
        self.diri = [-1, -1, -1, 0, 0, 1, 1, 1]
        self.dirj = [-1, 0, 1, -1, 1, -1, 0, 1]

    def get_key_index(self):
        i = 70
        max_counter = 0, key_index = 0
        for j in range(self.width):
            if(self.frame[i, j] == 0 and self.visited[i, j] == 0):
                self.counter = 0
                key_index += 1
                self.dfs(i,j)
                if(self.counter > max_counter):
                    ans = key_index
                    max_counter = self.counter
    def valid_pixel(self, i, j):
        if i < 0 or i >= self.height : return False
        if j < 0 or j >= self.width : return False
        if self.visited[i, j] == True : return False
        if self.frame[i, j] == 255 : return False
        return True

    def dfs(self, i, j):
        self.visited[i, j] = True
        self.counter += 1
        for k in range(8):
            next_i, next_j = i + self.diri[k], j + self.dirj[k]
            if self.valid_pixel(next_i, next_j):
                self.dfs(next_i, next_j)
               
if __name__ == "__main__":
    frame3 = np.load('frame5.npy')
    key = Key(frame3)
    key.get_key_index()