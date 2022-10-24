	# -*- coding: utf-8 -*-
"""RandomGrouping.ipynb

Automatically generated by Colaboratory.

Original file is located at-
    https://colab.research.google.com/drive/12xwTg_oSNM2wjyOYk2ifinietRRd9oKb
"""

import secrets
import sys
from tabulate import tabulate

GV = [
    "Trang",
    "Từ",
    "Yến",
    "Thanh",
    "Phúc",
    "Lâm",
    "Quốc",
]

K9 = [
    "Huy",
    "Thúy",
    #"Phi",
    "Kim Như",
    "Quỳnh Như",
    "Trân",
    "Khôi",
    "Phúc",
    #"Thịnh",
]

K10 = [
    "Thương",
    "Thảo",
    "Phong",
    "Hiệp",
    # "Phương",
    "Ngân",
    "Duyên",
    "Thắm",
    "Như",
    "Huyên",
    # "Giang",
    "Thùy",
    "Lộc"
]

K12A = [
    "Nghi",
    "Vân",
    "Tiên",
    "Thúy Nga",
    "Khơi Tâm",
    "Thúy",
    "Kiệt",
    "Hồng Ngọc",
    "Kim Ngọc",
    "Chi",
    "Linh",
    "Tân",
    "Trọng Tâm",
    "Gia Huy",
    "Minh",
]

K12B = [
    "Nhi",
    "Toàn",
    "Trúc",
    "Yến",
    "Khoa",
    "Nga Thới",
    "Lộc",
    "Thanh Tâm",
    "Hiên",
    "Thái",
    "Thanh",
    "Bảo"
]

K12 = K12A + K12B

GROUPS = {"GV": GV, "K9": K9, "K10": K10, "K12A": K12A, "K12B": K12B, "K12": K12}

def grouping(all_members: list, group_size: int) -> dict:
    """
    Divide class members into pairs/groups

    Note that if the number of all members is not divisible by
    the number of groups, there will be a group with fewer members

    group_size: number of members in a standard group
    all_members: an iterable containing all members of the class

    """
    groups = dict()
    all_members_size = len(all_members)
    remaining_members = all_members
    i = 1

    while remaining_members:
        group_name = "group " + str(i)
        remaining_members_size = len(remaining_members)
        size = min(remaining_members_size, group_size)
        members = secrets.SystemRandom().sample(remaining_members, k=size)

        groups[group_name] = members
        for mem in members:
            remaining_members.remove(mem)
        i += 1

    return groups

def main(argv):
    group_name, group_size = argv
    results = grouping(GROUPS[group_name.upper()], int(group_size))
    table = tabulate([(k,) + tuple(v) for k,v in results.items()])
    print(table)

if __name__ == '__main__':
    main(sys.argv[1:])
