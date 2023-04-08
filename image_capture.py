import cv2
import cube
import test
import cube_solver
import copy
from datetime import datetime

cube_white=(255,255,255)
cube_red=(255,0,0)
cube_green=(0,255,0)
cube_yellow=(255,255,0)
cube_blue=(0,0,255)
cube_orange=(255,130,0)

cube_colors=[cube_blue,cube_red,cube_green,cube_orange,cube_yellow,cube_white]
animation_colors=['blue','red','green','orange','yellow','white']

white=(255,255,255)
red=(0,0,255)
green=(0,255,0)
yellow=(0,255,255)
blue=(255,0,0)
orange=(0,130,255)
black=(0,0,0)

def inter_change_coloums(cube,ind,n):
    for i in range(n):
        for j in range(n//2):
            val=cube[ind][i][j]
            cube[ind][i][j]=cube[ind][i][n-1-j]
            cube[ind][i][n-1-j]=val
            
def color_detect(h,s,v):
    if (h>=0 and h<=100 and s<=70 and v<200):
        return red,'r'
    if (h>=10 and s<=110 and v>=200):
        return orange,'o'
    if (h<=120 and s>110 and v>=200):
        return yellow,'y'
    if (h>=30 and h<=160 and s>=100):
        return green,'g'
    if (h>=130 and h<=200 and s<=100):
        return blue,'b'
    return white,'w'

def capture_cube():

    cap=cv2.VideoCapture(0)
    cv2.namedWindow('frame')
    boxes=[[400+x*120,180+120*y] for x in range(3) for y in range(3)]
    box_width=40  
    cub=cube.Cube(3)

    cub_pos=[[100+x*40,100+40*y,[]] for x in range(3) for y in range(3)]
    cub_width=40
    
    values=[]
    color_numbers={'b':1,'r':2,'g':3,'o':4,'y':5,'w':6}
    last_detected=None
    alert=''  
    text_color=green  
           
    while True:
        ret,image=cap.read()
        
        image=cv2.resize(image,(1000,600))
        if last_detected is not None and (datetime.now()-last_detected).total_seconds()<=2:
            cv2.putText(img=image,text=alert,org=(50,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=text_color,thickness=2,lineType=cv2.LINE_AA)
     
        hsv=[]
        for x,y in boxes:
            l=box_width//2
            color,ex=color_detect(image[y+l][x+l][0],image[y+l][x+l][1],image[y+l][x+l][2])
            cv2.rectangle(image,(x,y),(x+box_width,y+box_width),color,5) 
            hsv.append(image[y+l][x+l])
                
        for x,y,color in cub_pos:
            l=cub_width
            cv2.rectangle(image,(x,y),(x+l,y+l),black,2)
            if len(color)>0:
                cv2.rectangle(image,(x+2,y+2),(x+l-2,y+l-2),color,-1)
              
        cv2.imshow('frame',image)
        cv2.waitKey(1)
        
        k=cv2.waitKey(1) & 0xFF
        if k==ord('e'):
            break
        
        if k==ord('s'):
            cur=copy.deepcopy(cub)
            try:
                cube_solver.solve_cube(cur)
            except:
                print('cube is invalid')
                last_detected=datetime.now()
                alert='cube is invalid'
                text_color=red
            else:
                test.solve(cur,cube_colors)
                   
        
        if k==ord('n'):
            
            cube_solver.fig=cube_solver.plt.figure(1)
            cube_solver.sol=[]
            cube_solver.plot_cube(cub,animation_colors)
            cube_solver.plt.show()
            
        if k==ord('m'):
    
            cube_solver.fig=cube_solver.plt.figure(1)
            cube_solver.sol=[]
            cube_solver.plot_cube(cub,animation_colors)
            
            cube_solver.fig=cube_solver.plt.figure(2)
            cur=copy.deepcopy(cub)
            last_detected=None
            try:
                patterns=cube_solver.solve_cube(cur)
            except:
                print('cube is invalid')
                last_detected=datetime.now()
                alert='cube is invalid'
                text_color=red
            else:
                cube_solver.start(patterns,cur)
            
            
        if k==ord('i'):
            values=[]
            for i in range(9):
                color,ex=color_detect(hsv[i][0],hsv[i][1],hsv[i][2])
                cub_pos[i][2]=color
                values.append(color_numbers[ex])
                
        if k==ord('u'):
            if len(values)>0:
                for i in range(9):
                    cub.cube[4][i//3][i%3]=values[i]
                    cub_pos[i][2]=[]
                cube.rotate(1,cub.cube,3,4)
                inter_change_coloums(cub.cube,4,3)
                cube_solver.sequence[4]=str(cub.cube[4][1][1])
        
        if k==ord('d'):
            if len(values)>0:
                for i in range(9):
                    cub.cube[5][i//3][i%3]=values[i]
                    cub_pos[i][2]=[]
                cube.rotate(1,cub.cube,3,5)
                inter_change_coloums(cub.cube,5,3)
                cube_solver.sequence[5]=str(cub.cube[5][1][1])
                    
        if k==ord('l'):
            if len(values)>0:
                for i in range(9):
                    cub.cube[0][i//3][i%3]=values[i]
                    cub_pos[i][2]=[]
                cube.rotate(1,cub.cube,3,0)
                inter_change_coloums(cub.cube,0,3)
                cube_solver.sequence[0]=str(cub.cube[0][1][1])
        
        if k==ord('r'):
            if len(values)>0:
                for i in range(9):
                    cub.cube[2][i//3][i%3]=values[i]
                    cub_pos[i][2]=[]
                cube.rotate(1,cub.cube,3,2)
                inter_change_coloums(cub.cube,2,3)
                cube_solver.sequence[2]=str(cub.cube[2][1][1])
        
        if k==ord('b'):
            if len(values)>0:
                for i in range(9):
                    cub.cube[3][i//3][i%3]=values[i]
                    cub_pos[i][2]=[]
                cube.rotate(1,cub.cube,3,3)
                inter_change_coloums(cub.cube,3,3)
                cube_solver.sequence[3]=str(cub.cube[3][1][1])
        
        if k==ord('f'):
            if len(values)>0:
                for i in range(9):
                    cub.cube[1][i//3][i%3]=values[i]
                    cub_pos[i][2]=[]
                cube.rotate(1,cub.cube,3,1)
                inter_change_coloums(cub.cube,1,3)
                cube_solver.sequence[1]=str(cub.cube[1][1][1])
        
        if k==ord('c'):
            print('current cube got deleted')
            cub=cube.Cube(3)  
            last_detected=datetime.now()
            alert='current cube got deleted'
            cube_solver.sequence=['1','2','3','4','5','6']
            text_color=green
        
               
             
    cap.release()
    cv2.destroyAllWindows()


if __name__=='__main__':
    capture_cube()


