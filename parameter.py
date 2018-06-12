import time
start_time = time.time()


import opusFC
import os
import pandas as pd
import numpy
import csv

SNM = []
INS = []
DAT = []
TIM = []
EXP = []
DUR = []
CNM = []
RES = []
ZFF = []
NPT = []
LWN = []
LXV = []
FXV = []
minY = []
maxY = []
values = []


def file_list():


    # Change current working directory to where OPUS files are stored in your computer
    os.chdir('file path')

    # Check currect working directory
    cwd = os.getcwd()

    file_list = os.listdir(os.curdir)
    #print file_list

    return file_list
#a=file_list()
#print(a)
counter=[]
f=[]
def parameters():

    fl=file_list()
    count = 0

    for f in fl:
        try:
            dbs = opusFC.isOpusFile(f)
  #control structure for the loop
            if dbs==True:

                conte=opusFC.listContents(f)
                data=opusFC.getOpusData(f,conte[0])
                count += 1
                print(count)
            #print conte, f
                data=opusFC.getOpusData(f, conte[0])
                print data.parameters, f

                SNM.append(data.parameters['SNM'])
                INS.append(data.parameters['INS'])
                DAT.append(data.parameters['DAT'])
                TIM.append(data.parameters['TIM'])
                DUR.append(data.parameters['DUR'])
                CNM.append(data.parameters['CNM'])
                RES.append(data.parameters['RES'])
                ZFF.append(data.parameters['ZFF'])
                NPT.append(data.parameters['NPT'])
                LWN.append(data.parameters['LWN'])
                FXV.append(data.parameters['FXV'])
                LXV.append(data.parameters['LXV'])
                minY.append(data.minY)
                maxY.append(data.maxY)

                continue

            else:
                print('identified as non-Opus', f)


        except ValueError:
            print('Cant process a non-Opus file', f)

            continue




b=parameters()
print(b)


# metadata
varnames = 'SNM', 'Instrument', 'Scan_date', "Time", "Duration", "Operator", "Resolution", "Zero_filling_Factor", "Number_points", "Laser_Wavenumber", "Wavenumber_one", "Wavenumber_last", "Min_absorbance", "Max_Absorbance"

metadata = numpy.vstack((SNM, INS, DAT, TIM, DUR, CNM, RES, ZFF, NPT, LWN, FXV, LXV, minY, maxY)).T

metadata = pd.DataFrame(metadata, columns=varnames)

print(metadata)



# write metadata to a csv file
metadata.to_csv('OPUS files metadata.csv')

print "time elapsed: {:.2f}s".format(time.time() - start_time)


