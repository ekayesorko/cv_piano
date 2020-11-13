class Player:
    def __init__(self):
        self.__last_note = -1 # 1 based indexing. 0 used for no note
        self.__same_note_count = 0
        self.__root_note = 0

    def hit(self, key):
        if key == 0:
            self.__last_note = -1 
