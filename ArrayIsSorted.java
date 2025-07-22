class ArrayIsSorted{
	
	public static void main(String[] args){
	//int[] arr = {1,2,3,4,5,6,7,8,9};
	int[] arr = {1,4,5,2,6,5,2};
	//method calling
	boolean res =  sortedarray(arr);
	if(res){
		System.out.println("The given array is sorted:- "+res);
	}
	else{
		System.out.println("the given array is sorted:- "+res);
	}
	}
	// method declaration 
	public static boolean sortedarray(int[] arr){
	for(int i =0;i<arr.length-1;i++){
	
		if(!(arr[i] <arr[i+1])){
				return false;
		
			}
		}
		return true;
	}
}
