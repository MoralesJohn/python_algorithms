import random, datetime

# establish start time
start = datetime.datetime.now()

# various test cases
# testarr = [8,7,6,5,4,3,2,1]
# testarr = [8,3,6,1,2,5,4,7]
# testarr = [1,2,3,4,5,6,7,8]
# testarr = []

# generate array of 100 elements, randomized in range 0 - 10,000
testarr = []
for x in range (100):
	testarr.append(int(round(random.random()*10000)))

# actual sort algorithm
def selection_sort(arr):
	# sort_ndx will track area to be sorted
	sort_ndx = 0
	# iterate array
	while sort_ndx < len(arr)-1:
		# min_ndx and min_val are the location and value of the lowest number in the sort area
		min_ndx = sort_ndx
		min_val = arr[min_ndx]
		# iterate through the sort are, checking each value against min_val, updating min_val as needed
		for i in range (min_ndx+1, len(arr)):
			if min_val > arr[i]:
				min_ndx = i
				min_val = arr[i]
		# swap min_val to the bottom of the sort area and narrow the sort area; end while loop
		arr[min_ndx] = arr[sort_ndx]
		arr[sort_ndx] = min_val
		sort_ndx = sort_ndx + 1
	# return sorted array and end function
	return arr

print selection_sort(testarr)

# calculate and print elapsed time
print "It took: ", datetime.datetime.now() - start