import java.util.Scanner;

class Pattern4{
	public static void main(String[] args){
	Scanner sc = new Scanner(System.in);
	System.out.println("Enter the number");
	int n = sc.nextInt();
	right_triangle_number(n);
	
	}
	
	public static void right_triangle_number(int n){
		int m =1;
		for(int i =0;i<n;i++){
			for(int j =0;j<=i;j++){
				System.out.print(m+" ");
			}
			System.out.println();
			m++;
		
		}
	
	}

}
