import random
# user inputs controlling how long the list is, what the biggest number can be, and if they want every step narrated
length = int(input("How big do you want your list to be? : "))
range = int(input("What is the biggest number that can be in your list?: "))
silent = (input("Do you want each step narrated? y/n: "))

# create an empty list which the users numbers will go into
testlist = []
i = 0  # variable that allows list to be appended to, up to "range" times

# generates a list with "range" random numbers in
while i < length:
    testlist.append(random.randint(1, range))
    i = i + 1
print("This is your original list: {}".format(testlist))


# Completes one pass of the bubble-sort, no narration
def Bubble_Pass_silent():
    j = 0
    while j < len(testlist) - 1:
        if testlist[j] > testlist[j+1]:
            smaller = int(testlist[j])
            bigger = int(testlist[j + 1])
            testlist.insert(j, bigger)
            testlist.insert(j + 1, smaller)
            del testlist[j + 2]
            del testlist[j + 2]
        j = j + 1


# Completes one pass of the bubble sort, with narration
def Bubble_Pass_narrated():
    j = 0
    while j < len(testlist) - 1:
        if testlist[j] < testlist[j+1]:
            print("{previous} is less than {next}, no swap needed".format(previous=testlist[j], next=testlist[j + 1]))
        elif testlist[j] == testlist[j+1]:
            print("{previous} is the same as {next}, no swap needed".format(previous=testlist[j], next=testlist[j + 1]))
        else:
            print("{previous} is bigger than {next}, swap is needed. Completing action now.".format(previous=testlist[j],next=testlist[j + 1]))
            smaller = int(testlist[j])
            bigger = int(testlist[j+1])
            testlist.insert(j, bigger)
            testlist.insert(j+1, smaller)
            del testlist[j+2]
            del testlist[j+2]
            # print(testlist)
        j = j + 1



req_passes = len(testlist) - 1

num_passes = 0
if silent == "y":
    while req_passes >= num_passes:
        print(testlist)
        Bubble_Pass_narrated()
        print("Pass number {} now completed".format(num_passes))
        num_passes = num_passes+1
else:
    while req_passes >= num_passes:
        Bubble_Pass_silent()
        num_passes = num_passes+1

print("Bubble sort now completed. It took {} passes to complete. See the sorted list below.".format(num_passes-1))
print(testlist)
