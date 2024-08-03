// 
// 234218 Data Structures 1.
// Semester: 2023B (spring).
// Wet Exercise #1.
// 
// Recommended TAB size to view this file: 8.
// 
// The following main file is necessary to link and run your code.
// This file is READ ONLY: even if you submit something else, the compiler ..
// .. WILL use our file.
// 

#include "pirates24b2.h"
#include <string>
#include <iostream>

using namespace std;

void print(string cmd, StatusType res);
void print(string cmd, output_t<int> res);

int main()
{
	
    int d1, d2;

    // Init
    oceans_t *obj = new oceans_t();
	
    // Execute all commands in file
	string op;
	while (cin >> op)
    {
        if (!op.compare("add_fleet")) {
            cin >> d1;
            print(op, obj->add_fleet(d1));
        } else if (!op.compare("add_pirate")) {
            cin >> d1 >> d2;
            print(op, obj->add_pirate(d1, d2));
        } else if (!op.compare("pay_pirate")) {
            cin >> d1 >> d2;
            print(op, obj->pay_pirate(d1, d2));
        } else if (!op.compare("num_ships_for_fleet")) {
            cin >> d1;
            print(op, obj->num_ships_for_fleet(d1));
        } else if (!op.compare("get_pirate_money")) {
            cin >> d1;
            print(op, obj->get_pirate_money(d1));
        } else if (!op.compare("unite_fleets")) {
            cin >> d1 >> d2;
            print(op, obj->unite_fleets(d1, d2));
        } else if (!op.compare("pirate_argument")) {
            cin >> d1 >> d2;
            print(op, obj->pirate_argument(d1, d2));
        } else {
            cout << "Unknown command: " << op << endl;
            return -1;
        }
        // Verify no faults
        if (cin.fail()){
            cout << "Invalid input format" << endl;
            return -1;
        }
    }

    // Quit 
	delete obj;
	return 0;
}

// Helpers
static const char *StatusTypeStr[] =
{
   	"SUCCESS",
	"ALLOCATION_ERROR",
	"INVALID_INPUT",
	"FAILURE"
};

void print(string cmd, StatusType res) 
{
	cout << cmd << ": " << StatusTypeStr[(int) res] << endl;
}

void print(string cmd, output_t<int> res)
{
    if (res.status() == StatusType::SUCCESS) {
	    cout << cmd << ": " << StatusTypeStr[(int) res.status()] << ", " << res.ans() << endl;
    } else {
	    cout << cmd << ": " << StatusTypeStr[(int) res.status()] << endl;
    }
}
