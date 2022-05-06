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
