from libcpp.vector cimport vector
from libcpp.pair cimport pair
import numpy as np
from libc.stdio cimport printf

#distutils: language = c++
#use this line in setup.py for using libcpp stuffs

ctypedef pair [int,int] cpair 

cpdef dfs(vector[ vector[int] ] photo):

    cdef vector[ pair[int, int] ] stack
    #stack.push_back(cpair(1,2))
    #h,w = photo.shape
    cdef int height = photo.size()
    cdef int width = photo[0].size()
    #printf("%d %d\n", height, width)
    cdef vector[ vector[int] ] visited = np.zeros((height,width),dtype = 'b') 
    cdef int i = 70, j = 0, k = 0
    cdef int pixel_counter, pressed_key = 0, max_pixel_counter = 0, key_index = 0
    cdef vector[int] dirx = [-1, -1, -1, 0, 0, 1, 1, 1]
    cdef vector[int] diry = [-1, 0, 1, -1, 1, -1, 0, 1]
    cdef pair[int, int] now
    cdef float average, total_pixel_counter = 0

    for j in range(width):
        if photo[i][j] == 0 and visited[i][j] == False:
            pixel_counter = 0
            key_index += 1
            stack.clear()
            stack.push_back( cpair(i,j))
            visited[i][j] = True
            while(stack.empty() == False):
                now = stack.back()
                pixel_counter += 1
                stack.pop_back()
                for k in range(8):
                    next_i = now.first + diry[k]
                    next_j = now.second + dirx[k]
                    if (next_i < 0 or next_i >= height
                    or next_j < 0 or next_j >= width):
                        continue
                    if visited[next_i][next_j] == True : continue
                    if photo[next_i][next_j] == 255 : continue
                    stack.push_back( cpair(next_i, next_j))
                    visited[next_i][next_j] = True
            if pixel_counter > max_pixel_counter:
                max_pixel_counter = pixel_counter
                pressed_key = key_index

            total_pixel_counter += pixel_counter 
            #printf("%d %d\n", contour_counter,pixel_counter)
    
    average =  (total_pixel_counter - max_pixel_counter) / (key_index - 1) #excluding the outlier
    #printf("%f/n", (max_pixel_counter - average) / max_pixel_counter * 100 )
    if ( (max_pixel_counter - average) / max_pixel_counter * 100 ) > 10 and key_index == 7:
        return pressed_key
    else : return 0





        

    