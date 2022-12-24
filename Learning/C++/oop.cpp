#include <iostream>
#include <cmath>

using namespace std;

// CLASS
// The "blueprint" of a datatype
// Naming convention - capital letter
// Semicolon after close bracket!
class Book {
  // public means any code outside of this class can access it
  public:
    string title;
    string author;
    int pages;

    // CONSTRUCTORS
    // Function that helps initialize an object easily
    // Can create multiple constructors (Ex. one with no parameters could be a default initialization)
    Book(string aTitle, string aAuthor, int aPages) {
      title = aTitle;
      author = aAuthor;
      pages = aPages;
    }
};

class Book2 {
  public:
    // Fancy Constructor
    Book2(string title, string author, int pages) : title(title), author(author), pages(pages) { }
    string title;
    string author;
    int pages;
};

class Student {
  private:
    double gpa;

  public:
    string name;
    string major;
    Student(string aName, string aMajor, double aGpa){
      name = aName;
      major = aMajor;
      setGpa(aGpa);
    }

    // SETTER
    // Allows you to validate user input
    // I think having the variable be public still works... people say private is better but I don't understand why yet
    void setGpa(double aGpa) {
      if (0 <= aGpa && aGpa <= 4.0) {
        gpa = aGpa;
      }
      else {
        gpa = -1;
      };
    }

    // GETTER
    // Since gpa is stored privately, we must call this function to fetch it instead of using student.gpa
    double getGpa() {
      return gpa;
    }

    // OBJECT FUNCTIONS
    // Any Student variable can call this
    bool hasHonours() {
      if(gpa >= 3.5) {
        return true;
      } return false;
    }
};

// Superclass
class Chef {
  public:
    void makeChicken() {
      cout << "The chef makes chicken" << endl;
    }
    void makeSalad() {
      cout << "The chef makes salad" << endl;
    }
    void makeSpecialDish() {
      cout << "The chef makes BBQ ribs" << endl;
    }
};

// INHERITENCE
// Subclass
class ItalianChef : public Chef {
  public:
    void makePasta() {
      cout << "The chef makes pasta" << endl;
    }
    void makeSpecialDish() {
      cout << "The chef makes pineapple pizza" << endl;
    }
};

int main()
{
  // OBJECTS
  // An instance of a class
  Book book1("Harry Potter", "J. K. Rowling", 400);
  book1.pages = 420;

  Student student1("Jim", "Business", 5);
  cout << student1.getGpa() << endl;
  Student student2("Pam", "Art", 3.6);
  cout << student2.hasHonours() << endl;

  Chef chef;
  chef.makeSpecialDish();

  ItalianChef italianChef;
  italianChef.makeSpecialDish();

  Book2 book2("Lord of the Rings", "J. R. R. Tolkien", 900);
  cout << book2.author;

  return 0;
}