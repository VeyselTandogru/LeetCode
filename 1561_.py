# 1561. Maximum Number of Coins You Can Get
# coin seçerken bob için her zaman en küçük olanı seçecek
# coin seçerken alice için her zaman en büyük olanı seçecek
# coin seçerken kendimiz için ise her zaman en büyükten bir küçük olanı seçeceğiz
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        i = 1
        sum_ = 0
        while i <= len(piles)//3:
            sum_ += piles[-2 * i]
            i += 1
        return sum_

