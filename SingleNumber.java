class SingleNumber{

	public static void main(String[] args){
	
	int[] arr= {4,1,2,2,1};
	
	
	int res = singlenumber(arr);
	System.out.println("The single number is "+res);	
	}
	
	public static int singlenumber(int[] arr){
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
