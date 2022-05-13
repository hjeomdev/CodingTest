//BaekJoon2523
//�ۼ��� : yazbyz
//20200603

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BOJ2523 {
	public static void main(String []args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N;
		
		N = Integer.parseInt(br.readLine());
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for(int i = 0 ; i < N; i++)
		{
			for(int j = 0; j <= i; j++)
			{
				bw.write("*");	
			}
			bw.write("\n");
		}
		for(int i = N - 1 ; i >= 0; i--)
		{
			for(int j = i - 1; j >= 0; j--)
			{
				bw.write("*");	
			}
			bw.write("\n");
		}
		
		bw.flush();
		bw.close();
	}
}
