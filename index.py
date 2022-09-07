import sys
sum = int(sys.argv[2])
arr = []
for item in sys.argv[1].split(','):
	arr.append(int(item))
unordered_map = {}
for i in range(len(arr)):
    if sum - arr[i] in unordered_map:
        print("+ " + str(arr[i]) + "," + str(sum - arr[i]))
    unordered_map[arr[i]] = 1