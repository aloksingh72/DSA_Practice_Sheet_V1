class MaximumConsecutive{

	public static void main(String[] args){
	
	int[] arr= {1,1,0,1,1,1,0,1};
	
	
	int res = maxconsecutive(arr);
	System.out.println("The maximum number of consecutive 1's "+res);	
	}
	
	public static int maxconsecutive(int[] arr){
	int count =0,max_count =0;
	
	for(int i =0;i<arr.length;i++){
			if(arr[i] ==1){
				count++;	
			}
			else{
			count=0;
			}
			
			if(count>max_count){
			max_count = count;
			}
		}
		return max_count;
	}

}
