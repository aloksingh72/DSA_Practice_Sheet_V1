//Find the number that appears once, and the other numbers twice
//Input Format: arr[] = {4,1,2,1,2}
//Output_Result: 4
//Explanation: In this array, only element 4 appear once and the other elements appear twice. So, 4 is the answer.
class SingleNumber{

	public static void main(String[] args){
	
	int[] arr= {1,2,1};
	
	// functin calling
	int res = singlenumber(arr);
	System.out.println("The single number is "+res);	
	}
	// function declaration
	public static int singlenumber(int[] arr){
	
	int element = 0;
	for(int i=0;i<arr.length;i++){
		int count =0;
		element = arr[i];
		//find the occurence
		for(int j=0;j<arr.length;j++){
			if(arr[j] == element){
			
				count++;
				}
			}
		if(count ==1){
			return element;
		}
		
		}
		return -1;
	}

}
