import json

palettes = [
            ("Rainbow",[[1,50,136,189],[2,153,213,148],[3,230,245,152],[4,254,224,139],[5,252,141,89],[6,213,62,79]],"Spectral / Cynthia Brewer / colorbrewer2.org"),
            ("Rainbow Discrete",[[1,136,204,238],[2,136,204,238],[2,68,170,153],[3,68,170,153],[3,51,34,136],[4,51,34,136],[4,17,119,51],[5,17,119,51],[5,153,153,51],[6,153,153,51],[6,221,204,119],[7,221,204,119],[7,204,102,119],[8,204,102,119],[8,136,34,85],[9,136,34,85],[9,170,68,153],[10,170,68,153]],"Paul Tol / https://personal.sron.nl/~pault/"),
            ("Red",[[1,254,224,210],[2,252,146,114],[3,222,45,38]],"Reds / Cynthia Brewer / colorbrewer2.org"),
            ("Green",[[1,229,245,224],[2,161,217,155],[3,49,163,84]],"Greens / Cynthia Brewer / colorbrewer2.org"),
            ("Blue",[[1,222,235,247],[2,158,202,225],[3,49,130,189]],"Blues / Cynthia Brewer / colorbrewer2.org"),
            ("Purple",[[1,254, 235, 226],[2, 251, 180, 185],[3, 247, 104, 161],[4, 197, 27, 138],[5, 122, 1, 119]], "RdPu / Cynthia Brewer / colorbrewer2.org"),
            ("Fall",[[1,255,255,178],[2,254,204,92],[3,253,141,60],[4,240,59,32],[5,189,0,38]],"YlOrRd / Cynthia Brewer / colorbrewer2.org"),
            ("Earthy",[[1,255, 255, 204],[2, 161, 218, 180], [3,65, 182, 196],[4, 44, 127, 184],[5, 37, 52, 148]], "YlGnBu / Cynthia Brewer / colorbrewer2.org"),
            ("Pink and Green",[[1,77,172,38],[2,184,225,134],[3,247,247,247],[4,241,182,218],[5,208,28,139]],"PiYG / Cynthia Brewer / colorbrewer2.org"),
            ("Red and Blue",[[1,5,113,176],[2,146,197,222],[3,247,247,247],[4,244,165,130],[5,202,0,32]],"RdBu / Cynthia Brewer / colorbrewer2.org"),
            ("Two Colors",[[1,228,26,28],[2,228,26,28],[2,55,126,184],[3,55,126,184]],"Set1 / Cynthia Brewer / colorbrewer2.org"),
            ("Three Colors",[[1,228,26,28],[2,228,26,28],[2,55,126,184],[3,55,126,184],[3,77,175,74],[4,77,175,74]],"Set1 / Cynthia Brewer / colorbrewer2.org"),
            ("Four Colors",[[1,228,26,28],[2,228,26,28],[2,55,126,184],[3,55,126,184],[3,77,175,74],[4,77,175,74],[4,152,78,163],[5,152,78,163]],"Set1 / Cynthia Brewer / colorbrewer2.org"),
            ("Five Colors",[[1,228,26,28],[2,228,26,28],[2,55,126,184],[3,55,126,184],[3,77,175,74],[4,77,175,74],[4,152,78,163],[5,152,78,163],[5,255,127,0],[6,255,127,0]],"Set1 / Cynthia Brewer / colorbrewer2.org"),
            ("Six Colors",[[1,228,26,28],[2,228,26,28],[2,55,126,184],[3,55,126,184],[3,77,175,74],[4,77,175,74],[4,152,78,163],[5,152,78,163],[5,255,127,0],[6,255,127,0],[6,255,255,51],[7,255,255,51]],"Set1 / Cynthia Brewer / colorbrewer2.org"),
            ("Seven Colors",[[1,228,26,28],[2,228,26,28],[2,55,126,184],[3,55,126,184],[3,77,175,74],[4,77,175,74],[4,152,78,163],[5,152,78,163],[5,255,127,0],[6,255,127,0],[6,255,255,51],[7,255,255,51],[7,166,86,40],[8,166,86,40]],"Set1 / Cynthia Brewer / colorbrewer2.org"),
            ("Eight Colors",[[1,228,26,28],[2,228,26,28],[2,55,126,184],[3,55,126,184],[3,77,175,74],[4,77,175,74],[4,152,78,163],[5,152,78,163],[5,255,127,0],[6,255,127,0],[6,255,255,51],[7,255,255,51],[7,166,86,40],[8,166,86,40],[8,247,129,191],[9,247,129,191]],"Set1 / Cynthia Brewer / colorbrewer2.org"),
            ("Nine Colors",[[1,228,26,28],[2,228,26,28],[2,55,126,184],[3,55,126,184],[3,77,175,74],[4,77,175,74],[4,152,78,163],[5,152,78,163],[5,255,127,0],[6,255,127,0],[6,255,255,51],[7,255,255,51],[7,166,86,40],[8,166,86,40],[8,247,129,191],[9,247,129,191],[9,153,153,153],[10,153,153,153]],"Set1 / Cynthia Brewer / colorbrewer2.org"),
            ("Two Pairs",[[1,166,206,227],[2,166,206,227],[2,31,120,180],[3,31,120,180],[3,178,223,138],[4,178,223,138],[4,51,160,44],[5,51,160,44]],"Paired / Cynthia Brewer / colorbrewer2.org"),
            ("Three Pairs",[[1,166,206,227],[2,166,206,227],[2,31,120,180],[3,31,120,180],[3,178,223,138],[4,178,223,138],[4,51,160,44],[5,51,160,44],[5,251,154,153],[6,251,154,153],[6,227,26,28],[7,227,26,28]],"Paired / Cynthia Brewer / colorbrewer2.org"),
            ("Four Pairs",[[1,166,206,227],[2,166,206,227],[2,31,120,180],[3,31,120,180],[3,178,223,138],[4,178,223,138],[4,51,160,44],[5,51,160,44],[5,251,154,153],[6,251,154,153],[6,227,26,28],[7,227,26,28],[7,253,191,111],[8,253,191,111],[8,255,127,0],[9,255,127,0]],"Paired / Cynthia Brewer / colorbrewer2.org"),
            ("Five Pairs",[[1,166,206,227],[2,166,206,227],[2,31,120,180],[3,31,120,180],[3,178,223,138],[4,178,223,138],[4,51,160,44],[5,51,160,44],[5,251,154,153],[6,251,154,153],[6,227,26,28],[7,227,26,28],[7,253,191,111],[8,253,191,111],[8,255,127,0],[9,255,127,0],[9,202,178,214],[10,202,178,214],[10,106,61,154],[11,106,61,154]],"Paired / Cynthia Brewer / colorbrewer2.org"),
            ("Two Scales",[[1,166,206,227],[3,31,120,180],[3,178,223,138],[5,51,160,44]],"Paired / Cynthia Brewer / colorbrewer2.org"),
            ("Three Scales",[[1,166,206,227],[3,31,120,180],[3,178,223,138],[5,51,160,44],[5,251,154,153],[7,227,26,28]],"Paired / Cynthia Brewer / colorbrewer2.org"),
            ("Four Scales",[[1,166,206,227],[3,31,120,180],[3,178,223,138],[5,51,160,44],[5,251,154,153],[7,227,26,28],[7,253,191,111],[9,255,127,0]],"Paired / Cynthia Brewer / colorbrewer2.org"),
            ("Five Scales",[[1,166,206,227],[3,31,120,180],[3,178,223,138],[5,51,160,44],[5,251,154,153],[7,227,26,28],[7,253,191,111],[9,255,127,0],[9,202,178,214],[11,106,61,154]],"Paired / Cynthia Brewer / colorbrewer2.org"),
            ("Grayscale",[[1,255,255,255],[2,0,0,0]],""),
            ("Old Rainbow",[[1,0,0,128],[2,0,0,255],[3,0,255,255],[4,0,255,0],[5,255,255,0],[6,255,0,0],[7,128,0,0]], ""),
     ]
