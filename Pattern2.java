import java.util.Scanner;

class Pattern2{
	public static void main(String[] args){
	Scanner sc = new Scanner(System.in);
	System.out.println("Enter the number");
	int n = sc.nextInt();
	right_triangle(n);
	
	}
	
	public static void right_triangle(int n){
		for(int i =0;i<n;i++){
			for(int j =0;j<=i;j++){
				System.out.print("* ");
			}
			System.out.println();
		
		}
	
	}

}
