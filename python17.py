# what is multi inheritance
# multi inheritance is the subclass that use two or more parent class as the element in
class father:
    def gardening(self):
        print("i love gardening")
class mother:
    def cooking(self):
        print("i love cooking")
class son(father,mother):
    def playing(self):
        print("i love playing")
s=son()
s.gardening()                                
s.cooking()
s.playing()