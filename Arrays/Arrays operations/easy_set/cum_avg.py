def cumulative_average(nums):
    cumulative_sum = 0
    cumulative_averages = []

    for i, num in enumerate(nums):
        cumulative_sum += num
        cumulative_averages.append(cumulative_sum / (i + 1))

    return cumulative_averages

def main():
    nums = list(map(int, input("Enter a list of numbers separated by space: ").split()))
    averages = cumulative_average(nums)

    print("Cumulative averages: ", averages)

if __name__ == "__main__":
    main()
