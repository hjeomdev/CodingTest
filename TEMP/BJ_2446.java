//BaekJoon2446
//ÀÛ¼ºÀÚ : yazbyz
//20200606

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BJ_2446 {
	public static void main(String []args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N;
		int k = 1;
		
		N = Integer.parseInt(br.readLine());
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		for(int i = 0; i < N; i++)
		{
			for(int t = 0; t < i; t++)
				bw.write(" ");
			
			for(int j = 0; j < 2*N-k; j++)
				bw.write("*");
			k += 2;
			
			bw.write("\n");
		}
		k = 3;
		for(int i = N - 1; i > 0; i--)
		{
			for(int t = i - 1; t > 0; t--)
				bw.write(" ");
			
			for(int j = 0; j < k; j++)
				bw.write("*");
			k += 2;
			
			bw.write("\n");
		}
		
		bw.flush();
		bw.close();
	}
}
