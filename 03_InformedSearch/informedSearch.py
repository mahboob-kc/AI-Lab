def bfs(x):
	pc=0
	f.append(x)
	print("Frontier: ",f,"\nExplored: ",e)
	x=f.pop()
	e.append(x)
	while(x!=gol):
		m=h[g[x][0]]
		for i in g[x]:
			f.append(i)
			if h[i]<=m:
				y=i
				m=h[i]
		print("Frontier: ",f,"\nExplored: ",e)
		pc+=p[(x,y)]
		x=y
		f.remove(x)
		e.append(x)	
		if (x==gol):
			print("Frontier: ",f,"\nExplored: ",e)
			print("path cost: ",pc)
			print("goal node reached")
			break

def astar(x):
	pc=0
	f.append(x)
	print("Frontier: ",f,"\nExplored: ",e)
	x=f.pop()
	e.append(x)
	while(x!=gol):
		temp=g[x][0]
		m=h[temp]+p[(x,temp)]
		for i in g[x]:
			f.append(i)
			c=h[i]+p[(x,i)]
			if c<=m:
				y=i
				m=c
		print("Frontier: ",f,"\nExplored: ",e)
		pc+=p[(x,y)]
		x=y
		f.remove(x)
		e.append(x)	
		if (x==gol):
			print("Frontier: ",f,"\nExplored: ",e)
			print("path cost: ",pc)
			print("goal node reached")
			break

s=input("enter the nodes: ")
g={}
h={}
p={}
for i in s.split():
	t=input("enter the nodes adjacent to "+i+" : ")
	g[i]=[j for j in t.split()]
	h[i]=int(input("enter heuristic value of "+i+" : "))
	for j in t.split():
		p[(i,j)]=int(input("enter path cost between "+i+" and "+j+" : "))
	print()
ini=input("enter the initial node: ")
gol=input("enter the goal node: ")
f=[]
e=[]
print("bfs:")
bfs(ini)
f=[]
e=[]
print("a*:")
astar(ini)
