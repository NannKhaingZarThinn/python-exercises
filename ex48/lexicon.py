class Lexicon(object):
    def __init__(self):
        #constants
        # TODO: Can we make these as constants so they can be accessed from out side the class with just the class name ?
        self.C_DIRECTION_WORDS = "direction"
        self.C_VERBS = "verb"
        self.C_STOP_WORDS = "stop"
        self.C_NOUNS = "noun"
        self.C_NUMBER = "number"
        self.C_ERROR = "error"

        #lexicon
        self.direction_words = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
        self.verbs = ['go', 'stop', 'kill', 'eat']
        self.stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
        self.nouns = ['door', 'bear', 'princess', 'cabinet']
        
    def get_tuple(self, word):
        ret_val = None
        lword = word.lower()
        if(lword in self.direction_words):
            ret_val = (self.C_DIRECTION_WORDS, word)
        elif(lword in self.verbs):
            ret_val = (self.C_VERBS, word)
        elif(lword in self.stop_words):
            ret_val = (self.C_STOP_WORDS, word)
        elif(lword in self.nouns):
            ret_val = (self.C_NOUNS, word)
        elif(self.convert_number(lword) != None):
            ret_val = (self.C_NUMBER, self.convert_number(lword))
        else:
            ret_val = (self.C_ERROR, word)

        return ret_val

    def convert_number(self, text):
        try:
            return int(text)
        except ValueError:
            return None


def scan(line):
    the_lexicon = Lexicon()
    ret_val = []
    words = line.split()
    for word in words:
        the_tuple = the_lexicon.get_tuple(word)
        ret_val.append(the_tuple)

    return ret_val