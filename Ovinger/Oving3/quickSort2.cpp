#include <iostream>
#include <string>
#include <sstream>
#include <deque>
#include <vector>
#define vec std::vector<std::pair<char,int> >
vec _quick(vec*arr) {
	vec less, pivots, more;
	if (arr->size() <= 1) return *arr;
	else {
		int piv = arr->at(0).second;
      	for (int i=0;i<arr->size();i++){
          std::pair<char,int>tmp = arr->at(i);
          if (tmp.second < piv) less.push_back(tmp);
          else if (tmp.second > piv) more.push_back(tmp);
          else pivots.push_back(tmp);
        }
		less = _quick(&less);
		more = _quick(&more);
      	less.reserve(less.size()+pivots.size()+more.size());
      	less.insert(less.end(),pivots.begin(),pivots.end());
      	less.insert(less.end(),more.begin(),more.end());
		return less;
	}
}

int main() {
	std::string line;
	vec vecDeck;
	while (std::getline(std::cin, line)) {
		std::stringstream ss(line.substr(2));
		int i;
		while (ss >> i) {
			vecDeck.push_back(std::make_pair(line[0], i));
			if (ss.peek() == ',') {
				ss.ignore();
			}
		}
	}
	vecDeck = _quick(&vecDeck);
  	for (int i=0;i<vecDeck.size();i++) std::cout << vecDeck.at(i).first;
	std::cout << std::endl;
	return 0;
}