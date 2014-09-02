#include "stdafx.h"
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

class LL
{
	struct Node 
	{
		string info;
		Node *nextNode;
	};

public:
	// constructor
	LL()
	{
		firstNode = 0;			//set head to 0
	}
	void addLine(string line)
	{
		Node *n = new Node();   //create new Node
		n->info = line;            
		n->nextNode = firstNode;         
		firstNode = n;               
	}

	string getText()
	{
		Node *n = firstNode;
		string txt = n->info;
		firstNode = firstNode->nextNode;
		return txt;
	}


private:
	Node *firstNode;			//this points to the first node
};

int main() 
{
	LL list;

	fstream fileobject("C:\\Users\\Jonathan\\output.txt"); // open a filestream
	string file;
	while (fileobject >> file)
	{
		//cout << file << endl;
		list.addLine(file);


	}
	fileobject.close();
	

	for (short i = 0; i < 43; i++)
	{
		cout << list.getText() << endl;
		cout << endl;
	}

	system("Pause");
	return 0;
}