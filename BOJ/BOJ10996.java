//BaekJoon10996
//�ۼ��� : yazbyz
//20200606

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BOJ10996 {
	public static void main(String []args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N;
		String[][] array;
		
		N = Integer.parseInt(br.readLine());
		array = new String[2][N];
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		for(int i = 0; i < N; i+=2)
		{
			array[0][i] = "*";
			array[1][i] = " ";
		}
		for(int i = 1; i < N; i+=2)
		{
			array[0][i] = " ";
			array[1][i] = "*";
		}
		
		
		//���
		for(int j = 0; j < N; j++)
		{
			for(int i = 0; i < N; i++)
				bw.write(array[0][i]);
			
			bw.write("\n");
			
			for(int i = 0; i < N; i++)
				bw.write(array[1][i]);
			
			bw.write("\n");
		}
		
		bw.flush();
		bw.close();
	}
}
