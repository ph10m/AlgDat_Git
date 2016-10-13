#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import stdin
from PIL import Image

def visualize_graph(coords, k):
    filtered_coords = [(k*coord[0], k*coord[1]) for coord in coords if coord != (-1, -1)]

    if len(filtered_coords) > 0:
        dimensions = (max(coord[0] for coord in filtered_coords) + k, max(coord[1] for coord in filtered_coords) + k)

        image = Image.new('RGB', dimensions)
        pixels = image.load()
        for x, y in filtered_coords:
            for i in range(k):
                for j in range(k):
                    pixels[x+i, y+j] = (255, 255, 255)

        image.show()

class Node:
	def __init__(self, x, y):
		self.x,self.y = x,y
		self.children = []
		self.parent = None
	
	def add_child(self, n):
		self.children.append(n)
		
	def add_parent(self, n):
		self.parent = n

def binary_graph(A):
    # SKRIV DIN KODE HER
    # Du må mest sannsynlig lage egne hjelpefunksjoner for denne funksjonen for å løse oppgaven
    # Funksjonen skal returnere koordinatene til hver node i en heap
	x,y = 1,0 # coords
	root = Node(x,y)
	while len(root.children)<2:
		# this root has no children
		
	
	

def main():
	A = stdin.readline().strip().split(" ")
	print (A)
	# visualize_graph(A, 30)
	print(binary_graph(A), end='')

	


visualize_graph([(1, 0), (0, 2), (2, 2), (-1, -1), (1, 4), (-1, -1), (3, 4)], 30)

main()