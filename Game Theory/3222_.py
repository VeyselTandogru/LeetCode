# 3222. Find the winning player in coin game
class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        if x > (y // 4):
            if (y // 4)%2 == 0:
                return "Bob"
            else: 
                return "Alice"
        else:
            if x%2 == 0:
                return "Bob"
            else:
                return "Alice"