# 292. Nim Game
# Bu oyunu kazanıp kazanamayacağını belirleyen şey taş sayısının 4’e bölümünden kalanı.
# 4'e bölümünden kalan 0 ise kaybetmek zorundayız.
# 4'e bölümünden kalan 0 değilse kazanabilir.
class Solution:
    def canWinNim(self, n: int) -> bool:
        return True if n % 4 != 0 else False  