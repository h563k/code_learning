###
终端某产品的车间工人位置分布视作一个矩阵，记为二维数组 scores，scores[row][col] 代表此位置工人的 11 月的完成件数。
每位工人都想计算同行同列中一共有多少人比自己完成的件数多，最后把计算结果记录在一个新的二维数组的对应位置上，并返回该二维数组。
示例 1：
输入：scores = [[10,20],[30,10]]
输出：[[2,0],[0,2]]
解释：

与 scores[0][0] 同行的元素中 scores[0][1] 比它大，与 scores[0][0] 同列的元素中 scores[1][0]比它大，同行同列合计2个人；
与 scores[0][1] 同行同列的两个元素都不比它大；
与 scores[1][0] 同行同列的两个元素都不比它大；
与 scores[1][1] 同行同列的两个元素都比它大。
注：返回的数组和 scores 的行、列数相等。

示例 2：
输入：scores = [[10,20,30],[30,15,10]]
输出：[[3,1,0],[0,2,3]]
解释：
与 scores[0][0] 同行同列的三个元素都比它大；
与 scores[0][1] 同行同列的三个元素中 score[0][2] 比它大；
与 scores[0][2] 同行同列的三个元素都不比它大；
与 scores[1][0] 同行同列的三个元素都不比它大；
与 scores[1][1] 同行同列的三个元素中 score[1][0]、score[0][1] 比它大；
与 scores[1][2] 同行同列的三个元素都比它大；

提示：
1 <= scores.length, scores[row].length <= 500
0 <= scores[row][col] <= 10^4
请注意，该题有性能要求，暴力解法的用例通过率不高
###
class Solution:
    def __init__(self):
        self.matrix_col = []
        self.matrix_row = []

    @staticmethod
    def sort_list(list_sort: List[int]):
        template = sorted(list_sort)
        template = {x: y for y, x in enumerate(template)}
        return [template[x] for x in list_sort]

    def cmp_scores(self, scores: List[List[int]]) -> List[List[int]]:
        len_row = len(scores)
        len_col = len(scores[0])
        temp = [[] for _ in range(len_col)]
        result = [[0] * len_col for _ in range(len_row)]
        for row in scores:
            self.matrix_row.append(self.sort_list(row))
            for num, i in enumerate(row):
                temp[num].append(i)

        for col in temp:
            self.matrix_col.append(self.sort_list(col))

        for row in range(len_row):
            for col in range(len_col):
                count = len_row - self.matrix_row[row][col] + len_col - self.matrix_col[col][row]
                result[row][col] = count - 2
        return result
