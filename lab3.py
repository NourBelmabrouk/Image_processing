import random
from lab1 import *
import numpy as np

def add_noise(filename):

    data=read_image_pgm(filename)
    result=data["matrix"].copy()
    for i in range(data["line"]):
        for j in range(data["column"]):
            random_number = random.randint(0, 20)
            if random_number==0:
                result[i][j]=0
            elif random_number==20:
                result[i][j]=255
    
    return result

def mean_filter(filename,n):
    
    data=read_image_pgm(filename)
    result=data["matrix"].copy()
    for line in range(data["line"]):
        for column in range(data["column"]):
            sum=0
            for i in range(line- n//2, line+ n//2):
                for j in range(column- n//2, column+ n//2):
                    val=0
                    if i<0:
                        val=data["matrix"][-i][j]
                    if i> data["line"]-1:
                        val=data["matrix"][2*(data["line"]-1)-i ][j]
                    if j<0:
                        val=data["matrix"][i][-j]
                    if j> data["column"]-1:
                        val=data["matrix"][i][2*(data["column"]-1)-j]
                    else :
                        val=data["matrix"][i][j]
                    sum+=val
            result[line][column]=sum/(n*n)
    
    return result


    

def median_filter(filename,n):

    data=read_image_pgm(filename)
    result=data["matrix"].copy()
    for line in range(data["line"]):
        for column in range(data["column"]):
            vals=[]
            for i in range(line- n//2, line+ n//2):
                for j in range(column- n//2, column+ n//2):
                    val=0
                    if i<0:
                        val=data["matrix"][-i][j]
                    if i> data["line"]-1:
                        val=data["matrix"][2*(data["line"]-1)-i ][j]
                    if j<0:
                        val=data["matrix"][i][-j]
                    if j> data["column"]-1:
                        val=data["matrix"][i][2*(data["column"]-1)-j]
                    else :
                        val=data["matrix"][i][j]
                    vals.append(val)
            result[line][column]=np.median(vals)

    return result
