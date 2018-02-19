class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        savedHead = head
        length = 0
        while head != None:
            length += 1
            head = head.next
        head = savedHead
        if n == length:
            return head.next
        nthFromBegin = length - n
        nodePoint = head
        while nthFromBegin > 1:
            nodePoint = nodePoint.next
            nthFromBegin -= 1
        nodePoint.next = nodePoint.next.next
        nodePoint = head
        return head


solution = Solution()
vals = [int(x) for x in input().split()]
lastNode = None
for val in vals:
    newNode = ListNode(val)
    if lastNode == None:
        head = lastNode = newNode
    else:
        lastNode.next = newNode
        lastNode = newNode
n = int(input())
head = solution.removeNthFromEnd(head, n)
while nodePoint != None:
    print(nodePoint.val)
    nodePoint = nodePoint.next
