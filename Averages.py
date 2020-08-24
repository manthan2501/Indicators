import numpy as np

class Dynamic_SMA(object):
    def __init__(self,X_now,look_back_period=14,fill_value=None):
        self.fill_value=fill_value
        self.start_values=None
        self.look_back_period=look_back_period
        self.X_array=np.full(look_back_period,fill_value)
        self._X_index=0
        self.X_array[self._X_index]=X_now
        if None in self.X_array:
            self.Average=None
        else:
            self.Average=self.X_array.mean()
        self._X_index=1%look_back_period

    def add(self,X):
        self.X_array[self._X_index]=X
        self._X_index=(self._X_index+1)%self.look_back_period
        
    def update(self,X):
        self.X_array[self._X_index]=X
        self._X_index=(self._X_index+1)%self.look_back_period
        if None in self.X_array:
            return
        self.Average=self.X_array.mean()
    
    def update_and_get(self,X):
        self.X_array[self._X_index]=X
        self._X_index=(self._X_index+1)%self.look_back_period
        if None in self.X_array:
            return None
        self.Average=self.X_array.mean()
        return self.Average