# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 21:04:06 2016

@author: Jeffrey
"""
def printList(circleList):
    #circleList
    if (len(circleList)<1):
        return (0,0,0)
    else:
        print "______kmean is runing________"
        iterations = 200
        ##TODO:  genreate a ranom number
        center1 = (100 ,100, 30)
        center2 =  (300, 300, 30)
        count1 = 0 
        count2 = 0
        circleNum=0
        #print "center1= " + str(center1[0])
        #print "center1= " + str(center1[1])
        for i in range(0, iterations):
            #print "count= " + str(i)
            if(count1+count2 == (0, 0)):  #first pass
                circleNum=0
                tempCircle=circleList[0]
                center1 = (100 ,100, tempCircle[3])
                center2= (300, 300, tempCircle[3])
            else:
                circleNum= circleNum+1
            for i in range(0, len(circleList)):
                tempCircle=circleList[i]
                #print "circleList= " +str(circleList)
                #print "center1= " + str(center1[0])
                #print "center1= " + str(center1[1])
                tempTuple = (0 ,0, 0)
                #print "tempTuple= " + str(tempTuple)
                tempTuple = (tempCircle[0], tempCircle[1])
                #print "tempTuple= " + str(tempTuple)
                if(nearestPoint(tempTuple, center1, center2)== center1):
                    if count1 ==0:
                        center1 =  ((center1[0]*count1 + tempCircle[0])/(count1+1), (center1[1]*count1 + tempCircle[1])/(count1+1), (center1[2]*count1 + tempCircle[2])/(count1+1))
                    else:
                        center1 = (tempCircle[0], tempCircle[1], tempCircle[2])
                    #center1 =  (C1Center.Lon*count1 + GPSNode.GetGPSValLon())/(count1+1)
                    count1 = count1+1
                else:
                    if count2 ==0:
                        center2 =  ((center2[0]*count2 + tempCircle[0])/(count2+1), (center2[1]*count2 + tempCircle[1])/(count2+1), (center2[2]*count2 + tempCircle[2])/(count2+1))
                    else:
                        center2 = (tempCircle[0], tempCircle[1], tempCircle[2])
                    #C2Center.Lat =  (C2Center.Lat*count2 + GPSNode.GetGPSValLat())/(count2+1)
                    #C2Center.Lon =  (C2Center.Lon*count2 + GPSNode.GetGPSValLon())/(count2+1)
                    count2 =count2+1
                
            print "why do I need this line"
        #print "center1: " + center1 + " & Center2: " + center2 
        kCenter = (center1, center2)
        print "kcenter: " + str(kCenter)
        return kCenter #(center1, center2)
     
def nearestPoint(point, point1, point2):
    #print "center= " + str(point[0]) + " , " +str(point[1])
    #print "center1= " + str(point1[0]) + " , " +str(point1[1])
    #print "center2= " + str(point2[0]) + " , " +str(point2[1])
    #print "nearestPoint running"
    LW=(abs(point[0]-point1[0]), abs(point[1]-point1[1]))
    #print "LW found"
    distToPoint1 = ((LW[0]**2)+(LW[1]**2))**(0.5)
    #print "distToPoint1 found"    
    LW=(abs(point[0]-point2[0]), abs(point[1]-point2[1]))
    distToPoint2 = ((LW[0]**2)+(LW[1]**2))**(0.5)
    #print "distToPoint1 found" +str(distToPoint2)
    if(distToPoint1 > distToPoint2):
        return point2
    else:
        return point1
    
    
    
    
    
    #for (circles) in circleList:
        #for (x, y, r) in circles:
            #print x, y, r
            
    
    
    """
    
    for i=0, i< iteration, i++:
		do  # do this for every recoded GPS point  guess
			if((C1Count+C2Count) ==0 ) # first pass
				GPSNode = GPSList.startNode;
			else
				GPSNode = GPSNode.nextNode()				
			if(nearestPoint(GPSNode, C1Center, C2Center) == C1Center)#distanceBetween(C1Center, GPSNode) < distanceBetween(C2Center, GPSNode)
				#assige to cluster 1
				C1Center.Lat =  (C1Center.Lat*C1Count + GPSNode.GetGPSValLat())/(C1Count+1)
				C1Center.Lon =  (C1Center.Lon*C1Count + GPSNode.GetGPSValLon())/(C1Count+1)
				C1Count++
			}
			else
			{
				C2Center.Lat =  (C2Center.Lat*C2Count + GPSNode.GetGPSValLat())/(C2Count+1)
				C2Center.Lon =  (C2Center.Lon*C2Count + GPSNode.GetGPSValLon())/(C2Count+1)
				C2Count++
			}

		}while(GPSNode != GPSList.endNode) #each node
		
		if(distanceBetween(C1Center, oldC1Center) <= tolerance && distanceBetween(C2Center, oldC2Center)  <= tolerance) # if the ceter point is within tolerance 
			break    #exit for loop
		else
			oldC1Center = C1Center
			oldC2Center = C2Center
    
    
    """
    """
    
FindNodeCenters(LinkedList GPSList, int iteration = 10, float tolerance = 0.01) //TODO: make tolerence = 1 ftell
{
	std::ifstream fin1("/root/temp1.txt", std::ios::in);
	td::ifstream fin2("/root/temp2.txt", std::ios::in);
	std::string mode;
    std::getline(fin1, mode1);
	std::getline(fin2, mode2);
    fout << "Mode: " << mode << std::endl;

	if()
	{
		std::ifstream fin("/root/waypoints.txt", std::ios::in);
	}
	_waypoints
	//TODO: set up defalt starting postions of center postions
	new GPS_cords C1Center;
	new GPS_cords C2Center;  //center of each cluster
	new GPS_cords oldC1Center;
	new GPS_cords oldC2Center;
	int iteration = 10;
	int C1Count = 0, C2Count =0; // number of points assigent to each cluster
	
	for(i=0, i< iteration, i++)
	{
		do  // do this for every recoded GPS point  guess
		{
			if((C1Count+C2Count) ==0 ) // first pass
			{
				GPSNode = GPSList.startNode;
			}
			else
			{
				GPSNode = GPSNode.nextNode();				
			}
			if(nearestPoint(GPSNode, C1Center, C2Center) == C1Center)//distanceBetween(C1Center, GPSNode) < distanceBetween(C2Center, GPSNode)
			{
				//assige to cluster 1
				C1Center.Lat =  (C1Center.Lat*C1Count + GPSNode.GetGPSValLat())/(C1Count+1);
				C1Center.Lon =  (C1Center.Lon*C1Count + GPSNode.GetGPSValLon())/(C1Count+1);
				C1Count++;
			}
			else
			{
				C2Center.Lat =  (C2Center.Lat*C2Count + GPSNode.GetGPSValLat())/(C2Count+1);
				C2Center.Lon =  (C2Center.Lon*C2Count + GPSNode.GetGPSValLon())/(C2Count+1);
				C2Count++;
			}

		}while(GPSNode != GPSList.endNode); //each node
		
		if(distanceBetween(C1Center, oldC1Center) <= tolerance && distanceBetween(C2Center, oldC2Center)  <= tolerance) // if the ceter point is within tolerance 
		{
			break;//exit for loop
		}
		else
		{
			oldC1Center = C1Center;
			oldC2Center = C2Center;
		}
	}
}
start point()
{
	
	//abs(a-b);
}

//template <typename T>
//findHypotenuse(T x, T y)
//{
//	return sqrt(x*x+y*y);
//} """