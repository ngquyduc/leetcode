class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        prev_num = {
            '0': '9',
            '1': '0',
            '2': '1',
            '3': '2',
            '4': '3',
            '5': '4',
            '6': '5',
            '7': '6',
            '8': '7',
            '9': '8'
        }
        next_num = {
            '0': '1',
            '1': '2',
            '2': '3',
            '3': '4',
            '4': '5',
            '5': '6',
            '6': '7',
            '7': '8',
            '8': '9',
            '9': '0'
        }
        visited = set(deadends)
        pendings = deque()
        turns = 0
        if "0000" in visited:
            return -1

        pendings.append("0000")
        visited.add("0000")

        while pendings:
            for _ in range(len(pendings)):
                current = pendings.popleft()

                if current == target:
                    return turns

                for wheel in range(4):
                    new = list(current)
                    new[wheel] = next_num[new[wheel]]
                    new_str = "".join(new)

                    if new_str not in visited:
                        pendings.append(new_str)
                        visited.add(new_str)

                    new = list(current)
                    new[wheel] = prev_num[new[wheel]]
                    new_str = "".join(new)

                    if new_str not in visited:
                        pendings.append(new_str)
                        visited.add(new_str)
            turns += 1
        return -1