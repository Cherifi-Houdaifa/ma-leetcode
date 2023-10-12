class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

# l3 = ListNode(0)
# l4 = ListNode(0)
# l5 = ListNode(9 , ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
# l6 = ListNode(9 , ListNode(9, ListNode(9, ListNode(9))))

# l7 = ListNode(5, ListNode(6))
# l8 = ListNode(5, ListNode(4, ListNode(9)))


def main(l1: ListNode, l2: ListNode):
    num1 = convertListToNum(l1)
    num2 = convertListToNum(l2)
    result = num1 + num2
    return convertNumToList(result)

def convertListToNum(l: ListNode):
    # input: 2 -> 4 -> 3
    # output: 342
    temp = l
    count = 0
    result: int = 0
    while temp:
        result += temp.val * pow(10, count)
        if (temp.next):
            temp = temp.next
        else:
            break
        count += 1
    return result

# need to optimize this
def convertNumToList(num: int):
    # input: 807
    # output: 7 -> 0 -> 8
    numList = str(num)
    head = None
    for i in numList:
        if head == None:
            head = ListNode(int(i))
        else:
            temp = ListNode(int(i), next=head)
            head = temp
    return head



main(l1, l2)



# def convertNumToList(num: int):
#     # input: 807
#     # output: 7 -> 0 -> 8

#     if (num == 0):
#         # just in case num is 0 and it can not be negative
#         return ListNode(0)

#     head = None

#     # add this because 807 - 800 = 7 (but i need 07 to add the 0 to the list)
#     numLength = len(str(num))

#     # imitate the insert function
#     while num > 0:
#         digit = getLastDigit(num)
#         num = num - (digit * pow(10, len(str(num)) - 1))

#         if (head == None):
#             head = ListNode(digit)
#         else:
#             temp = ListNode(digit, next=head)
#             head = temp
#         numLength -= 1
#         # this means that a 0 has been skipped so just add it
#         if (len(str(num)) < numLength):
#             # this defines how much zeros to add like in 10009998 we add 3 zeros
#             zeros = numLength - len(str(num))
#             for i in range(0, zeros):
#                 temp1 = ListNode(0, next=head)
#                 head = temp1
#             numLength -= zeros

#     # there is still zeros like in 1010 the last 0 will not be counter
#     # this will solve it (i hope)
#     while numLength > 0:
#         temp2 = ListNode(0, next=head)
#         head = temp2
#         numLength -= 1
#     return head


# def getLastDigit(num: int) -> int:
#     # input: 807
#     # output: 8
#     result = int(num / pow(10, len(str(num)) - 1))
#     return result

# main(l7, l8)
