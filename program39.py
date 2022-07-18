class que:
    def __init__(self,max):
        self.a=[]
        self.max=max
    def enque(self):
        if(len(self.a)>=self.max):
            print("que is full")
        else:
            self.a.append(int(input("enter the number:")))
    def deque(self):
        if(len(self.a)==0):
            print("que is empty")
        else:
            self.a.pop(0)
    def display(self):
        for i in self.a:
            print(i,end=" ")
q=que(int(input("enter the size of queue:")))
q.enque()
q.enque()
q.display()
q.deque()
q.display()


