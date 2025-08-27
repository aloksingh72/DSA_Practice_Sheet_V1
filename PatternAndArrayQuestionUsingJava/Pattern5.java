import java.util.Scanner;

class Pattern5{
	public static void main(String[] args){
	Scanner sc = new Scanner(System.in);
	System.out.println("Enter the number");
	int n = sc.nextInt();
	upper_right_triangle(n);
	
	}
	
	public static void upper_right_triangle(int n){
		
		for(int i =0;i<=n;i++){
			for(int j =n;j>=i;j--){
				System.out.print("* ");
			}
			System.out.println();
		
		
		}
	
	}

}
