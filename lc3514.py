class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        max_val = max(nums)
        bits = max(1, (max_val).bit_length()) + 1
        size = 1 << bits
        full = (1 << size) - 1

        patterns = []
        for b in range(bits):
            block = 1 << b
            pattern = 0
            pos = 0
            while pos < size:
                for _ in range(block):
                    if pos < size:
                        pattern |= (1 << pos)
                    pos += 1
                pos += block
            patterns.append(pattern)

        def shift_xor(mask, v):
            result = mask
            for b in range(bits):
                if v & (1 << b):
                    block = 1 << b
                    pat = patterns[b]
                    low = result & pat
                    high = result & (~pat & full)
                    result = (low << block) | (high >> block)
            return result

        distinct = set(nums)
        base_mask = 0
        for x in distinct:
            base_mask |= (1 << x)

        pair_mask = 0
        for v in distinct:
            pair_mask |= shift_xor(base_mask, v)

        triple_mask = 0
        for v in distinct:
            triple_mask |= shift_xor(pair_mask, v)

        return bin(triple_mask).count('1')
