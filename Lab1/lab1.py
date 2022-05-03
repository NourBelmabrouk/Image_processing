import numpy as np

def read_image_pgm(filename):
    file=open(filename,"r")
    lines=file.readlines()
    for line in lines:
        if line[0]=='#':
            lines.remove(line)

    data=[]
    for line in lines:
        for val in line.split():
            data.append(val)

    image_format=data[0]
    if image_format!= "P2" and image_format!="P5":
        print("format not supported")
        file.close()
        exit()
    del(data[0])

    column=int(data[0])
    del(data[0])
    line=int(data[0])
    del(data[0])

    lvl_gray=int(data[0])
    del(data[0])

    for i in range(len(data)):
        data[i]=int(data[i])
    
    matrix=np.reshape(np.array(data),(line,column))
    file.close()
    
    return {
        "line":line,
        "column":column,
        "lvl_gray": lvl_gray,
        "matrix":matrix
    }


def write_image_pgm(filepath,matrix,line,column,lvl_gray):
    file=open(filepath,"w")
    file.write("P2\n")
    file.write("# image created in an image processing lab\n")
    file.write(str(column)+" "+str(line)+"\n")
    file.write(str(lvl_gray)+"\n")
    for i in range(line):
        for j in range(column):
            file.write(str(matrix[i][j])+" ")
        file.write("\n")
    file.close()
    
def calculate_mean_deviation(matrix):
    mean=np.mean(matrix)
    deviation=np.std(matrix)
    return mean,deviation

def histogram(matrix,column,line,lvl_gray):
    h=[0 for i in range(lvl_gray+1)]
    for i in range(line):
        for j in range(column):
            h[matrix[i][j]]+=1
    return h

def cumulative_histogram(hist):
    c=[hist[i] for i in range(len(hist))]
    for i in range(1,len(c)):
        c[i]+=c[i-1]
    return c
