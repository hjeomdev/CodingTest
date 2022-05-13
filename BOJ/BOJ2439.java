//BaekJoon2439
//�ۼ��� : yazbyz
//20200601

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BOJ2439 {
	public static void main(String []args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N;
		
		N = Integer.parseInt(br.readLine());
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for(int i = 0 ; i < N; i++)
		{
			//���� 0 ~ (��ü - �� - 1)
			for(int t = 0; t < N - i - 1; t++)
			{
				bw.write(" ");
			}
			//�� ���
			for(int j = 0; j <= i; j++)
			{
				bw.write("*");	
			}
			//����
			bw.write("\n");
		}
		
		bw.flush();
		bw.close();
	}
}
