import java.util.Scanner;
class LinearSearch {
    public static void main(String[] args) {
   int[] arr = {1,2,3,4,5,6,7};
   
   for(int i = 0;i<arr.length;i++){
       System.out.print(arr[i]+" ");
   }
    Scanner sc  = new Scanner(System.in);
    System.out.println();
   System.out.println("Enter the number you want to search:-");
   int nums = sc.nextInt();
 linearsearch(arr,nums);
 
}
public static int linearsearch(int[] arr,int nums){
 
   for(int i =0;i<arr.length;i++){
       if(arr[i] == nums){
           System.out.print(nums+" is present at "+i+"th index");
           
       }
       
   }
   return -1;
}
}

