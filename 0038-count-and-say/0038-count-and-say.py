class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 0:
            return ""
        result = "1"
        for _ in range(n - 1):
            result = self.next_sequence(result)
        return result

    def next_sequence(self, s: str) -> str:
        result = []
        i = 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1
            result.append(str(count) + s[i])
            i += 1
        return ''.join(result)
