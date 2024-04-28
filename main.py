import stats

numbers = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

median = stats.compute_median(numbers)
mode = stats.compute_mode(numbers)
mean = stats.compute_mean(numbers)

print("Median:", median)
print("Mode:", mode)
print("Mean:", mean)
