import numpy as np
import sys

class Frame:
    def __init__(self, photo):

        sys.setrecursionlimit(10000) #wth cant live without recursion
        self.__frame = photo
        self.__height, self.__width = self.__frame.shape
        self.__visited = np.zeros(self.__frame.shape, dtype = 'b')
        self.__diri = [-1, -1, -1, 0, 0, 1, 1, 1] #edges for dfs
        self.__dirj = [-1, 0, 1, -1, 1, -1, 0, 1]
        self.__counter = 0 #also used outside init. used in dfs as a global

        self.pressed_key = 0 #getter maybe?
        
        i = 70 # a horizontal line through all the keys
        max_counter = 0
        key_index = 0
        for j in range(self.__width):
            if(self.__frame[i, j] == 0 and self.__visited[i, j] == 0):
                self.__counter = 0
                key_index += 1
                self.__dfs(i,j)
                #print('{} {}'.format(self.__counter, key_index))
                if(self.__counter > max_counter):
                    self.pressed_key = key_index
                    max_counter = self.__counter
    
    def __valid_pixel(self, i, j):
        if i < 0 or i >= self.__height : return False
        if j < 0 or j >= self.__width : return False
        if self.__visited[i, j] == True : return False
        if self.__frame[i, j] == 255 : return False
        return True

    def __dfs(self, i, j):
        self.__visited[i, j] = True
        self.__counter += 1
        for k in range(8):
            next_i, next_j = i + self.__diri[k], j + self.__dirj[k]
            if self.__valid_pixel(next_i, next_j):
                self.__dfs(next_i, next_j)
               
if __name__ == "__main__":
    photo3 = np.load('frame5.npy')
    frame = Frame(photo3)
    print(frame.pressed_key)
