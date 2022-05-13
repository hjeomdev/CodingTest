//BaekJoon10951
//작성자 : yazbyz
//20200602

import java.util.Scanner;

public class BJ_10951 {
	public static void main(String []args) throws Exception {
		Scanner scan = new Scanner(System.in);
		
		while(scan.hasNext())
		{
			int A = scan.nextInt();
			int B = scan.nextInt();
			//String C = scan.nextLine();
			
			System.out.println(A + B);
			//System.out.println(C);
		}
		
		/*
		 * hasNext() 메소드는 입력된 토큰이 있으면 true를 반환한다.
		 * 
		 * scanner.next(), scanner.nextInt()는 
		 * 토큰을 구분하는 공백, 줄바꿈은 읽지 않음.
		 * 
		 * scanner.nextInt() 메소드는 사용자 입력의 마지막 개행문자를 읽지 않고 
		 * 개행문자 전까지만 숫자로 입력받음. 
		 * scanner.nextLine()은 사용자의 입력을 String으로 받음.
		 * 그래서 scanner.nextInt()다음에 scanner.nextLine()을 호출하면
		 * scanner.nextLine()은 남아있는 개행문자를 입력받게 됨
		 */
		scan.close();
	}
}
