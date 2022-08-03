class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """
        def pathtraversal(edges,_path,node,distance):
            #print("path traversal", _path)
            #print(node, edges[node])
        
            if (node != -1 and _path[node] == -1):
                _path[node] = distance
                pathtraversal(edges,_path,edges[node],distance+1)
        
            return _path

        

        #print("functiion call")
        _path1 = [-1] * len(edges)
        _path2 = [-1] * len(edges)

        _path1=pathtraversal(edges,_path1,node1,0)
        _path2=pathtraversal(edges,_path2,node2,0)

        #print(_path1)
        #print(_path2)
    
        ans=-1
        minimumpath = float('inf')
        for i in range(len(edges)):
            if _path1[i] > -1 and _path2[i] > -1 and max(_path1[i],_path2[i]) < minimumpath:
                minimumpath = max(_path1[i],_path2[i])
                print(minimumpath)
                ans = i

        return ans
        