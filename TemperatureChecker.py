
import statistics, random
class TempTracker():
    def __init__(self):
        self.temperatures = list()
    
    def insert(self, new_temp):
        self.temperatures.append(new_temp)
    
    def print_temperatures(self):
        print(self.temperatures)
    
    def __find_min(self):
        return min(self.temperatures) 
    
    def get_min(self):
        print(self.__find_min())
    
    def __find_max(self):
        return max(self.temperatures)
    
    def get_max(self):
        print(self.__find_max())
    
    def get_mean(self):
        sum = 0
        for item in self.temperatures:
            sum += item
        mean = sum/len(self.temperatures)
        print(float(mean))
        
    def __find_mode(self):
        occurences = dict((i,0) for i in self.temperatures)
        for item in self.temperatures:
            occurences[item] +=1
        modes = []
        #get first key in occurences dictionary
        keys_view = occurences.keys()
        key_iterator = iter(keys_view)
        mode = next(key_iterator)
        values_view = occurences.values()
        value_iterator = iter(values_view)
        largest = next(value_iterator)
        #get first value in occurences dictionary
        for key, value in occurences.items():
            largest = max(largest, value)
        for key, value in occurences.items(): 
            if value == largest: 
                return key, largest 
    def get_mode(self):
        print(self.__find_mode())
a = TempTracker()
for i in range(0, 20):
   a.insert(random.randint(1,10)) 
#a.print_temperatures()
a.get_mode()
a.get_min()
a.get_max()
a.get_mean()
