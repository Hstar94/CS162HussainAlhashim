from stopwatch import stopwatch
import time
import os
class VideoGameSearchEngine:
    def __init__(self) -> None:
        self._data=[]
        with open('video_game_data.csv','r') as resultsFile:
            resultsFile.readline()
            for line in resultsFile:
                term=line.split(",")
                self._data.append(term)
            resultsFile.close
    
    def linearSearch(self,search_terms,column_index):
        results=[]
        timer=stopwatch()
        for game  in self._data:
            for term in search_terms:
                if term==game[column_index]:
                    results.append(game)
                    break
        return results,timer.elapsed()
    
    @staticmethod
    def print_results(results,searchTime):
        seperator = '         '
        for res in results:
            for row in zip(res):
                #print(seperator.join(row))
                print(seperator.join(res))
                #print(row)
        print("Total search time: {0}. Total results: {1}".format(searchTime,len(results)))
            
def main():
    print("VIDEO GAME SEARCH ENGINE")
    print("Choose option: ")
    print("(0) Id Number")
    print("(1) Name")                     
    print("(2) Platform")
    print("(3) Year",)
    print("(4) Genre")
    print("(5) publisher")
    print("(6) Developer")
    print("(7) Rating")                     #Doesn't work because of empty spaces on some of them
    colIndex=int(input("--> "))
    terms=input("Enter search terms(s): ")
    print("Search Results\n")
    print("ID Number       Name              Platform          Year         Genre         Publisher         Developer         Rating\n\n")
    vgse=VideoGameSearchEngine()
    results,size=vgse.linearSearch(terms.split("  "),colIndex)
    vgse.print_results(results,size)
    option=input("search again Y(es) or N(o) :")
    if option=="Y" or option=="y":
        main()

if __name__ == "__main__":
    main()