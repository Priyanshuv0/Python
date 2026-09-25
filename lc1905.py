class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def parse(i):
            res = {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == '{':
                    sub, i = parse(i + 1)
                else:
                    sub = {expression[i]}
                    i += 1

                res = {a + b for a in res for b in sub}

            return res, i + 1 if i < len(expression) and expression[i] == '}' else i

        def solve(s):
            stack = [[]]
            i = 0

            while i < len(s):
                if s[i] == '{':
                    depth = 1
                    j = i + 1

                    while depth:
                        if s[j] == '{':
                            depth += 1
                        elif s[j] == '}':
                            depth -= 1
                        j += 1

                    sub = solve(s[i + 1:j - 1])
                    stack[-1].append(sub)
                    i = j
                elif s[i] == ',':
                    stack.append([])
                    i += 1
                else:
                    stack[-1].append({s[i]})
                    i += 1

            ans = set()

            for parts in stack:
                cur = {""}
                for part in parts:
                    cur = {a + b for a in cur for b in part}
                ans.update(cur)

            return ans

        return sorted(solve(expression))
