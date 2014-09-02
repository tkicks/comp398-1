#include "stdafx.h"
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

//Jonathan Liss
//File name: source.cpp
//Date Last Modified: 9/2/2014
//This program takes a text file with a column of state names and a column of state abbreviations and displays them




class LL			//simple linked list class
{
	struct Node 
	{
		string info;		//building a space for our text inside the node
		Node *nextNode;		//pointer to the next node
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


	string getText()			//look into the node and return text
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

	ifstream fileobject("C:\\Users\\Jonathan\\Documents\\states.txt"); // open a filestream (this path needs to be modified each time.. sorry)
	string file;
	while (getline(fileobject, file))					//loop through the text file and grab each line
	{
		list.addLine(file);								//add the text to the node and then print using the .getText() function
		cout <<  list.getText() << endl << endl;		

	}
	fileobject.close();
	

	system("Pause");
	return 0;
}