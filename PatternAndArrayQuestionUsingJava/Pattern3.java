import java.util.Scanner;
// class for pattern 3

class Pattern3{
	// main method
	public static void main(String[] args){
	Scanner sc = new Scanner(System.in);
	System.out.println("Enter the number");
	int n = sc.nextInt();
		// method calling
	right_triangle2(n);
	
	}
	// method calling 
	public static void right_triangle2(int n){
		for(int i =0;i<n;i++){
			int m =1;
			for(int j =0;j<=i;j++){
				System.out.print(m);
				m++;
			}
			System.out.println();
		
		}
	
	}

}
