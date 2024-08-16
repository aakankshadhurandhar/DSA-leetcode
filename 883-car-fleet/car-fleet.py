class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        stack = []
        for pos, vel in sorted(zip(position, speed))[::-1]:
            dist = float(target - pos)
            print(dist / vel)
            if not stack:
                stack.append(dist / vel)     
            elif dist / vel > stack[-1]:
                stack.append(dist / vel)
        return len(stack)


        