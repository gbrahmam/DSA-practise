class Flight:
    def __init__(self, upTime, downTime):
        self.upTime = upTime
        self.downTime = downTime

    def calculateFlight(self):
        # Your Code goes here
        upTime = [int(x) for x in t1.split(':')]
        downTime = [int(x) for x in t2.split(':')]
        h_up = upTime[0]
        m_up = upTime[1]
        h_down = downTime[0]
        m_down = downTime[1]
        down_in_mm = downTime[0]*60 + downTime[1]
        up_in_mm = upTime[0]*60 + upTime[1]
        total_fly = int(down_in_mm - up_in_mm)
        return total_fly
        
### DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__ == '__main__':
    
    t1 = input()
    t2 = input()

    f1 = Flight(t1, t2)
    print(f1.calculateFlight())