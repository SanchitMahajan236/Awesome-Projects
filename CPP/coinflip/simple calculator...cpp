#include<iostream>
#include<cmath>
using namespace std;
int main(){
	int num;
	float a,b,c,ans,x1,x2;
	char op;
	cout<<"         Select Formate"<<endl;
	cout<<"-------------------------------------------"<<endl;
	cout<<"1.Simple Calculation."<<endl;
	cout<<"2.Roots of Quadratic Equation."<<endl;
	cout<<"3.Square root of a number"<<endl;
	cout<<"4.Simple Square, Cube of a single value."<<endl;
	cout<<"-------------------------------------------"<<endl;
	cin>>num;
	if(num==1){
	cout<<"Enter the question in this formate  2+5."<<endl;
	cin>>a>>op>>b;
	switch(op){
		case '+':
			ans=a+b;
			cout<<ans<<" Ans"<<endl;
			break;
		case '-':
			ans=a-b;
			cout<<ans<<" Ans"<<endl;
			break;
		case '*':
			ans=a*b;
			cout<<ans<<" Ans"<<endl;
			break;
		case '/':
			ans=a/b;
			cout<<ans<<" Ans"<<endl;
			break;
	}
	cout<<"-------------------------------------------"<<endl;
}
   else if(num==2){
   	cout<<"-------------------------------------------"<<endl;
	   cout<<"Enter the constant a: ";
   	cin>>a;
   	cout<<"Enter the constant b: ";
   	cin>>b;
   	cout<<"Enter the constant c: ";
   	cin>>c;
   	 x1=(-b+sqrt(pow(b,2)-(4*a*c)))/(2*a);
   	 x2=(-b-sqrt(pow(b,2)-(4*a*c)))/(2*a);
   	 cout<<"X1="<<x1<<" Ans"<<endl;
   	 cout<<"X2="<<x2<<" Ans"<<endl;
   	 cout<<"-------------------------------------------"<<endl;
   }
   else if(num==3){
   	cout<<"-------------------------------------------"<<endl;
   	cout<<"Enter a number: ";
   	cin>>a;
   	cout<<sqrt(a)<<" Ans"<<endl;
   	cout<<"-------------------------------------------"<<endl;
   }
   else if(num==4){
   	cout<<"-------------------------------------------"<<endl;
   	cout<<"Enter a number: ";
   	cin>>a;
   	cout<<"Enter its Power: ";
   	cin>>b;
   	cout<<pow(a,b)<<" Ans"<<endl;
   	cout<<"-------------------------------------------"<<endl;
   }
	return 0;
}
