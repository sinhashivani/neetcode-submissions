class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        grades = {}
        items.sort(key = lambda x: (x[0], -x[1]))

        res = []
        n = len(items)
        i = 0
        while i < n:
            ids = items[i][0]
            sums = 0
            for a in range(i, i + 5):
                sums += items[a][1]
            while i < n and items[i][0] == ids:
                i += 1
            res.append([ids, sums // 5])

        return res
                    