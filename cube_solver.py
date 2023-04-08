'''This is used for animation of the cube using matplotlib in 3 dimension.It will display each steps to solve the rubik's cube and the solution will also be written there
at the top of the figure '''


from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import cube
from matplotlib.animation import FuncAnimation
import kociemba
import copy
  
fig = plt.figure() 
plt.rcParams.update({'font.size':20})

sol=[]
moves={}
sequence=['1','2','3','4','5','6']

def get_cube(cub):
   # this funtion is used to copy the cube
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
    '''this function create a string of the cube which is needed since python's kociemba algorithm takes string as input so we need to crate a string of patterns of
    the cube'''
    
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
            
    s=s.replace(sequence[0],'L')
    s=s.replace(sequence[1],'F')
    s=s.replace(sequence[2],'R')
    s=s.replace(sequence[3],'B')
    s=s.replace(sequence[4],'U')
    s=s.replace(sequence[5],'D')
                 
    return s


def get_cube_pattern(sol):
  # this retunrs the sol in the form of list 
    patterns=[]
    for i in range(len(sol)):
        if sol[i]!=' ' and sol[i]!='2' and sol[i]!='3' and sol[i]!="'":
            t=sol[i]
            if ((i+1)<len(sol)) and (sol[i+1]=='2' or sol[i+1]=='3' or sol[i+1]=="'"):
                t+=sol[i+1]
                i+=1
            patterns.append(t)
    return patterns
                
def solve_cube(cub):
    global sol,moves
    
    s=stringfy(cub.cube)
    solution=kociemba.solve(s)
         
    sol=get_cube_pattern(solution)
    pattern=[get_cube(cub)]
    index=0
    
    for ind in range(len(solution)):    
        if solution[ind]=='U':
            d=-1
            n=1
            t=solution[ind]
            if ind+1<len(solution) and solution[ind+1]=="'":
                d=1
                t+=solution[ind+1]
            if ind+1<len(solution) and (solution[ind+1]=='2' or solution[ind+1]=='3'):
                n=int(solution[ind+1])
                t+=solution[ind+1]
                
            for i in range(n):
                cub.horizontal_rotate(d,0,4)
                c=get_cube(cub)
                pattern.append(c)
                moves[(stringfy(c),t)]=index
            index+=1
            
        elif solution[ind]=='D':
            d=1
            n=1
            t=solution[ind]
            if ind+1<len(solution) and solution[ind+1]=="'":
                d=-1
                t+=solution[ind+1]
            if ind+1<len(solution) and (solution[ind+1]=='2' or solution[ind+1]=='3'):
                n=int(solution[ind+1])
                t+=solution[ind+1]
            for i in range(n): 
                cub.horizontal_rotate(d,2,5)
                c=get_cube(cub)
                pattern.append(c)
                moves[(stringfy(c),t)]=index 
            index+=1  
            
        elif solution[ind]=='L':
            d=-1
            n=1
            t=solution[ind]
            if ind+1<len(solution) and solution[ind+1]=="'":
                d=1
                t+=solution[ind+1]
            if ind+1<len(solution) and (solution[ind+1]=='2' or solution[ind+1]=='3'):
                n=int(solution[ind+1])
                t+=solution[ind+1]
                
            for i in range(n):
                cub.vertical_rotate(d,0,0)
                c=get_cube(cub)
                pattern.append(c)
                moves[(stringfy(c),t)]=index
            index+=1
                        
        elif solution[ind]=='R':
            d=1
            n=1
            t=solution[ind]
            if ind+1<len(solution) and solution[ind+1]=="'":
                d=-1
                t+=solution[ind+1]
            if ind+1<len(solution) and (solution[ind+1]=='2' or solution[ind+1]=='3'):
                n=int(solution[ind+1])
                t+=solution[ind+1]
            for i in range(n):
                cub.vertical_rotate(d,2,2)
                c=get_cube(cub)
                pattern.append(c)
                moves[(stringfy(c),t)]=index
            index+=1
                
        elif solution[ind]=='B':
            d=-1
            n=1
            t=solution[ind]
            if ind+1<len(solution) and solution[ind+1]=="'":
                d=1
                t+=solution[ind+1]
            if ind+1<len(solution) and (solution[ind+1]=='2' or solution[ind+1]=='3'):
                n=int(solution[ind+1])
                t+=solution[ind+1]
            for i in range(n):
                cub.face_rotate(d,0)
                c=get_cube(cub)
                pattern.append(c)
                moves[(stringfy(c),t)]=index
            index+=1
        
        elif solution[ind]=='F':
            d=1
            n=1
            t=solution[ind]
            if ind+1<len(solution) and solution[ind+1]=="'":
                d=-1
                t+=solution[ind+1]
            if ind+1<len(solution) and (solution[ind+1]=='2' or solution[ind+1]=='3'):
                n=int(solution[ind+1])
                t+=solution[ind+1]
            for i in range(n):
                cub.face_rotate(d,2)
                c=get_cube(cub)
                pattern.append(c)
                moves[(stringfy(c),t)]=index
            index+=1
        
    return pattern
              
