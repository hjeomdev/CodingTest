//BaekJoon10430
//�ۼ��� : yazbyz
import java.util.Scanner;

public class BOJ10430 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		int A, B;
		
		do {
			A = scan.nextInt();
			B = scan.nextInt();
		}while((A/100 <= 0) || (B/100 <= 0));
		
		System.out.println(A * (B%10));
		System.out.println(A * (B%100/10));
		System.out.println(A * (B/100));
		
		System.out.println(A * B);
		
		scan.close();
	}

}
