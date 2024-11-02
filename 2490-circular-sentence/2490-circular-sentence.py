class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()
        return all(a[-1] == b[0] for a, b in pairwise(sentence + [sentence[0]]))