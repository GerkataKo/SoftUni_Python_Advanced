nums_list=[int(x) for x in input().split()]
nums_positive=[x for x in nums_list if x>0]
nums_negative=[x for x in nums_list if x<0]
sum_positive=sum(nums_positive)
sum_negative=sum(nums_negative)
abs_sum_negative=abs(sum_negative)

print(sum_negative)
print(sum_positive)
if abs_sum_negative>sum_positive:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")