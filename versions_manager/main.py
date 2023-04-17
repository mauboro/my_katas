from string import ascii_letters as letters

class VersionManager:
    def __init__(self, version='0.0.1'):
        values = self.clean_input(version)
        self.major_state, self.minor_state, self.patch_state = values[0], values[1], values[2]
        self.history = [f"{self.major_state}.{self.minor_state}.{self.patch_state}"]
        
    def clean_input(self, version="0.0.1"):
        major, minor, patch = 0, 0, 1
        if len(version.split(".")) >= 3:
            major, minor, patch = version.split(".")[0], version.split(".")[1], version.split(".")[2]
        elif len(version.split(".")) == 2:
            major, minor = version.split(".")[0], version.split(".")[1]
            patch = 0
        elif not version:
            major, minor, patch = 0, 0, 1 
        elif len(version.split(".")) == 1:
            major = version.split(".")[0]
            minor, patch = 0, 0 
        check = str(major) + str(minor) + str(patch)
        if any([True for c in check if c in letters]) :
            raise Exception("Error occured while parsing version!") 

        return (int(major), int(minor), int(patch))
    
    def major(self):
        self.major_state += 1
        self.minor_state = 0
        self.patch_state = 0
        self.history.append(f"{self.major_state}.{self.minor_state}.{self.patch_state}")
        return self
        
    def minor(self):
        self.minor_state += 1
        self.patch_state = 0
        self.history.append(f"{self.major_state}.{self.minor_state}.{self.patch_state}")
        return self
    
    def patch(self):
        self.patch_state += 1
        self.history.append(f"{self.major_state}.{self.minor_state}.{self.patch_state}")
        return self
        
    def rollback(self):
        if len(self.history) == 1:
            raise Exception("Cannot rollback!")
        else:
            self.history.pop()
            values = self.clean_input(self.history[-1])
            self.major_state, self.minor_state, self.patch_state = values[0], values[1], values[2]
        return self
    
    def release(self):
        return self.history[-1]

#READ THIS SHIT PROPERLY SOME OTHER TIME
class VersionManagerRefactored:
    
    def __init__(self, version=None):
        if not version: version='0.0.1'
        self.__memory = []
        try:
            arr = [*map(int,version.split('.')[:3])] + [0,0,0]
        except:
            raise Exception("Error occured while parsing version!")
        del arr[3:]
        self.__version = arr if any(arr) else [0,0,1]
    
    def release(self):
        return '.'.join(map(str, self.__version))

    def rollback(self):
        if not self.__memory: raise Exception("Cannot rollback!")
        self.__version = self.__memory.pop()
        return self
        
    def __update(self, i):
        self.__memory.append([*self.__version])
        self.__version[i] += 1
        self.__version[i+1:] = [0] * (len(self.__version)-1-i)
        return self
    
    def major(self): return self.__update(0)
    def minor(self): return self.__update(1)
    def patch(self): return self.__update(2)

