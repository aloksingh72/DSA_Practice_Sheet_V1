import java.util.Scanner;

class Pattern1{
public static void main(String[] args){

		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number");
		int n  = sc.nextInt();
	
		//method  calling
		squarepattern(n);
		
		sc.close();
	}
//method decalration
public static void squarepattern(int n){
		for(int i =0;i<=n;i++){
			for(int j =0;j<n;j++){
				System.out.print("*  ");
			}
			System.out.println(" ");
		}
	}
}
