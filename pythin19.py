#how to implement iterators in python code
class remotecontrol():
    def __init__(self):
            self.channels=["sony","bharat","sports"]
            self.index=-1
    def __iter__(self):
          return self
    def __next__(self):
          self.index+=1
          if self.index== len(self.channels):
                raise StopIteration
          return self.channels[self.index]
r=remotecontrol()
itr=iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

           