text='' 


# drawing code starts from here
def draw_edges(x,y,z,x1,y1,z1,ax):
       
    verts = [list(zip(x,y,z))]
    ax.add_collection3d(Poly3DCollection(verts,color='black'))
        
    verts = [list(zip(x1,y1,z1))]
    ax.add_collection3d(Poly3DCollection(verts,color='black'))

    temp=copy.deepcopy(x)
    x=copy.deepcopy(z)
    z=temp
        
    verts = [list(zip(x,y,z))]
    ax.add_collection3d(Poly3DCollection(verts,color='black'))
    
    temp=copy.deepcopy(x1)
    x1=copy.deepcopy(z1)
    z1=temp
        
    verts = [list(zip(x1,y1,z1))]
    ax.add_collection3d(Poly3DCollection(verts,color='black'))           
                
def plot_cube(cubc,colors):
    global sol,moves,text,ind
    
    ax=Axes3D(fig,auto_add_to_figure=False)
    fig.add_axes(ax)
    scale=0.29
    sp=stringfy(cubc.cube)
    
    for i in range(len(sol)):
        colour='black' 
        if (sp,sol[i]) in moves and  moves[(sp,sol[i])]==i:
            colour='red'
            if text!='':
                text.remove()
            text=ax.text2D(-0.1,0.4,sol[i],transform=ax.transAxes,color=colour) 
        if ind==0:
            if text!='':
                text.remove()
            text=ax.text2D(-0.1,0.4,'',transform=ax.transAxes,color=colour) 
            
        ax.text2D(-0.15+i*0.07,0.9,sol[i],transform=ax.transAxes,color=colour)
        
    cub=[]
    for i in range(6):
        l1=[]
        for j in range(3):
            l2=[]
            for k in range(3):
                l2.append(cubc.cube[i][j][k])
            l1.append(l2)
        cub.append(l1)
                
    cube.rotate(1,cub,3,0)
    cube.rotate(1,cub,3,1)
    cube.rotate(1,cub,3,2)
    cube.rotate(1,cub,3,2)
    cube.rotate(1,cub,3,3)
    cube.rotate(1,cub,3,3)
    cube.rotate(1,cub,3,5)
    
    l=3*scale+0.02
    x = [scale,0.01+scale,scale,scale+0.01]
    z = [l,l,0,0]
    y = [0,0,0,0]
    x1 = [2*scale+0.01,0.02+scale*2,scale*2+0.01,2*scale+0.02]
    z1 = [l,l,0,0]
    y1 = [0,0,0,0]
        
    draw_edges(x,y,z,x1,y1,z1,ax)
    draw_edges(y,x,z,y1,x1,z1,ax)
    draw_edges(x,z,y,x1,z1,y1,ax)
    
    x = [scale,0.01+scale,scale,scale+0.01]
    z = [l,l,0,0]
    y = [l,l,l,l]
    x1 = [2*scale+0.01,0.02+scale*2,scale*2+0.01,2*scale+0.02]
    z1 = [l,l,0,0]
    y1 = [l,l,l,l]
        
    draw_edges(x,y,z,x1,y1,z1,ax)
    draw_edges(y,x,z,y1,x1,z1,ax)
    draw_edges(x,z,y,x1,z1,y1,ax)

    for i in range(3):
        for j in range(3):
            a=j*0.3
            b=i*0.3
            x = [a,a+scale,a+scale,a]
            y = [b,b,b+scale,b+scale]
            z = [0,0,0,0]
                
            verts = [list(zip(x,y,z))]
            ax.add_collection3d(Poly3DCollection(verts,color=colors[cub[5][i][j]-1]))
        
    for i in range(3):
        for j in range(3):
            a=i*0.3
            b=j*0.3
            x = [a,a+scale,a+scale,a]
            y = [0,0,0,0]
            z = [b,b,b+scale,b+scale]
            
            verts = [list(zip(x,y,z))]
            ax.add_collection3d(Poly3DCollection(verts,color=colors[cub[0][i][j]-1]))

    for i in range(3):
        for j in range(3):
            a=i*0.3
            b=j*0.3
            z = [a,a+scale,a+scale,a]
            y = [b,b,b+scale,b+scale]
            x = [0,0,0,0]
            
            verts = [list(zip(x,y,z))]
            ax.add_collection3d(Poly3DCollection(verts,color=colors[cub[3][i][j]-1]))

    for i in range(3):
        for j in range(3):
            a=j*0.3
            b=i*0.3
            x = [a,a+scale,a+scale,a]
            z = [b,b,b+scale,b+scale]
            y = [0.89,0.89,0.89,0.89]
            
            verts = [list(zip(x,y,z))]
            ax.add_collection3d(Poly3DCollection(verts,color=colors[cub[2][i][j]-1]))

    for i in range(3):
        for j in range(3):
            a=j*0.3
            b=i*0.3
            z = [a,a+scale,a+scale,a]
            y = [b,b,b+scale,b+scale]
            x = [0.89,0.89,0.89,0.89]
            
            verts = [list(zip(x,y,z))]
            ax.add_collection3d(Poly3DCollection(verts,color=colors[cub[1][i][j]-1]))

    for i in range(3):
        for j in range(3):
            a=i*0.3
            b=j*0.3
            x = [a,a+scale,a+scale,a]
            y = [b,b,b+scale,b+scale]
            z = [0.89,0.89,0.89,0.89]
            
            verts = [list(zip(x,y,z))]
            ax.add_collection3d(Poly3DCollection(verts,color=colors[cub[4][i][j]-1]))
    ax.axis('off')
     
def start(cubs,cub):
    global ind
    
    ind=len(cubs)
    cub.cube=cubs[0]
    interval=1000
    
    def update(self):
        global ind
        colors=['blue','red','green','orange','yellow','white']
        if ind<len(cubs):
            cub.cube=cubs[ind]
        else:
            cub.cube=cubs[0]
        plot_cube(cub,colors)
        ind+=1
        if ind==1:
            anim.event_source.stop()
        if ind>=len(cubs):
            ind=0
            anim.event_source.stop()
               
    anim=FuncAnimation(fig,update,interval=interval)  
    
    def on_press(event):
        global ind
        
        if event.key=='shift':
            anim.event_source.stop()
        if event.key=='enter':
            anim.event_source.start()
        if event.key=='r':
            ind=len(cubs)
                               
    fig.canvas.mpl_connect('key_press_event',on_press)
    plt.show()
    

if __name__=='__main__':
    cubd=cube.Cube(3)
    cubs=[copy.deepcopy(cubd.cube)]
    
    
    start(cubs,cubd)
