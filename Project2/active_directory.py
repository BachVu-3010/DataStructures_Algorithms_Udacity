class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):

    answer = user in group.users

    sub_groups = group.get_groups()

    for sub_group in sub_groups:
        answer |= is_user_in_group(user, sub_group)

    return answer


# Test_cases
"""
Tests
Group Structure:
    Parent
    |--Child1
    |  `--+--SubChild11
    |     `--SubChild12
    `--Child2
    `--+--SubChild21
        `--SubChild22
Description:
    Each Group contains 2 children
"""


# Groups
parent = Group("parent")

child1 = Group("child1")
child2 = Group("child2")

sub_child11 = Group("subchild11")
sub_child12 = Group("subchild12")

sub_child21 = Group("subchild21")
sub_child22 = Group("subchild22")

# Users
parent_user_1 = "parent_user_1"
child1_user_1 = "child1_user_1"
child2_user_1 = "child2_user_1"
sub_child11_user_1 = "sub_child11_user_1"
sub_child12_user_1 = "sub_child12_user_1"
sub_child21_user_1 = "sub_child21_user_1"
sub_child22_user_1 = "sub_child22_user_1"

parent_user_2 = "parent_user_2"
child1_user_2 = "child1_user_2"
child2_user_2 = "child2_user_2"
sub_child11_user_2 = "sub_child11_user_2"
sub_child12_user_2 = "sub_child12_user_2"
sub_child21_user_2 = "sub_child21_user_2"
sub_child22_user_2 = "sub_child22_user_2"

parent.add_user(parent_user_1)
parent.add_user(parent_user_2)

parent.add_group(child1)
child1.add_user(child1_user_1)
child1.add_user(child1_user_2)

parent.add_group(child2)
child2.add_user(child2_user_1)
child2.add_user(child2_user_2)

child1.add_group(sub_child11)
sub_child11.add_user(sub_child11_user_1)
sub_child11.add_user(sub_child11_user_2)

child1.add_group(sub_child12)
sub_child12.add_user(sub_child12_user_1)
sub_child12.add_user(sub_child12_user_2)

child2.add_group(sub_child21)
sub_child21.add_user(sub_child21_user_1)
sub_child21.add_user(sub_child21_user_2)

child2.add_group(sub_child22)
sub_child22.add_user(sub_child22_user_1)
sub_child22.add_user(sub_child22_user_2)


# Parent1 in Parent
print("Pass" if (is_user_in_group(parent_user_1, parent) == True) else "Fail")

# Parent2 in Parent
print("Pass" if (is_user_in_group(parent_user_2, parent) == True) else "Fail")

# Child1_1 in Parent
print("Pass" if (is_user_in_group(child1_user_1, parent) == True) else "Fail")
