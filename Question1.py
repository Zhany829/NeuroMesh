class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        def find_next_index(source_index, target_index):
            while source_index < len(source) and target_index < len(target):
                if source[source_index] == target[target_index]:
                    target_index += 1
                source_index += 1
            return target_index

        source_length = len(source)
        target_length = len(target)
        subsequence_count = 0
        target_index = 0

        while target_index < target_length:
            new_target_index = find_next_index(0, target_index)
            if new_target_index == target_index:
                return -1
            target_index = new_target_index
            subsequence_count += 1

        return subsequence_count
