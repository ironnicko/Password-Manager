class paper:
    def __init__(self,name,password,university):
        self._name=name
        self._password=password
        self._university=university
        self._accounts=[(self._name,self._password,self._university)]
        print('Account created for '+self._name)
        self.save()
        paper.load_data()
    def save(self):
        with open('Cred.txt','a') as zuccini:
            for i in self._accounts:
                print(self._name,self._password,self._university,file=zuccini)
    @staticmethod
    def load_data():
        with open('Cred.txt','r') as ano:
            for line in ano:
                un, passwo, univ = tuple(line.strip('\n').split())
                return (f'Username:{un} \n Password:{passwo} \n University:{univ}')


if __name__ == '__main__':
    while True:
        a=input('Enter your Name:')
        b=input('Enter Your Password:')
        c=input('Enter University Name(without spaces):')
        dude = paper(a,b,c)
        if int(input('Press 0 to stop:'))==0:
            break
