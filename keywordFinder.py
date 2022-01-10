import re
import pandas
class findKeyword:
    def __init__(self, fileAddress, regex="\w*\s*\w*[:]\s\d*.\d*"):
        self.regText = regex
        self.keywordDict = {}
        self.__processFile(fileAddress)
    
    def __processFile(self, fileAddress):
        file = open(fileAddress)
        while True:
            line = file.readline()
            if not line:
                break
            matches = re.findall(self.regText, line)
            self.__processMatch(matches)

    def __processMatch(self, matches):
        for match in matches:
            pair = match.split(':')
            if not (len(pair) == 2):
                continue
            if pair[0].strip() in  self.keywordDict:
                self.keywordDict[pair[0].strip()].append(pair[1].strip())
            else :
                self.keywordDict[pair[0].strip()] = [pair[1].strip()]
                
    def saveDataToCSV(self,saveAddress ,keywords=["Train loss","Valid loss","Current_accuracy","Best_accuracy","Current_norm_ED","Best_norm_ED"]):
        df = pandas.DataFrame(self.keywordDict, columns= keywords)       
        df.to_csv(saveAddress,index = False, header=True)    


if __name__ == '__main__':
    a = findKeyword("/home/mmt/myThesis/code V3/saved_models/TPS-ResNet-BiLSTM-AttnCTC-Seed1111/log_train.txt")
    a.saveDataToCSV("./data.csv")