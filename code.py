from collections import defaultdict
class Solution(object):
    def copyRandomList(self, head):
        clone = defaultdict(lambda: Node(0))
        clone[None] = None
        cur = head
        while cur:
            clone[cur].val = cur.val
            clone[cur].next = clone[cur.next]
            clone[cur].random = clone[cur.random]
            cur = cur.next
        return clone[head]



