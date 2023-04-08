# it is used to solve the cube. It contains a virtual cube which we can scramble by keyboard buttons and solves it using python's kociemba module. It uses python's pygame module.

import kociemba
import cube
import pygame
import cube_solver
import copy

pygame.init()

clock=pygame.time.Clock()
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
yellow=(255,255,0)
blue=(0,0,128)
orange=(255,130,0)
black=(0,0,0)

def get_cube(cub):
    c=[]
    for i in range(6):
            l1=[]
            for j in range(cub.n):
                l2=[]
                for k in range(cub.n):
                    l2.append(cub.cube[i][j][k])
                l1.append(l2)
            c.append(l1)
    return c

def stringfy(cub):
    s=""
    n=len(cub[0][1])
    
    for i in range(n):
        for j in range(n):
            s+=str(cub[4][i][j])
            
        
    for i in range(n):
        for j in range(n):
            s+=str(cub[2][i][j])
            
            
    for i in range(n):
        for j in range(n):
            s+=str(cub[1][i][j])
    
    for i in range(n):
        for j in range(n): 
            s+=str(cub[5][i][j])
    
    for i in range(n):
        for j in range(n): 
            s+=str(cub[0][i][j])
            
    
    for i in range(n):
        for j in range(n):
            s+=str(cub[3][i][j])
            
    s=s.replace(cube_solver.sequence[0],'L')
    s=s.replace(cube_solver.sequence[1],'F')
    s=s.replace(cube_solver.sequence[2],'R')
    s=s.replace(cube_solver.sequence[3],'B')
    s=s.replace(cube_solver.sequence[4],'U')
    s=s.replace(cube_solver.sequence[5],'D')
                 
    return s


def solve(cub,colors):
    
    screen_widht=1000
    screen_height=800
    cur=None
    screen=pygame.display.set_mode((screen_widht,screen_height))
    display=True
    h,v=0,0
    scramble=stringfy(cub.cube)
    solution=[]
    colors_c=['blue','red','green','orange','yellow','white']

    solving=False
    ind=0   
    s=[]         
    while display:
        screen.fill(black)
        cub.show(screen,colors)
        
        if len(solution)>0:
            
            if solution[ind]=='U':
                d=-1
                n=1
                if ind+1<len(solution) and solution[ind+1]=="'":
                    d=1
                if ind+1<len(solution) and (solution[ind+1]=='2' or solution[ind+1]=='3'):
                    n=int(solution[ind+1])
                    
                for i in range(n):
                    cub.horizontal_rotate(d,0,4)
                
            elif solution[ind]=='D':
                d=1
                n=1
                if ind+1<len(solution) and solution[ind+1]=="'":
                    d=-1
                if ind+1<len(solution) and (solution[ind+1]=='2' or solution[ind+1]=='3'):
                    n=int(solution[ind+1])
                for i in range(n): 
                    cub.horizontal_rotate(d,2,5)   
                
            elif solution[ind]=='L':
                d=-1
                n=1
                if ind+1<len(solution) and solution[ind+1]=="'":
                    d=1
                if ind+1<len(solution) and (solution[ind+1]=='2' or solution[ind+1]=='3'):
                    n=int(solution[ind+1])
                    
                for i in range(n):
                    cub.vertical_rotate(d,0,0)
                           
            elif solution[ind]=='R':
                d=1
                n=1
                if ind+1<len(solution) and solution[ind+1]=="'":
                    d=-1
                if ind+1<len(solution) and (solution[ind+1]=='2' or solution[ind+1]=='3'):
                    n=int(solution[ind+1])
                for i in range(n):
                    cub.vertical_rotate(d,2,2)
                    
            elif solution[ind]=='B':
                d=-1
                n=1
                if ind+1<len(solution) and solution[ind+1]=="'":
                    d=1
                if ind+1<len(solution) and (solution[ind+1]=='2' or solution[ind+1]=='3'):
                    n=int(solution[ind+1])
                for i in range(n):
                    cub.face_rotate(d,0)
            
            elif solution[ind]=='F':
                d=1
                n=1
                if ind+1<len(solution) and solution[ind+1]=="'":
                    d=-1
                if ind+1<len(solution) and (solution[ind+1]=='2' or solution[ind+1]=='3'):
                    n=int(solution[ind+1])
                for i in range(n):
                    cub.face_rotate(d,2)
            
            if ind>=len(solution)-1:
                
                solution=[]
                ind=0
                solving=False
                
        ind+=1
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                display=False
            if event.type==pygame.KEYDOWN:
                
                if event.key==pygame.K_1:
                    ind=0
                    solving=True
                    scramble=stringfy(cub.cube)
                    cur=copy.deepcopy(cub)
                    print(scramble)
                    solution=kociemba.solve(scramble)   
                    cube_solver.sol=solution
                    print(solution)
                    
                    
                if event.key==pygame.K_w:
                    h=0
                if event.key==pygame.K_x:
                    h=2
                if event.key==pygame.K_a:
                    v=0
                if event.key==pygame.K_d:
                    v=2
                if event.key==pygame.K_g:
                    cube_solver.fig=cube_solver.plt.figure(1)
                    cube_solver.sol=[]
                    cube_solver.plot_cube(cub,colors_c)
                    cube_solver.plt.show()
                    
                if event.key==pygame.K_h:
                    
                    if cur is None:
                        cur=copy.deepcopy(cub)
                    cube_solver.fig=cube_solver.plt.figure(1)
                    cube_solver.sol=[]
                    cube_solver.plot_cube(cur,colors_c)
                    cube_solver.fig=cube_solver.plt.figure(2)
                    
                    pattern=cube_solver.solve_cube(cur)
                    cube_solver.start(pattern,cur) 
                    
                    
                    cur=None 
                    
                if event.key==pygame.K_UP:
                    cub.vertical_rotate(1,v,0)
                    
                elif event.key==pygame.K_DOWN:
                    cub.vertical_rotate(-1,v,0)
                    
                elif event.key==pygame.K_LEFT:
                    cub.horizontal_rotate(-1,h,0)
                    
                elif event.key==pygame.K_RIGHT:
                    cub.horizontal_rotate(1,h,4)
                    
        if solving:
            clock.tick(10)
        pygame.display.update()
        
        
if __name__=='__main__':
    cub=cube.Cube(3)
    colors=[blue,red,green,orange,yellow,white]
    solve(cub,colors)
