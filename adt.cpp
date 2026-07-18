#include <iostream>
#include <conio.h>
#include <string.h>

struct student
{
    int rollno;
    char name[30];
    float marks;
};

void createstudent(student &s)
{
     cout<<"\nEnter Roll Number : "; cin>>s.rollNo;
     cout<<"Enter Name : ";/ cin>>s.rollno;
     cout<<"Enter Marks : ";/ cin>>s.Marks;

    
     

void displaystudent (student s)
{
    if(s.rollNo==0) {count<<"\nNo student Record Found!";return; }
    count<<"\nRoll Number : "<<s.name;
    count<<"\nMarks : "<<s.marks;
}

void updatestudent (student &s)
{
    if(s.rollNo==0){ count<<"\nNo Record available!"; return; }
    count<<"\nEnter New Name : "; cin>>s.name;
    count<<"Enter New Marks : "; cin>>s.marks;
}

void deletestudent (student &s)
{
    s.rollNo=0;
    strcpy(s.name," ");
    s.marks=0;
}

void main()
{
    student s; s.rollNo=0;
    int ch;
    do{
        count<<"\n1.create\n2.display\n3.update\n4.delete\n5.Exit\n";
        cin>>ch;
        switch(ch) {
            case 1:createstudent (s) ;break;
            case 2:displaystudent (s) ;break;
            case 3:updatestudent (s) ;break;
            case 4:deletestudent (s) ;count<<"\nDelete",break;
                }
    }while (ch!=5);
    getch();

}