#dependency does nothing by itself
import csv
class NetworkAnalysis:
    
    def __init__(self,fname):
        
     
        with open(fname,'r') as file:
            
            reader=csv.reader(file)
            header=next(reader)
            
            self._data=list(map(tuple,reader))
    
    def __Partition(self,tlist, lowIndex, highIndex,tidex):
        #Pick middle element as pivot
        midpoint = int(lowIndex + (highIndex - lowIndex) / 2)
        pivot = tlist[midpoint][1]

        done = False
        while (not done):
            
            while (tlist[lowIndex][1] < pivot):
                lowIndex += 1
          
            while (pivot < tlist[highIndex][1]):
                highIndex -= 1
          
            if (lowIndex >= highIndex):
                done = True
          
            else:
             # Swap tlist[lowIndex] and tlist[highIndex]
                temp = tlist[lowIndex]
                tlist[lowIndex]= tlist[highIndex]
                tlist[highIndex] = temp

                #Update lowIndex and highIndex
                lowIndex += 1
                highIndex -= 1
          
       

        return highIndex
    

    def __Quicksort(self,tlist, lowIndex, highIndex,tindex):
        #Base case: If the partition size is 1 or zero 
        #elements, then the partition is already sorted
        if (lowIndex >= highIndex):
            return
       

        #Partition the data within the dic. Value lowEndIndex returned from partitioning is the index of the low partition's last element.
        lowEndIndex = self.__Partition(tlist, lowIndex, highIndex,tindex)

        #Recursively sort low partition (lowIndex to lowEndIndex) 
        #and high partition (lowEndIndex + 1 to highIndex)
        self.__Quicksort(tlist, lowIndex, lowEndIndex,tindex)
        self.__Quicksort(tlist, lowEndIndex + 1, highIndex,tindex)
        
  
            
    def ips_by_connections(self):
        
        ips={}
        
        for i in self._data:
            ip=i[2]
            if(ip in ips):
                ips[ip]=ips[ip]+1
            else:
                ips[ip]=1
                
        d_items =list(ips.items())#list of tuples
        self.__Quicksort(d_items, 0, (len(d_items)-1),1)
        for i in range(len(d_items)):
            print(i,d_items[i])

 

    def ips_by_bytes(self):
        ips={}
        
        for i in self._data:
            ip=i[2]
            if(ip in ips):
                ips[ip]=ips[ip]+int(i[5])
            else:
                ips[ip]=int(i[5])
        
        d_items =list(ips.items())#list of tuples
        self.__Quicksort(d_items, 0, (len(d_items)-1),1)
        for i in range(len(d_items)):
            print(i,d_items[i])
    
    def protocols_by_connections(self):
        protocols={}
        
        for p in self._data:
            protocol=p[4]
            if(protocol in protocols):
                protocols[protocol]=protocols[protocol]+1
            else:
                protocols[protocol]=1
                
        d_items =list(protocols.items())#list of tuples
        self.__Quicksort(d_items, 0, (len(d_items)-1),1)
        for i in range(len(d_items)):
            print(i,d_items[i])
            
    def protocols_by_bytes(self):
        protocols={}
        
        for p in self._data:
            protocol=p[4]
            if(protocol in protocols):
                protocols[protocol]=protocols[protocol]+int(p[5])
            else:
                protocols[protocol]=int(p[5])
                
        d_items =list(protocols.items())#list of tuples
        self.__Quicksort(d_items, 0, (len(d_items)-1),1)
        for i in range(len(d_items)):
            print(i,d_items[i])
            
    def connections_by_connections(self):
        connections={}
        
        for c in self._data:
            connection=c[2],c[3]
            if(connection in connections):
                connections[connection]=connections[connection]+1
            else:
                connections[connection]=1
                
        d_items =list(connections.items())#list of tuples
        self.__Quicksort(d_items, 0, (len(d_items)-1),1)
        for i in range(len(d_items)):
            print(i,d_items[i])
        
    def connections_by_bytes(self):
        connections={}
        
        for c in self._data:
            connection=c[2],c[3]
            if(connection in connections):
                connections[connection]=connections[connection]+int(c[5])
            else:
                connections[connection]=int(c[5])
                
        d_items =list(connections.items())#list of tuples
        self.__Quicksort(d_items, 0, (len(d_items)-1),1)
        for i in range(len(d_items)):
            print(i,d_items[i])
        
