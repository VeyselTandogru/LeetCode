# 1025. Divisor Game
# çift sayılar True : Mesela 16 yı düşünelim 16-8 = 8, 8-4 = 4, 4-2 = 2, 2-1 = 1
# Tek sayılar False : Mesela 17 yı düşünelim 17-1 = 16, 16-8 = 8, 8-4 = 4, 4-2 = 2, 2-1 = 1
class Solution:
    def divisorGame(self, n: int) -> bool:
        if n %2 != 0:
            return False
        else: 
            return True
