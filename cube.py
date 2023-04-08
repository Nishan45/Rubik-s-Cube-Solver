#This is the cube class. This class contains Horizontal, Vertical and Face rotation of the cube.

import pygame

pygame.init()

def swap(a,b):
    return b,a

def rotate(direction,cube,n,ind):
    temp=[[0 for i in range(n)] for j in range(n)]
    
    for i in range (n):
        for j in range(n):
            temp[i][j]=cube[ind][j][i]
            
    cube[ind]=temp
    if direction==-1:
        for i in range(n):
            for j in range(n//2):
                cube[ind][j][i],cube[ind][n-1-j][i]=swap(cube[ind][j][i],cube[ind][n-1-j][i])
            
    if direction==1:
        for i in range(n):
            for j in range(n//2):
                cube[ind][i][j],cube[ind][i][n-1-j]=swap(cube[ind][i][j],cube[ind][i][n-1-j])
            

class Cube:
    def __init__(self,n):
        self.n=n
        self.cube=[]
        for i in range(6):
            l1=[]
            for j in range(self.n):
                l2=[]
                for k in range(self.n):
                    l2.append(i+1)
                l1.append(l2)
                
            self.cube.append(l1)

    def show(self,screen,colors):
        for i in range(6):
        
            for j in range(self.n*self.n):
                x=200+60*self.n*i+(j%self.n)*60
                y=200+(j//self.n)*60
                
                if i==4:
                    y-=self.n*60
                    x=200+self.n*60+(j%self.n)*60
                if i==5:
                    y+=self.n*60
                    x=200+self.n*60+(j%self.n)*60
                    
                pygame.draw.rect(screen,colors[self.cube[i][j//self.n][j%self.n]-1],(x,y,50,50))
                
    
    def vertical_rotate(self,direction,col,side=None):
        list=[4,1,5,3]
        if direction==-1:
            list.reverse()
        temp=[]
        for i in range(self.n):
            if list[0]==3:
                temp.append(self.cube[list[0]][self.n-1-i][self.n-1-col])
            else:
                temp.append(self.cube[list[0]][i][col])
                        
        for i in range(3):
            for j in range(self.n):
                
                if list[i]==3:
                    self.cube[list[i]][self.n-1-j][self.n-1-col]=self.cube[list[i+1]][j][col]
                elif list[i+1]==3:
                    self.cube[list[i]][j][col]=self.cube[list[i+1]][self.n-1-j][self.n-1-col]
                else:
                    self.cube[list[i]][j][col]=self.cube[list[i+1]][j][col]
                    
        for i in range(self.n):
            if list[3]==3:
                self.cube[list[3]][self.n-1-i][self.n-1-col]=temp[i]
            else:
                self.cube[list[3]][i][col]=temp[i]
            
        if side is not None: 
            if col==0:
                side=0
                if direction==1:
                    rotate(-1,self.cube,self.n,side)
                elif direction==-1:
                    rotate(1,self.cube,self.n,side)
                    
            elif col==self.n-1:
                side=2
                if direction==-1:
                    rotate(-1,self.cube,self.n,side)
                elif direction==1:
                    rotate(1,self.cube,self.n,side)  
    
    def horizontal_rotate(self,direction,row,side=None):
        list=[0,1,2,3]
        if direction==1:
            list.reverse()
        self.cube[list[0]][row],self.cube[list[1]][row],self.cube[list[2]][row],self.cube[list[3]][row]=self.cube[list[1]][row],self.cube[list[2]][row],self.cube[list[3]][row],self.cube[list[0]][row]
        
        if side is not None: 
            if row==0:
                side=4
                if direction==-1:
                    rotate(1,self.cube,self.n,side)
                if direction==1:
                    rotate(-1,self.cube,self.n,side)
            if row==self.n-1:
                side=5
                if direction==1:
                    rotate(1,self.cube,self.n,side)
                if direction==-1:
                    rotate(-1,self.cube,self.n,side)
    
    def face_rotate(self,direction,ind):
        l=[0,4,2,5]
        side=None
        if ind==0:
            side=3
        if ind==self.n:
            side=1
        temp=[]
        for i in range(self.n):
            temp.append(self.cube[0][i][ind])
            
        if direction==-1:
            for i in range(self.n):
                self.cube[0][i][ind]=self.cube[4][ind][self.n-1-i]
            for i in range(self.n):
                self.cube[4][ind][i]=self.cube[2][i][self.n-1-ind]
            for i in range(self.n):
                self.cube[2][i][self.n-1-ind]=self.cube[5][self.n-1-ind][self.n-1-i]
            for i in range(self.n):
                self.cube[5][self.n-1-ind][i]=temp[i]
            if ind==0:
                rotate(1,self.cube,self.n,3)
            if ind==self.n-1:
                rotate(-1,self.cube,self.n,1)
        
        if direction==1:
            for i in range(self.n):
                self.cube[0][i][ind]=self.cube[5][self.n-1-ind][i]
            for i in range(self.n):
                self.cube[5][self.n-1-ind][i]=self.cube[2][self.n-1-i][self.n-1-ind]
            for i in range(self.n):
                self.cube[2][i][self.n-1-ind]=self.cube[4][ind][i]
            for i in range(self.n):
                self.cube[4][ind][i]=temp[self.n-1-i]
            if ind==0:
                rotate(-1,self.cube,self.n,3)
            if ind==self.n-1:
                rotate(1,self.cube,self.n,1)
          
                            
    

                   
    
