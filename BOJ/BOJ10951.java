//BaekJoon10951
//�ۼ��� : yazbyz
//20200602

import java.util.Scanner;

public class BOJ10951 {
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
		 * hasNext() �޼ҵ�� �Էµ� ��ū�� ������ true�� ��ȯ�Ѵ�.
		 * 
		 * scanner.next(), scanner.nextInt()�� 
		 * ��ū�� �����ϴ� ����, �ٹٲ��� ���� ����.
		 * 
		 * scanner.nextInt() �޼ҵ�� ����� �Է��� ������ ���๮�ڸ� ���� �ʰ� 
		 * ���๮�� �������� ���ڷ� �Է¹���. 
		 * scanner.nextLine()�� ������� �Է��� String���� ����.
		 * �׷��� scanner.nextInt()������ scanner.nextLine()�� ȣ���ϸ�
		 * scanner.nextLine()�� �����ִ� ���๮�ڸ� �Է¹ް� ��
		 */
		scan.close();
	}
}
