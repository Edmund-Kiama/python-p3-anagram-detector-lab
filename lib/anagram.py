# your code goes here!
class Anagram:
    def __init__(self, anagram):
        self.anagram = anagram
        
    def match(self, list):
        sorted_anagram = sorted(self.anagram)
        return [word for word in list if sorted(word) == sorted_anagram]