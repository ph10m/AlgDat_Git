#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>

#define vec std::vector<int>

//vec _quick(vec* arr) {
//	vec less, pivots, more;
//	if (arr->size() <= 1) return *arr;
//	else {
//		int piv = arr->at(0);
//		for (const auto &i : *arr) {
//			if (i < piv) less.push_back(i);
//			else if (i > piv) more.push_back(i);
//			else pivots.push_back(i);
//		}
//		less = _quick(&less);
//		more = _quick(&more);
//		for (const auto &k : pivots) less.push_back(k);
//		for (const auto &k : more) less.push_back(k);
//		return less;
//	}
//}

int partition(vec *arr, int lo, int hi) {
	int piv = arr->at(hi);
	int i = lo - 1;
	for (int j = lo; j <= hi - 1; j++) {
		if (arr->at(j) <= piv) {
			i++;
			std::iter_swap(arr->begin() + i, arr->begin() + j);
		}
	}
	std::iter_swap(arr->begin() + (i+1), arr->begin() + (hi));
	return (i + 1);
}

void qSort(vec *arr, int lo, int hi) {
	if (lo < hi) {
		int part = partition(arr, lo, hi);
		qSort(arr, lo, part - 1);
		qSort(arr, part + 1, hi);
	}
}

int binSearch(vec *arr, int val) {
	int lo(0), mid(0), hi(arr->size() - 1);
	while (lo <= hi) {
		mid = (hi + lo) / 2;
		if (val < arr->at(mid)) hi = mid - 1;
		else if (val > arr->at(mid)) lo = mid + 1;
		else return mid;
	}
	return mid;
}

void find(vec *arr, int lo, int hi){
	int min(0), max(0);
	int a = binSearch(arr, lo);
	int b = binSearch(arr, hi);
	//std::cout << "Got... Min = " << min << ", Max = " << max << std::endl;
	if (arr->at(min)>lo && min != 0) min = arr->at(a - 1);
	else min = arr->at(a);
	
	if (b == arr->size()) b--;
	else if (arr->at(b) < hi && b < arr->size()-1) b++;
	max = arr->at(b);
	std::cout << min << " " << max << std::endl;
}

int main() {
	vec inList;
	std::string line;
	std::getline(std::cin, line);
	std::stringstream arrStream(line);
	int input;
	while (arrStream >> input) inList.push_back(input);
	qSort(&inList,0,inList.size()-1);

	while (std::getline(std::cin, line)){
		int n, lo, hi;
		std::istringstream ints(line);
		ints >> lo;
		ints >> hi;
		find(&inList, lo, hi);
	}
	while (true) {} //wait
	return 0;
}