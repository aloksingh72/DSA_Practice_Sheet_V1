class RotateArrayByK{
	public static void main(String[] args){
	
	int[] arr = {1,2,3,4,5,6,7};
	int k=2;
	rotatearraytoright(arr,k);
	System.out.print("After Rotating the k elements to right ");
	
	for(int i =0;i<arr.length;i++){
		System.out.print(arr[i]+" ");
		
	}
		System.out.println();
	}
	
	public static void rotate(int[] arr,int start,int end){
	while(start<=end){
	
		int temp = arr[start];
		arr[start] = arr[end];
		arr[end]= temp;
		start++;
		end--;
		}
	}
	
	public static void rotatearraytoright(int[] arr,int k){
	int n = arr.length;
	
	k = k%n;
	if(k>n){
	return;
	}
	
	rotate(arr,0,n-1);
	rotate(arr,0,k-1);
	rotate(arr,k,n-1);
	
	}
	
}
