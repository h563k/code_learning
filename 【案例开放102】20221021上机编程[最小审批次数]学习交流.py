###
某公司各级部门之间的连接关系为一颗多叉树结构，每个节点表示一个部门（有两个属性：部门id和部门研究的技术分类tech），父节点表示上级部门；以样例1数据为例，连接关系如下：
https://oj.rnd.huawei.com/public/upload/d87db7e027.png
现给定各个部门的连接关系和tech，及你所在部门myDeptId，你需要查阅所有与你部门tech相同的其它部门的资料，查阅资料的审批流程如下：

·         查阅每个部门的资料都需要进行一次申请
·         假设你申请查阅部门B的资料，审批规则为：
·         如果你的部门是B的上级部门（含直接和间接），则不需要审批。
·         如果你的部门不是B的上级部门（含直接和间接），则需要你的上级部门逐层审批：
·         若B是你的上级部门（含直接和间接），则审批到B结束；
·         若B不是你的上级部门，则审批到距离两部门最近的同一个上级部门。

注：每审批一次审批次数加 1 。
请计算并返回累计的审批次数。
解答要求时间限制：1000ms, 内存限制：256MB

输入
首行是一个整数 num，表示部门数量，部门id从 0 到 num - 1，1 <= num <= 1000
接下来一行的整数序列techs表示这num个部门的技术分类，下标为部门id，1 <= techs[i] <= 20
然后一行是整数 row，表示部门上下级关系数据的行数，1 <= row <= 999
接下来row行，每行第一个数字表示一个部门id，第二个数字表示直接下级部门的数量，后面的数字表示直接下级部门id。

1 <= 直接下级部门的数量 <= 100
最后一行是你所在部门 myDeptId
输入保证部门id合法，且仅能构建一棵树
输出
一个整数，表示累计的审批次数
样例
输入样例 1
8

16 20 15 15 15 15 15 11
5
0 3 3 1 5
3 1 4
1 1 6
4 1 7
7 1 2
4

输出样例 1
5

提示样例 1
连接关系如题目图示：申请者id4的部门的tech为15，其它tech为15的部门有部门2，部门3, 部门5, 部门6
四次申请的审批如下：

l  查阅部门2，部门4是部门2的上级部门，不需要审批
l  查阅部门3，依次需要 部门3 审批，审批 1 次
l  查阅部门5，依次需要 部门3 -> 部门0 审批，审批 2 次
l  查阅部门6，依次需要 部门3 -> 部门0 审批，审批 2 次
因此累计审批次数为 5
输入样例 2

6
16 13 16 14 12 15
3
0 2 4 1
4 2 2 5
1 1 3
0
输出样例 2
0
提示样例 2
部门0的tech为16
tech同为16的节点是部门2，部门0是部门2的上级部门（间接上级），因此不需要审批。
###
from typing import List


class Node:
    def __init__(self, ind: int, tech: int):
        self.id = ind
        self.tech = tech
        self.child = []


class Solution:
    def __init__(self):
        self.node_dict = {}
        self.start_end = {}
        self.start = 0
        self.tech_list = []

    def dfs(self, root: Node):
        if root:
            self.start_end[root] = [self.start, 0]
            self.start += 1
            for child in root.child:
                self.dfs(child)
            self.start_end[root][1] = self.start

    def counts(self, node: Node, my_dept_id: int):
        count, temp = -1, []
        my_start, my_end = self.start_end[self.node_dict[my_dept_id]]
        start, end = self.start_end[node]
        for note, (note_start, note_end) in self.start_end.items():
            if note_start <= my_start and my_end <= note_end:
                temp.append(note)
        while temp:
            note_start, note_end = self.start_end[temp.pop()]
            count += 1
            if note_start <= start and end <= note_end:
                return count

    def get_approval_times(self, relations: List[List[int]], techs: List[int], my_dept_id: int) -> int:
        count = 0
        for ind, tech in enumerate(techs):
            temp = Node(ind, tech)
            self.node_dict[ind] = temp
            if tech == techs[my_dept_id]:
                self.tech_list.append(temp)
        for relation in relations:
            node = self.node_dict[relation[0]]
            for child in relation[2:]:
                node.child.append(self.node_dict[child])
        self.dfs(self.node_dict[0])
        for node in self.tech_list:
            count += self.counts(node, my_dept_id)
        return count



