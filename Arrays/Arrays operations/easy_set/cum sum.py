# Function to return the cumulative sum list
def cumulative_list(old_list):

	for i in range(1, len(old_list)):
		old_list[i] = old_list[i-1] + old_list[i]

	return old_list

if __name__ == "__main__":
	old_list = [10, 20, 30, 40, 50]

	print("Original List:")
	for item in old_list:
		print(item, end=" ")
	print()

	cumulative_list_result = cumulative_list(old_list)

	print("Cumulative Sum List:")
	for item in cumulative_list_result:
		print(item, end=" ")
