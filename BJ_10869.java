import java.util.Scanner;

public class BJ_10869 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		int A, B;
		do{
			A = scan.nextInt();
		}while(A < 0);
		
		do {
			B = scan.nextInt();
		}while(B > 10000);
		
		System.out.println(A + B);
		System.out.println(A - B);
		System.out.println(A * B);
		System.out.println(A / B);
		System.out.println(A % B);		
		
		scan.close();
	}

}
