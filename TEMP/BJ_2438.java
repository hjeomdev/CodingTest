//BaekJoon2438
//ÀÛ¼ºÀÚ : yazbyz
//20200601

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BJ_2438 {
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
		
		bw.flush();
		bw.close();
	}
}
