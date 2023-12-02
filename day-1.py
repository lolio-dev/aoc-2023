with open("sample.txt", 'r') as f:
	data = f.readlines()

total_sum = 0

numbers = {
	"zero": 0,
	"one": 1,
	"two": 2,
	"three": 3,
	"four": 4,
	"five": 5,
	"six": 6,
	"seven": 7,
	"eight": 8,
	"nine": 9
}

for fragment in data:
	local_nums = []
	local_chain = ""

	for i in fragment[:-1]:
		if i.isdigit():
			local_nums.append(int(i))
			local_chain = ""
		else:
			local_chain += i
			for number in numbers:
				if number in local_chain:
					local_nums.append(numbers.get(number))
					local_chain = ""
	if len(local_nums) >= 2:
		total_sum += int(str(local_nums[0]) + str(local_nums[-1]))
	else:
		total_sum += int(str(local_nums[0]) * 2)

print(total_sum)
