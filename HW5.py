##Exercise 1
class Player:
    Life = 3
    def heal(self,Life):
        Life += 1
        return Life
    def damage(self,Life):
        Life -= 1
        return Life 

class Game:
    def Player1(self):
        return Player()
    def Player2(self):
        return Player()

    def Cheat(self,Player1, Player2):
        return Player1.heal and Player2.damage

##Exercise 2
class Empty :
    def IsEmpty (self):
        return True
    def __rlshift__ (self,v):
        return Node (v,self)
    def Sum (self):
        return 0
    def Length (self):
        return 0

class Node :
    def IsEmpty (self): 
        return False
    def Head (self): 
        return self.head
    def Tail (self): 
        return self.tail
    def __init__ (self,x,xs):
        self.head = x
        self.tail = xs
    def __rlshift__ (self,v):
        return Node (v,self)
    def Sum (self):
        return self.head + self.tail.Sum()
    def Length (self):
        return 1 + self.tail.Length()

Empty = Empty ()

l = 5 << (9 << (-1 << (Empty)))


##Exercise 3
class Empty :
    def IsEmpty (self):
        return True
    def __rlshift__ (self,v):
        return Node (v,self)
    def Sum (self):
        return 0
    def Length (self):
        return 0
    def Map (self,f):
        return self
    def Filter (self,p):
        return self


class Node :
    def IsEmpty (self): 
        return False
    def Head (self): 
        return self.head
    def Tail (self): 
        return self.tail
    def __init__ (self,x,xs):
        self.head = x
        self.tail = xs
    def __rlshift__ (self,v):
        return Node (v,self)
    def Sum (self):
        return self.head + self.tail.Sum()
    def Length (self):
        return 1 + self.tail.Length()
    def Map (self,f):
        return Node(f(self.head),self.tail.Map(f))
    def Filter (self,p):
        xs = self.tail.Filter(p)
        if p(self.head):
            return Node(self.head,xs)
        else:
            return xs


Empty = Empty ()

l = 5 << (9 << (-1 << (Empty)))

##Exercise 4
class Empty :
    def IsEmpty (self):
        return True
    def __rlshift__ (self,v):
        return Node (v,self)
    def Sum (self):
        return 0
    def Length (self):
        return 0
    def Map (self,f):
        return self
    def Filter (self,p):
        return self
    def Fold (self,f,z):
        return z

class Node :
    def IsEmpty (self): 
        return False
    def Head (self): 
        return self.head
    def Tail (self): 
        return self.tail
    def __init__ (self,x,xs):
        self.head = x
        self.tail = xs
    def __rlshift__ (self,v):
        return Node (v,self)
    def Sum (self):
        return self.head + self.tail.Sum()
    def Length (self):
        return 1 + self.tail.Length()
    def Map (self,f):
        
        lambda(x,2), x + 2
        
        return Node(f(self.head),self.tail.Map(f))
    def Filter (self,p):
        xs = self.tail.Filter(p)
        if p(self.head):
            return Node(self.head,xs)
        else:
            return xs
    def Fold(self,f,z):
        return f(self.head,self.tail.Fold(f,z)) 


Empty = Empty ()

l = 5 << (9 << (-1 << (Empty)))