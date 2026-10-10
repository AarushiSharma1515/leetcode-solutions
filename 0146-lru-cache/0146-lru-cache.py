from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        super(LRUCache, self).__init__()
        self.capacity=capacity
        

    def get(self, key):
        if key in self:
            value = self.pop(key)
            self[key]=value
            return value
        else:
            return -1

    def put(self, key, value):
        if key in self:
            self.pop(key)
        self[key] = value
        if len(self)>self.capacity:
            self.popitem(last=False)
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)