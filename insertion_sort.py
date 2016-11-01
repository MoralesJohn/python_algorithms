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
def insertion_sort(arr):
	# initialize swap and iterative variables
	temp = 0
	sort_ndx = 1
	# iterate array
	while sort_ndx < len(arr):
		temp = arr[sort_ndx]
		# chk_ndx is the index of the already-sorted value we are comparing the tmep variable against
		chk_ndx = 0
		for i in reversed(range(sort_ndx)):
			# search the sorted values for correct place to insert temp
			if arr[i] > temp:
				# shift larger values right
				arr[i+1] = arr[i]
			else:
				# correct location found
				chk_ndx = i + 1
				break
		# place swap value, increment sort index and end while loop
		arr[chk_ndx] = temp
		sort_ndx += 1
	# return sorted array and end function
	return arr

print insertion_sort(testarr)

# calculate and print elapsed time
print "It took: ", datetime.datetime.now() - start