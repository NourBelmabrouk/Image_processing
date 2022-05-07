from cv2 import line
from lab1 import *

def histogram_equalization(filename):
    data=read_image_pgm(filename)
    hist=histogram(data["matrix"],data["column"],data["line"],data["lvl_gray"])
    cum_hist=cumulative_histogram(hist)
    eq=[0 for i in range(len(cum_hist))]
    taille=data["line"]*data["column"]

    #initialize list for frequency probabilities: P
    pdf=[]
    for i in hist:
        pdf.append(i/taille)

    #initialize list for cumulative probability: Pc
    cdf=[]
    total=0
    for i in pdf:
        total=total+i
        cdf.append(total)

    #intialize list for mapping cdf: n1
    tr=[]
    for i in cdf:
        t=int(i*(data["lvl_gray"]-1))
        tr.append(t)

    #initialize list containing new frequencies for equalized hist
    hs=[]
    for i in range(256):
        count=0
        tot=0
        for j in tr:
            if (j==i):
                tot=tot+hist[count]
            count=count+1
        hs.append(tot)

    return hs


def linear_transformation(filename,point1,point2):
    data=read_image_pgm(filename)
    new_matrix=data["matrix"].copy()
    for i in range(data["line"]):
        for j in range(data["column"]):
            if data["matrix"][i][j] <= point1[0] :
                new_matrix[i][j]= (point1[1]/point1[0])*data["matrix"][i][j]
            elif (point1[0]<data["matrix"][i][j] and data["matrix"][i][j]<=point2[0]):
                new_matrix[i][j]=((point2[1]-point1[1])/(point2[0]-point1[0]))*(data["matrix"][i][j]-point1[0])+point1[1]
            else:
                new_matrix[i][j]=((data["lvl_gray"]-point2[1])/(data["lvl_gray"]-point2[0]))*(data["matrix"][i][j]-point2[0])+point2[1]
    
    return new_matrix
