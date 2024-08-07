class RandomizedSet(object):

    def __init__(self):
        self.delete_random_map={}
        self.delte_random_list=[]
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.delete_random_map:
            self.delete_random_map[val]=len(self.delte_random_list)
            self.delte_random_list.append(val)
            return True
        else:
            return False
        
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if not val in self.delete_random_map:
            return False
        else:
            last_element_list=self.delte_random_list[-1]
            index_ele_to_remove= self.delete_random_map[val]
            self.delete_random_map[last_element_list]=index_ele_to_remove
            self.delte_random_list[index_ele_to_remove]=last_element_list
            self.delte_random_list[-1]=val
            self.delte_random_list.pop()
            self.delete_random_map.pop(val)

            return True
        
        

        

    def getRandom(self):
        """
        :rtype: int
        """
        
        return random.choice(self.delte_random_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()