#!/usr/bin/python3

from sys import stdin


def max_value(widths, heights, values, paper_width, paper_height):
    # SKRIV DIN KODE HER
	pass

def best_val(w,h,v):
	for i in range(len(w)):
		area = w[i] * h[i]
		print ('value per size:',v[i]/area)
	
def main():
	widths = []
	heights = []
	values = []
	for triple in stdin.readline().split():
		dim_value = triple.split(':', 1)
		dim = dim_value[0].split('x', 1)
		width = int(dim[0][1:])
		height = int(dim[1][:-1])
		value = int(dim_value[1])
		widths.append(int(width))
		heights.append(int(height))
		values.append(int(value))
	best_val(widths,heights,values)

	print ('widths:',widths)
	print ('heights:',heights)
	print ('values:',values)
	for line in stdin:
		paper_width, paper_height = [int(x) for x in line.split('x', 1)]
		print ('paper w:',paper_width)
		print ('paper h:',paper_height)
	print((max_value(widths, heights, values, paper_width, paper_height)))


main()