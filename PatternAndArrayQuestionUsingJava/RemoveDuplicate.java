class RemoveDuplicate{
	public static void main(String[] args){

	int[] arr = {1,1,2,2,2,3,3,4};
	//method calling
	int k = removeduplicate(arr);
	for(int i =0;i<k;i++){
		System.out.print(arr[i]+" ");
	}
}	
	//method declaration
	public static int removeduplicate(int[] arr){
	int i =0;
	for(int j=1;j<arr.length;j++){
		if(arr[i]!=arr[j]){
			i++;
			arr[i] = arr[j];
		}
	}
	return i+1;
}
}

