str="apna college"
print(str[:6])#[0:5]
print(str[6:1])#[start>end aur step default +1ho,to empty string return hoti hain]
print(str[5:])#from index 5 to last value
print(str[1:6:2])#start from index 1 end at 6 ad step3 har 2nd alphabet /character lo)
print(str[1:6:-1])# +ve slicing ocur left to right cond:start<end
#-ve slicing occur from right to left cond:start>end
#give empty
print(str[6:1:-1])#start from index6 and end at index 2 decrement of one by one value occur till index2