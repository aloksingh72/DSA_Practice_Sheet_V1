class SecondSmallestLargest{
	public static void main(String[] args){
	
	int[] arr = {1,2,4,7,7,5};
	//int[] arr = {1};
	int n = arr.length;
	int res = secondsmallestlargest(arr,n);
	System.out.println("The second largest element is:"+res);
	int result = secondsmallest(arr,n);
	System.out.println("The second smallest element is:"+result);
	}
	
	public static int secondsmallestlargest(int[] arr,int n ){
	int max= Integer.MIN_VALUE;
	int secondlargest = Integer.MIN_VALUE;
	//int max= -1;
	//int secondlargest = -1;
	
	if(n<2){
		return -1;
	}
	
	for(int i =0;i<arr.length;i++){
			if(arr[i] > max){
				secondlargest = max;
				max =arr[i];
			}
			else if(arr[i] > secondlargest && arr[i] != max){
				secondlargest = arr[i];
			}
		}
	return secondlargest;
	}
	
	public static int secondsmallest(int[] arr,int n){
	int min= Integer.MAX_VALUE;
	int secondsmallest = Integer.MAX_VALUE;
	
	if(n<2){
		return -1;
	}
	
	for(int i =0;i<arr.length;i++){
		if(arr[i] < min){
			secondsmallest = min;
			min = arr[i];
		}
		else if (arr[i] <secondsmallest && arr[i] !=min){
			secondsmallest = arr[i];
		}
	}
	return secondsmallest;
	
	
	}

}
