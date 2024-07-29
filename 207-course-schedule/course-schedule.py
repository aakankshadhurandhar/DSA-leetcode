class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph=[[] for _ in range(numCourses)]
        for course,prerequisite in prerequisites:
            graph[prerequisite].append(course)
        print(graph)
        #indgree array
        indgree=[0]*numCourses
        for neighbours in graph:
            for neighbour in neighbours:
                indgree[neighbour]+=1
        queue=deque()
        for i in range(numCourses):
            if indgree[i]==0:
                queue.append(i)
        order=[]
        while queue:
            curr_course=queue.popleft()
            order.append(curr_course)
            for neighbour in graph[curr_course]:
                indgree[neighbour]-=1
                if indgree[neighbour]==0:
                    queue.append(neighbour)
        print(order)
        return len(order)==numCourses
            
                



        