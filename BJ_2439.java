//BaekJoon2439
//작성자 : yazbyz
//20200601

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BJ_2439 {
	public static void main(String []args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N;
		
		N = Integer.parseInt(br.readLine());
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for(int i = 0 ; i < N; i++)
		{
			//띄어쓰기 0 ~ (전체 - 행 - 1)
			for(int t = 0; t < N - i - 1; t++)
			{
				bw.write(" ");
			}
			//별 출력
			for(int j = 0; j <= i; j++)
			{
				bw.write("*");	
			}
			//개행
			bw.write("\n");
		}
		
		bw.flush();
		bw.close();
	}
}
