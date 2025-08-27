import java.util.*;
class UnionOfArray {
    public static void main(String[] args) {
   int[] arr1 = {1,2,3,4,9,9};
   int[] arr2 = {2,2,3,4,5,6,7,8,9};

        //method calling
   unionofarray(arr1,arr2);
 
}
//method decalation
public static void unionofarray(int[] arr1,int[] arr2){
 //because we need dynamic array
 List<Integer> temp = new ArrayList<>();
 int i =0,j=0;
 
   while(i<arr1.length && j<arr2.length){
       if(arr1[i] <arr2[j]){
             if (temp.size() == 0 || temp.get(temp.size() - 1) != arr1[i]) {
        temp.add(arr1[i]);
    }
           i++;
       }
       else if(arr1[i] > arr2[j]){
            if (temp.size() == 0 || temp.get(temp.size() - 1) != arr2[j]) {
        temp.add(arr2[j]);
    }
           j++;
       }
       else if(arr1[i] == arr2[j]){
           if (temp.size() == 0 || temp.get(temp.size() - 1) != arr1[i]) {
        temp.add(arr1[i]);
    }
           i++;
           j++;
       }
       
   }
   // add the remaining element 
   while(i<arr1.length){
         if (temp.size() == 0 || temp.get(temp.size() - 1) != arr1[i]) {
        temp.add(arr1[i]);
    }
       i++;
   }
   while(j<arr2.length){
         if (temp.size() == 0 || temp.get(temp.size() - 1) != arr2[j]) {
        temp.add(arr2[j]);
    }
       j++;
   }
   
    for(int k = 0;k<temp.size();k++){
      System.out.print(temp.get(k)+" ");
  }
   
 
}
}

