class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            if op == '+':
                record.append(record[len(record)-1]+record[len(record)-2])

            elif op == 'D':
                record.append(2*record[len(record)-1])

            elif op == 'C':
                record.pop()

            else:
                record.append(int(op))

        return sum(record)

        
        