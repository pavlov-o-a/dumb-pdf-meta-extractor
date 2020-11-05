def getNextInt(f):
	start = f.tell()
	nums = b'0123456789'
	result = []
	i = f.read(1)
	start = f.tell()
	while i not in nums and f.tell() - start < 40: 
		i = f.read(1)
	start = f.tell()
	while i in nums and f.tell() - start < 40: 
		result.append(i); 
		i = f.read(1)
	return result
def seekFromEndTo(f, key):
	f.seek(-2, 2)
	queue = [b'a']*len(key)
	while f.tell() > 1:
		queue.insert(0,f.read(1))
		queue.pop(-1)
		if queue == key:
			return
		f.seek(-2,1)
def getObject(f):
	result = []
	queue = [f.read(1), f.read(1)]
	while True:
		if queue == [b'<', b'<']: result = []
		if queue == [b'>', b'>']:
			result.pop(); result.pop() 
			return result
		b = f.read(1)
		result.append(b)
		queue.append(b)
		queue.pop(0)
def getMeta(f):
	#looking for "/Info" tag in trailer 
	seekFromEndTo(f, [b'/',b'I',b'n',b'f',b'o'])
	if f.tell() == 0: return "No meta in pdf"
	#getting index of  info object
	objN = getNextInt(f)
	objC = getNextInt(f)
	#looking for info object
	seekFromEndTo(f, objN + [b' '] + objC + [b' '] + [b'o',b'b',b'j'])
	if f.tell() == 0: return "No meta in pdf"
	#getting meta from info object
	meta = getObject(f)
	return ''.join(x.decode() for x in meta)
print('Enter path to pdf')
with open(input(), 'rb') as f:
	print(getMeta(f))
