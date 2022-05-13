//BaekJoon2739
//�ۼ��� : yazbyz

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BOJ2739 {
	public static void main(String []args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N;
		String n;
		
		do {
		N = Integer.parseInt(br.readLine());
		}while(N < 0 || N > 10);
		
		n = Integer.toString(N);
		
		for(int i = 1; i < 10; i++) {
			System.out.println(n + " * " + i + " = " + (N * i));
		}
		
		
	}
}
