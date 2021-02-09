"""
f0 = 0
f1 = 1
fn = fn-1 + fn-2
"""
# tinh fibonacy thu n
def fibonacy(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibonacy(n-1)+fibonacy(n-2)


if __name__ == '__main__':
	n = int(input())
	result = fibonacy(n)
	print(result)