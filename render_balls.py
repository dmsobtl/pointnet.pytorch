import numpy as np

class point_info:
    x=0
    y=0
    z=0
    r=0
    g=0
    b=0
    def __init__(self,x,y,z,R):
        self.x=x
        self.y=y
        self.z=z
        self.r=z/R
        self.g=z/R
        self.b=z/R


def render_ball(h,w,show,n,xyzs,c0,c1,c2,r):
    r=np.maximum(r,1)
    depth=[-210000000 for x in range(h*w)]
    pattern=[]
    for dx in range(-r,r):
        for dy in range(-r,r):
            if (dx*dx+dy*dy<r*r):
                dz=np.sqrt(r*r-dx*dx-dy*dy)
                point=point_info(dx,dy,dz,r)
                pattern.append(point)
    zmin=0
    zmax=0
    for i in range(n):
        if i==0:
            zmin=xyzs[i,2]-r
            zmax=xyzs[i,2]+r
        else:
            zmin = min(zmin, (xyzs[i, 2] - r))
            zmax = max(zmax, (xyzs[i, 2] + r))
    for i in range(n):
        x = xyzs[i, 0]
        y = xyzs[i, 1]
        z = xyzs[i, 2]
        for j in range(len(pattern)):
            x2=x+pattern[j].x
            y2=y+pattern[j].y
            z2=z+pattern[j].z
            if (not(x2 < 0 or x2 >= h or y2 < 0 or y2 >= w) and depth[x2 * w+y2] < z2):
                depth[x2 * w+y2]=z2
                intensity=np.minimum(1.0, (z2-zmin) / (zmax-zmin) * 0.7+0.3)
                show[x2, y2, 0]=pattern[j].b * c2[i] * intensity
                show[x2, y2, 1]=pattern[j].g * c0[i] * intensity
                show[x2, y2, 2]=pattern[j].r * c1[i] * intensity




