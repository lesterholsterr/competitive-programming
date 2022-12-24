#include <iostream>
#include <cmath>

using namespace std;

// requires a return type, void = none
// "Declared before main"
void sayHi(string name, int age);
double cube(double num);
double myMax(double num1, double num2, double num3);
string getDayOfWeek(int dayNum);
double myExp(double base, int exp);

int main() {
  // // Single quote for char, double for string (mandatory!)
  // string characterName = "Bob";
  // char grade = 'F';

  // // Double can store more decimal points than float, which is more niche
  // int age = 100;
  // double gpa = 2.3;

  // // Prints out 0 for false, 1 for true
  // bool isMale = true;

  // // cout = consule out
  // // endl = end line (and start a new one)
  // cout << false << isMale << end
  

  // // STRINGS
  // string phrase = "I don't know what to name this";
  // cout << phrase.length() << endl;
  // cout << phrase[0] << endl;
  // phrase[0] = 'A';
  // cout << phrase << endl;
  // cout << phrase.find("what", 0) << endl;
  // // First parameter is start index, second parameter is # of chars to grab
  // cout << phrase.substr(13, 4) << endl;

  // // NUMBERS
  // cout << 10 / 3 << endl;
  // cout << 10 / 3.0 << endl;
  // cout << pow(2, 5) << endl;
  // double root2 = sqrt(2);
  // cout << round(root2) << endl;
  // cout << ceil(root2) << endl;
  // cout << floor(root2) << endl;
  // cout << fmax(root2, 1.5) << endl;
  // cout << fmin(root2, 1.5) << endl;

  // // USER INPUT
  // int age;
  // cout << "Enter your age: ";
  // cin >> age;
  // string fullName;
  // cout << "Enter your name: ";
  // // Seems like using getline after a cin doesn't work (I think same thing happenes in Java?)
  // string filler;
  // cin >> filler;
  // getline(cin, fullName);
  // cout << "Hello " << fullName;

  // // CALCULATOR (less scuffed)
  // double num1, num2, result;
  // char op;
  // cout << "First number: ";
  // cin >> num1;
  // cout << "Operator (+, -, *, /): ";
  // cin >> op;
  // cout << "Second number: ";
  // cin >> num2;
  // if (op == '+') {
  //   result = num1 + num2;
  // } else if (op == '-') {
  //   result = num1 - num2;
  // } else if (op == '*') {
  //   result = num1 * num2;
  // } else if (op == '/') {
  //   result = num1 / num2;
  // } else {
  //   cout << "Invalid operator";
  // }
  // cout << result;

  // // ARRAYS
  // int luckyNums[20] {5, 29, 58, 100};
  // cout << luckyNums[1];
  // luckyNums[2] = 69;
  // luckyNums[4] = 420;

  // // FUNCTIONS
  // sayHi("John", 20);
  // double answer = cube(2);
  // cout << answer << endl;

  // // IF STATEMENTS
  // bool isMale = true;
  // bool isTall = true;
  // if(isMale && isTall) {
  //   cout << "You are a tall male" << endl;
  // } else if(isMale && !isTall) {
  //   cout << "Hi Daniel :)" << endl;
  // } else {
  //   cout << "You are a female or one of those other genders..." << endl;
  // }
  // cout << myMax(3, 4, 5) << endl;

  // // SWITCHES
  // cout << getDayOfWeek(6);

  // // WHILE LOOPS
  // int index = 6;
  // do {
  //   cout << index << endl;
  //   index++;
  // } while (index <= 5);

  // // FOR LOOPS
  // int nums[] = {1, 2, 5, 7, 3};
  // for (int i = 0; i < 5; i++) {
  //   cout << nums[i] << endl;
  // }
  // cout << myExp(3, 4);

  // // 2D ARRAYS
  // // Rows THEN columns
  // int numberGrid[3][2] = {
  //   {1, 2},
  //   {3, 4},
  //   {5, 6}
  // };
  // for (int i = 0; i < 3; i++) {
  //   for (int j = 0; j < 2; j++) {
  //     cout << numberGrid[i][j] << " ";
  //   }
  //   cout << endl;
  // }

  // POINTERS
  // This is the memory address of a variable (where it is stored in RAM)
  // Wtf is the use case of this???
  int age = 19;
  int* pAge = &age;
  // Putting the asterisk in front is called "dereferencing"
  cout << pAge << " " << *pAge;

  
  
  return 0;
}


void sayHi(string name, int age) {
  cout << "Hi " << name << ", you are " << age << endl;
}

double cube(double num) {
  double result = num * num * num;
  return result;
  // Return breaks out of the function
  cout << "Hello";
}

double myMax(double num1, double num2, double num3) {
  int result;
  if (num1 > num2) {
    if (num1 > num3) {
      return num1;
    } else return num3;
  } else if (num3 > num2) {
    return num3;
  } else return num2;
}

string getDayOfWeek(int dayNum) {
  string dayName;

  switch (dayNum) {
  case 0:
    dayName = "Sunday";
    break;
  case 1:
    dayName = "Monday";
    break;
  case 2:
    dayName = "Tuesday";
    break;
  case 3:
    dayName = "Wednesday";
    break;
  case 4:
    dayName = "Thursday";
    break;
  case 5:
    dayName = "Friday";
    break;
  case 6:
    dayName = "Saturday";
    break;
  default:
    dayName = "Invalid Day Number";
  }

  return dayName;
}

double myExp(double base, int exp) {
  double power = 1;
  for (int i = 0; i < exp; i++) {
    power *= base;
  }
  return power;
}