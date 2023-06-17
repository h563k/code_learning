# 导入基本常见的库
from collections import *
from typing import *
from math import *
import re
from functools import wraps
import time
import copy


def timer(func):
    """this is outer clock function"""

    @wraps(func)  # --> 4
    def clocked(*args, **kwargs):  # -- 1
        """this is inner clocked function"""
        start_time = time.perf_counter()
        result = func(*args, **kwargs)  # --> 2
        time_cost = time.perf_counter() - start_time
        print(func.__name__ + " time_cost -> {}".format(time_cost))
        return result
    return clocked  # --> 3


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# if __name__ == "__main__":
#     from leetcode import *
