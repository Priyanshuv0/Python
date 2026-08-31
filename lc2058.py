class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        a = []
        p = head
        i = 0

        while p.next and p.next.next:
            if (p.val < p.next.val > p.next.next.val) or (p.val > p.next.val < p.next.next.val):
                a.append(i + 1)
            p = p.next
            i += 1

        if len(a) < 2:
            return [-1, -1]

        mn = min(a[i] - a[i - 1] for i in range(1, len(a)))
        mx = a[-1] - a[0]

        return [mn, mx]
