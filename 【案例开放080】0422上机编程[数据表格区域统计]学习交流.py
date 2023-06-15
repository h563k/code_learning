###
Excel工作表中对选定区域的数值进行统计的功能非常实用。仿照Excel的这个功能，请对给定表格中选中区域中单元格进行求和统计，并输出统计结果。
为简化统计，假设当前输入中每个单元格内容仅为数字或公式两种。
l  如果为数字，则是一个非负整数，形如 0、11
l  如果为公式，则固定以=开头，且仅包含下面三种情况：
Ø  等于某单元格的值，形如=B12
Ø  两个单元格的双目运算（仅为 + 或 -），形如=C1-C2、C10+B2
Ø  单元格和数字的双目运算（仅为 + 或 -），形如=B12+1、=100-B12
公式不存在嵌套，例如 =C1-C2，其中C1和C2单元格的内容只会是数字，不会是公式。
公式内容都是合法的，例如不存在“=C+2”,“=C1-C2+B3”,“=5”,“=1+10”； 内容中不存在空格、括号
输入

第一行两个整数 rows cols，表示给定表格区域的行数和列数， 1 <= rows <= 20，1 <= cols <= 26
接下来 rows 行，每行 cols 个以空格分隔的字符串，表示给定表格 values 的单元格内容
最后一行输入的字符串，表示给定的选中区域，形如A1:C2

l  表格的行号 1~20，列号 A~Z，例如单元格 B3 对应 values[2][1]
l  输入的单元格内容（含公式）中的数字均为十进制，值范围 [0, 100]
l  选中区域: 冒号左侧单元格表示选中区域的左上角，右侧表示右下角，如可以为 B2:C10、B2:B5、B2:Y2、B2:B2，无类似 C2:B2、C2:A1 的输入

输出
一个整数，表示选中区域的数值之和
样例
输入样例 1

5 3
10 12 =C5
15 5 6
7 8 =3+C2
6 =B2-A1 =C2
7 5 3

B2:C4

输出样例 1
29

提示样例 1
给定表格内容为5行3列，各单元格的输入数据及计算后数值，表示如下：
https://oj.rnd.huawei.com/public/upload/8a370809dd.png

其中几个单元格内容为公式，这几个单元格的值计算过程如下：
C1 = C5 = 3
C3 = 3+C2 = 3+6 = 9
B4 = B2-A1 = 5-10 = -5
C4 = C2 = 6

选中区域 B2:C4 包含6个单元格（图中蓝色区域），统计结果为：5 + 8 - 5 + 6 + 9 + 6 = 29

输入样例 2

1 3
1 =A1+C1 3
A1:C1
输出样例 2
8

提示样例 2
选定区域为整行。B1单元格按公式计算为4，结果为1+4+3=8
###
class Solution:
    def __init__(self):
        self.dict = {x: y for y, x in enumerate(string.ascii_uppercase)}
        self.values = []
        self.sum = 0

    def get_sum(self, values: List[List[str]], sum_area: str) -> int:
        self.values = [value[0].split(' ') for value in values]
        # 能整数处理的全部整数处理
        temp = []
        for row, value in enumerate(self.values):
            for col, val in enumerate(value):
                if not val.isdigit():
                    temp.append([row, col])
        # 循环处理内容
        while temp:
            row, col = temp.pop(0)
            value = self.values[row][col].strip('=')
            # 我们把匹配项全部拿出来
            match = re.findall('([A-Z]\d+|\d+)([+|-]*)', value)
            temp_str = ''
            process = True
            # 查找匹配项的值
            for match_num, cells in enumerate(match):
                item, func = cells
                if item.isdigit():
                    temp_str = temp_str + item + func
                else:
                    col_init, row_init = re.findall('([A-Z])(\d+)', item)[0]
                    cell = self.values[int(row_init) - 1][self.dict[col_init]]
                    temp_str = temp_str + cell + func
            if process:
                self.values[row][col] = str(eval(temp_str))
        start, end = sum_area.split(':')
        start_col, start_row = re.findall('([A-Z])(\d+)', start)[0]
        end_col, end_row = re.findall('([A-Z])(\d+)', end)[0]
        start_col, start_row = self.dict[start_col], int(start_row)
        end_col, end_row = self.dict[end_col], int(end_row)
        for j in range(start_col, end_col + 1):
            for i in range(start_row, end_row + 1):
                self.sum += int(self.values[i - 1][j])
        return self.sum
values = [
    ['10 12 =C5'],
    ['15 5 6'],
    ['7 8 =3+C2'],
    ['6 =B2-A1 =C2'],
    ['7 5 3'],
]

sum_area = 'B2:C4'
sol = Solution()
sol.get_sum(values, sum_area)
