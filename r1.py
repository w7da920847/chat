def read_file(fileName):
	lines = []
	with open(fileName, 'r', encoding = 'utf-8-sig') as f:
		for line in f :
			lines.append(line.strip())
	return lines

def convert(lines) :
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person :
			new.append(person +': '+ line)
	return new

def write_file(fileName, lines):
	with open(fileName, 'w', encoding = 'utf-8-sig') as f :
		for line in lines :
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	#print(lines)
	lines = convert(lines)
	write_file('output.txt', lines)


main()