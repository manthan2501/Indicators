import numpy as np
from Averages import Dynamic_SMA

class RSI_Dynamic(object):
    def __init__(self,X_now,look_back_period,avg_type='SMA',fill_value=None):
        self.X_last=X_now
        self.Down_Average=Dynamic_SMA(0,look_back_period,fill_value=fill_value)
        self.Up_Average=Dynamic_SMA(0,look_back_period,fill_value=fill_value)
        self.RS=1
        self.RSI=50
        self.epsilon=1e-4
        pass
    def update_and_get(self,X_now):
        
        if self.X_last < X_now:
            self.Down_Average.update(0)
            self.Up_Average.update(X_now-self.X_last)
        else:
            self.Down_Average.update(self.X_last-X_now)
            self.Up_Average.update(0)

        
        if self.Up_Average.Average == None or self.Down_Average.Average == None:
            self.RS=None
            self.RSI=None
            return self.RSI
            
        # max precison is epsilon
        self.RS=max(self.Up_Average.Average,self.epsilon)/max(self.Down_Average.Average,self.epsilon)
            
        self.RSI=100/(1+(1/self.RS))
        
        return self.RSI
        
    def get_RSI(self):
        return self.RSI