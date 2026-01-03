import math
#First import math to round te code
def paint_calc(height, weidth, cover):
    area = height * weidth
    num_of_cans = math.ceil(area / cover) 
    print(f"you will need {num_of_cans} cans to paint the wall")
    # here we defined out function and calculations that will happen in background   
test_h = int(input("what is the height: "))
test_w = int(input("What is the Width: ")) 
coverage = 5
#Taked out inputs
paint_calc(height = test_h, weidth = test_w, cover = coverage)
#now calling our cunctions to give them commends with inputs

# practicing
# import math
# def paint_calculator(height, weidth, cover):
#     area = height * weidth
#     num_of_cans = math.ceil(area / cover)
#     print(f"you need {num_of_cans} can paint")
# ht = int(input("enter height"))
# wt = int(input("enter weidth"))
# coverage = 5
# paint_calculator(height = ht, weidth = wt, cover = coverage)