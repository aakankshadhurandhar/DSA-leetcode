class Solution(object):

    def fill(self,image,sr,sc,color,curr):
        #boundary condition
        if sr <0 or sc<0 or sr>=len(image) or sc>=len(image[0]):
            return 
        # check for last element is notequal to curr eleemnt
        if curr!=image[sr][sc]:
            return 
        image[sr][sc]=color
        # now go all directions
        #right
        self.fill(image,sr,sc+1,color,curr)
        #left
        self.fill(image,sr,sc-1,color,curr)
        #up
        self.fill(image,sr+1,sc,color,curr)
        #down
        self.fill(image,sr-1,sc,color,curr)


        

    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc]==color:
            return image
        self.fill(image, sr, sc, color,image[sr][sc])
        return image



        