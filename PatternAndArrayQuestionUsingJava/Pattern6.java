import java.util.Scanner;

class Pattern6{
	public static void main(String[] args){
	Scanner sc = new Scanner(System.in);
	System.out.println("Enter the number");
	int n = sc.nextInt();
	upper_right_triangle_2(n);
	
	}
	
	public static void upper_right_triangle_2(int n){
		
		for(int i =0;i<n;i++){
		int m =1;
			for(int j =n;j>i;j--){
				System.out.print(m+" ");
				m++;
			}
			System.out.println();
		
		
		}
	
	}

}
