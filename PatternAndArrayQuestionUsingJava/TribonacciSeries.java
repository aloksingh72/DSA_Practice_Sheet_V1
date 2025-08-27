
//WAP:- Print the Tribonacci Series 
import java.util.Scanner;
class TribonacciSeries {
    public static void main(String[] args) {
        System.out.println("Enter the number of terms:-");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x =0,y=1,z=1;
        System.out.println("Tribonacci series:-");
        System.out.print(x+" ");
        System.out.print(y+" ");
        System.out.print(z+" ");
        int w = x+y+z;
        for(int i =4;i<=n;i++){
            x= y;
            y=z;
            z=w;
            w=x+y+z;
            System.out.print(w+" ");
        }
        System.out.println();
    }
}


