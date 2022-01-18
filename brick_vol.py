def calculate_total_price_of_bricks(dimensions, brick_count):
    if dimensions[0]==-1:
        dimensions[0]=60
    if dimensions[1]== -1:
        dimensions[1]=40
    vol = volume(100,dimensions[0],dimensions[1])
    tot_vol = vol * brick_count
    tol_price = calculate_price(tot_vol)
    return tol_price
    

### Do not change anything below this line
def volume(length=100,width=60,height=40):
	return length*width*height

def calculate_price(volume, price=0.00005):
	return round(volume*price)

if __name__ == "__main__":
    brick_count = int(input())
    dimensions = [int(i) for i in input().split(' ')]
    total_price = calculate_total_price_of_bricks(dimensions, brick_count)
    print(total_price)