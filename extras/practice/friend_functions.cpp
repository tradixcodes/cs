#include <iostream>

using namespace std;

class Person {
private:
    //if not declared the data and methods are assumed to be private
    string name;

public:
    Person(string n){
        name = n;
    }

    friend void display(Person person);

};

void display(Person person) {
        cout << "The person's name is:" << person.name << endl;
    }

int main (){
    Person p1("Alice");
    display(p1);

    return 0;
}