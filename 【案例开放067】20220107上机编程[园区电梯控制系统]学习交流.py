###
某大楼有一部电梯，初始电梯内没有乘客，乘客出现顺序保存在数组 passengers 中，passengers[i]格式为from to，分别表示乘客所在的楼层和想去的楼层。
假设乘客按顺序一个一个出现，当前乘客 passengers[i] 进入电梯且电梯关门后，后一个乘客 passengers[i+1] 立刻出现并等待。
电梯搭载规则如下：
·         当电梯内无乘客时，立即去接当前等待乘客。
·         当电梯内有乘客时：
·         将电梯内乘客都送到之前，电梯不会改变运行方向。
·         若电梯经过当前等待乘客所在楼层、且运行方向与当前等待乘客想去的方向一致，就会顺路搭载当前等待乘客。
假设电梯能携带的乘客数量没有限制，请计算电梯运送完最后一个乘客时，总共运行了多少层的距离。
输入
首行两个整数num initFloor，分别表示乘客的个数和电梯初始所在的楼层，1 <= num <= 100，1 <= initFloor <= 100
接下来 num 行表示passengers信息，passengers[i]格式为from to，分别表示乘客所在的楼层和想去的楼层，1 <= from <= 100，1 <= to <= 100，from != to
输出
一个整数，表示电梯总共运行了多少层的距离
样例
输入样例 1

3 50
12 66
25 27
26 83

输出样例 1
109
提示样例 1

https://oj.rnd.huawei.com/public/upload/65d7c742e0.png电梯初始时位于50层，共有3个乘客依次出现。
首先电梯从50层下降到12层接上乘客0。运行距离：50-12=38
然后电梯从12层上升，到25层时顺路接上乘客1。运行距离：25-12=13
然后电梯从25层上升，到26层时顺路接上乘客2。运行距离：26-25=1
然后电梯从26层上升到27层，放下乘客1。运行距离：27-26=1
然后电梯从27层上升到66层，放下乘客0。运行距离：66-27=39
然后电梯从66层上升到83层，放下乘客2。运行距离：83-66=17
电梯运行总距离为：38+13+1+1+39+17=109

输入样例 2


4 50
50 10
40 20
30 100
30 100

 输出样例 2

270

提示样例 2

https://oj.rnd.huawei.com/public/upload/3cdae4eca6.pngstep3说明：
1.电梯下降到第30层时，因为乘客2并不顺路（方向相反），所以不会捎带上
step4说明：
1.电梯送完乘客0和1后（乘客1在第20层下电梯，乘客0在第10层下电梯），去30层接乘客2
2.乘客2上电梯后，乘客3在30层立刻出现并等待电梯（虽然乘客3和2都是计划从30层到100层，但乘客2进电梯关门后乘客3才出现，所以此时不会同时搭载乘客3）
后续处理：乘客2在100层下电梯后，电梯下降到30层接乘客3
###

from typing import List
from collections import deque
class Solution:
    def __init__(self):
        self.count = 0
        # 电梯内的乘客
        self.passenger = []

    def cal_distance(self, init_floor: int, passengers: List[List[int]]) -> int:
        # 第一位乘客坐电梯
        # final 为当前电梯要去的楼层
        passengers = deque(passengers)
        self.passenger.append(passengers.popleft())
        begin, final = self.passenger[0]
        self.count += abs(begin - init_floor)
        while self.passenger or passengers:
            lets_go = True
            print('电梯', self.passenger, '排队', passengers, '起点', begin, '终点', final, '行程', self.count)
            while lets_go and passengers:
                # 下一位乘客进入等待
                come_from, go_to = passengers.popleft()
                # 首先判断乘客是否能顺路带上
                # 条件一、方向一致
                if (final - begin) * (go_to - come_from) > 0:
                    # 条件二、电梯经过
                    if begin < come_from < final:
                        final = max(final, go_to)
                        self.passenger.append([come_from, go_to])
                        continue
                    elif begin > come_from > final:
                        final = min(final, go_to)
                        self.passenger.append([come_from, go_to])
                        continue
                lets_go = False
                passengers.appendleft([come_from, go_to])
            print('电梯', self.passenger, '排队', passengers, '起点', begin, '终点', final, '行程', self.count)
            # 不能带上，那么 电梯内的乘客会走光，直到电梯空掉
            self.count += abs(final - begin)
            self.passenger = []
            print('电梯', self.passenger, '排队', passengers, '起点', begin, '终点', final, '行程', self.count)
            # 更新目的地
            if passengers:
                temp = final
                begin, final = passengers.popleft()
                self.passenger = [begin, final]
                self.count += abs(temp - begin)
            print('电梯', self.passenger, '排队', passengers, '起点', begin, '终点', final, '行程', self.count)
        return self.count

init_floor = 50
passengers = [
    [50, 10],
    [40, 20],
    [30, 100],
    [30, 100],
]

sol = Solution()
sol.cal_distance(init_floor, passengers)
