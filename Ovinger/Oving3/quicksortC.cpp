#include <iostream>
#include <string>
#include <sstream>
#include <deque>
#define DEQUE std::deque<std::pair<char,int> >

/* QUCIKSORT */
void _swap(DEQUE *arr, int one, int two) {
	std::pair<char, int>tmp = arr->at(two);
	arr->at(two) = arr->at(one);
	arr->at(one) = tmp;
}

int partition(DEQUE *arr, const int left, const int right) {
	const int mid = left + (right - left) / 2;
	const int pivot = arr->at(mid).second;
	_swap(arr, mid, left);
	int i = left + 1;
	int j = right;
	while (i <= j) {
		while (i <= j && arr->at(i).second <= pivot) {
			i++;
		}
		while (i <= j && arr->at(j).second > pivot) {
			j--;
		}
		if (i < j) {
			_swap(arr, i, j);
		}
	}
	_swap(arr, i - 1, left);
	return i - 1;
}

void quicksort(DEQUE *arr, const int left, const int right, const int sz) {
	if (left >= right) return;
	int part = partition(arr, left, right);
	quicksort(arr, left, part - 1, sz);
	quicksort(arr, part + 1, right, sz);
}

int main() {
	DEQUE deqDeck;
	std::string line;
	while (std::getline(std::cin, line)) {
		char letter = line[0];
		std::stringstream ss(line.substr(2));
		int i = 0;
		while (ss >> i) {
			deqDeck.push_back(std::make_pair(letter, i));
			if (ss.peek() == ','){
				ss.ignore();
			}
		}
	}
	int _size = deqDeck.size();
	quicksort(&deqDeck, 0, _size -1, _size);
	for (int i = 0; i < _size; i++) {
		std::cout << deqDeck.at(i).first;
	}
	std::cout << std::endl;
	return 0;
}