partitions = 6;
data = [] #Declare array to hold palette names and resulting hex color values

#Convert a RGB list (of the form [256, 256, 256]) to hex value
def rgbToHex(rgbList):    
      return "#"+"".join(hex(x)[2:] for x in rgbList)

#Return hex color value based on a point between two color steps
def gradientCalc(rgb1, rgb2, pct): 
    print(rgb1, rgb2)
    print("pct: ",pct)
    RGB = [0,0,0]
    RGB[0] = int(rgb1[0]+(rgb2[0]-rgb1[0])*pct) 
    RGB[1] = int(rgb1[1]+(rgb2[1]-rgb1[1])*pct)
    RGB[2] = int(rgb1[2]+(rgb2[2]-rgb1[2])*pct)
    return RGB

#Given a palette, return boolean value if there are repeating color steps
def uniqueSeq(palRange):
    if(len(palRange)==palRange[-1][0]):
        return True
    return False

#Given a palette (indices and color values) and target position, return single RGB color list
def stepNeighbors(palRange, target):
    index = [x[0] for x in palRange]
    nextStep = [i for i,v in enumerate(index) if v>=target][0] #get next step index in palRange after target

    #decision tree to check for gradient, coinciding point, and two coinciding points
    print(index[nextStep],target)
    if(index[nextStep]==target):
        
        if index[nextStep] != index[-1] and index[nextStep+1] ==target:
            print("current1A: ",index[nextStep+1],target)
            return palRange[nextStep+1][1:]
        print("current1: ",index[nextStep],target)
        return palRange[nextStep][1:]
    else:
        print("current2: ",index[nextStep],target)

        priorStep = [i for i,v in enumerate(index) if v<target][-1]
        print(priorStep,index[priorStep])
        pct = round((target-index[priorStep])/(index[nextStep]-index[priorStep]),3)
        return gradientCalc(palRange[priorStep][1:],palRange[nextStep][1:],pct)
        #this returns the gradient calc, not rgb values


#Returns an array of hex colors values given a palette and number of selections from the palette
def colorFetch(palette,n): 
    #step = palette[1][-1][0]/n #Get largest step value from palette and divide with desired selections
    step = (palette[1][-1][0]-1)/(n-1)
    result = []
    uniqueTest = uniqueSeq(palette[1])
    #if not uniqueTest: result.append(palette[1][0][1:])
    for x in range(0,n):
        result.append(rgbToHex(stepNeighbors(palette[1], step*x+1)))
        print(result)
    return result

#colorFetch(palettes[0],6) works (CASE: ALL STEPS ARE MATCHING WITH INDEX)
for pal in palettes:
    result =[]
    result.append(pal[0])
    result.append(colorFetch(pal,partitions))
    data.append(result)

out = open("pal_out.txt","w")
out.write(json.dumps(data))
out.close()
#format data down here
case = ["#fee0d2", "#fec2ad", "#fda387", "#f77f64", "#eb5645", "#df2e27"]



