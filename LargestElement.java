import java.util.Scanner;

class LargestElement{
	public static void main(String[] args){
	//Scanner sc = new Scanner(System.in);
	//System.out.println("Enter the number");
	//int n = sc.nextInt();
	
	int[] arr = {2,0,1,3,5};
	int res = largestElement(arr);
	System.out.println("The largest element of the aray is: "+res);
	
	}
	//method declaration
	public static int largestElement(int arr[]){
		int max =arr[0];
		for(int i =0;i<=arr.length-1;i++){
			 if(arr[i] > max){
			 	max =arr[i];
			 }
		}
		return max;
	}

}
