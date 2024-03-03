# your code goes here!

class Anagram:

    def __init__(self, word):
        self.word = word

    
    def match(self, anagrams):
        sorted_word = sorted(self.word.lower())
        matches = []
        for anagram in anagrams:
            if sorted(sorted_word) == sorted(anagram.lower()):
                matches.append(anagram)
        return matches
            
mujahid = Anagram('listen')
matches = mujahid.match(['enlists', 'google', 'inlets', 'banana', 'enlists', 'nistel'])
print(matches)


