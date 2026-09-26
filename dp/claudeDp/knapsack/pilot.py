weights = [6, 3, 4]   # gold, diamond, painting
values  = [60, 50, 40]
capacity = 10

def knapsack(index, remaining_capacity):
    # base case: no more items to decide on
    if index>= len(weights):return 0
    # what should this return?
    
    # recursive case: at `index`, you have two choices —
    # 1. skip this item
    # 2. take this item (only legal if it fits in remaining_capacity)
    # return the BETTER of the two
    

print(knapsack(0, capacity))  # should print 110