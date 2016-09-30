#include <iostream>
#include <string>
#include <sstream>
#include <deque>

using namespace std;
#define DEQUE deque<pair<char,int> >

DEQUE deq(DEQUE left, DEQUE right) {
	DEQUE temp;
	while (!left.empty() && !right.empty()){
		if (left.at(0).second <= right.at(0).second) {
			temp.push_back(left.front());
			left.pop_front();
		}
		else {
			temp.push_back(right.front());
			right.pop_front();
		}
	}
	if (!left.empty()){
		for (DEQUE::iterator it = left.begin(); it != left.end(); ++it) {
			temp.push_back(*it);
		}
	}
	if (!right.empty()) {
		for (DEQUE::iterator it = right.begin(); it != right.end(); ++it) {
			temp.push_back(*it);
		}
	}
	return temp;
}

DEQUE merge(DEQUE deck) {
	int _size = deck.size();
	if (_size == 2) {
		DEQUE leftMost(deck.begin(), deck.begin() + 1);
		DEQUE rightMost(deck.begin() + 1, deck.begin() + 2);
		return deq(leftMost, rightMost);
	}
	else if (_size == 1) {
		return DEQUE(deck.begin(), deck.begin() + 1);
	}
	else {
		size_t const half = _size / 2;
		DEQUE left(deck.begin(), deck.begin() + half);
		DEQUE right(deck.begin() + half, deck.end());
		return deq(merge(left), merge(right));
	}
}

int main() {
	DEQUE deqDeck;
	string line;
	while (getline(cin, line)) {
		char letter = line[0];
		stringstream ss(line.substr(2));
		int i = 0;
		while (ss >> i) {
			deqDeck.push_back(make_pair(letter, i));
			if (ss.peek() == ',') ss.ignore();
		}
	}
	deqDeck = merge(deqDeck);
  	while(!deqDeck.empty()){
      cout << deqDeck.at(0).first;
      deqDeck.pop_front();
    }
    cout << endl;
	return 0;
}