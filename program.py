#main
from network_analysis import NetworkAnalysis 

def main():
    print('NETWORK ANALYZER')
    
    fname=input("Enter in the PCAP filename: ")
    networkAnalysis=NetworkAnalysis(fname)
  
    while(True):
        
        option=input("Choose analysis option:\n(0) IPs by Connection\n"+
                    "(1) IPs by Bytes\n(2) Protocols by Connections\n"+
                    "(3) Protocols by Bytes\n(4) Connections by Connections\n"+
                    "(5) Connections by Bytes\n(6) Quit\n --> ")
        if(option=="0"):
            networkAnalysis.ips_by_connections()
        elif(option=="1"):
            networkAnalysis.ips_by_bytes()
        elif(option=="2"):
            networkAnalysis.protocols_by_connections()
        elif(option=="3"):
            networkAnalysis.protocols_by_bytes()
        elif(option=="4"):
            networkAnalysis.connections_by_connections()
        elif(option=="5"):
            networkAnalysis.connections_by_bytes()
        elif(option=="6"):
            break
        else:
            print("Invalid option entered")
            
    
       
main()

