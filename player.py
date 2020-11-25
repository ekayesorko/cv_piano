from numpy.lib.function_base import place
import pygame.mixer as mx

class Player:
    def __init__(self):
        self.__last_note = -1 # 1 based indexing. 0 used for no note
        self.__same_note_count = 0
        self.__root_note = 0
        self.__activation_threshold = 5
        
        mx.init(frequency=22050) 
        self.sounds = self.__init_sounds()

    def hit(self, key):
        if self.__last_note == key:
            self.__same_note_count += 1
        else:
            self.__last_note = key
            self.__same_note_count = 1
        
        if self.__same_note_count == self.__activation_threshold: 
            #same note count beshi hoiler ekbar e bajbe
            #jotokkhon na key = 0 diye reset na hoy
            if key != 0:
                self.__play_note(key)

    def __play_note(self, key):
        self.sounds[key - 1].play()

    def __init_sounds(self):
        note_names = ["A5", "B5", "C5", "D5", "E5", "F5", "G5"]
        sounds = []
        for i, str in enumerate(note_names):
            filename = "sounds/" + str + ".wav"
            sounds.append(mx.Sound(filename))
        return sounds

if __name__ == "__main__":
    import time
    player = Player()
    player.sounds[1].play()
    time.sleep(2)
    arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
    for i in arr:
        player.hit(i)
        time.sleep(0.03)
    