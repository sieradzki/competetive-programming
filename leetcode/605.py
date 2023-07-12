class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i, val in enumerate(flowerbed):
            if i == 0:
                if len(flowerbed) > 1:
                    if val == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        count += 1
                else:
                    if val == 0:
                        count += 1
            elif i == len(flowerbed)-1:
                if val == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    count += 1
            else:
                if val == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    count += 1

        return count >= n