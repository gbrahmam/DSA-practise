def difference_sum_even_odd_index(numbers):
    ev_arr = 0
    odd_arr = 0
    for i in range(len(numbers)):
        if i%2 == 0:
            ev_arr+=numbers[i]
        else:
            odd_arr+=numbers[i]
    return int(ev_arr - odd_arr)
        
        
if __name__ == "__main__":
    numbers = [int(i) for i in input().split(' ')]
    print(difference_sum_even_odd_index(numbers))