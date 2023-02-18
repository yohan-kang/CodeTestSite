

# Example 1:

# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:

# Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.


# 딕셔너리 사용 1
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        frequency = {}

        for i in words:
            if (i in frequency.keys()):
                frequency[i] += 1
            else:
                frequency[i] = 1
        
        sorted_keys = sorted(list(frequency.keys()), key=lambda x: (-frequency[x],x))
        return sorted_keys[:k]

from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        cnt = Counter(words)
        
        print(cnt.items())
        
        most_list = sorted(list(cnt.items()), key=lambda x: [-x[1], x[0]])
        
        print(most_list)
        
        answer = []
        
        for i in range(k):
            answer.append(most_list[i][0])
            
        return answer

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq = collections.Counter(words)
        res = sorted(freq, key=lambda x: (-freq[x], x))
        return res[:k]

# 딕셔너리 사용
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        word_count = {}
        
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        word_count_list = [(count, word) for word, count in word_count.items()]
        word_count_list.sort(key=lambda x: (-x[0], x[1]))
        return [word for count, word in word_count_list[:k]]