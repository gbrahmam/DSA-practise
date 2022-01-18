class CarSell:
    def __init__(self, customer_proposals):
        self.list1 = customer_proposals
        self.total_bids = len(customer_proposals)
        
        
    def getPromisingCustomers(self):
        good_customers = []
        count = 0
        for i in range(self.total_bids):
            if self.list1[i]>=(0.9*(10**6)):
                good_customers.append(i)
                count+=1
        if count>0:
            return good_customers
        else:
            return ([-1])
        
        
if __name__ == "__main__":
    num_customers = int(input())
    customer_proposals = []
    for i in range(num_customers):
        customer_proposals.append(int(input()))

    car_sell = CarSell(customer_proposals)
    for j in car_sell.getPromisingCustomers():
        print(j)