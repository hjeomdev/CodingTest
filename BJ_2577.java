//BaekJoon2577
//ÀÛ¼ºÀÚ : yazbyz
//20200606

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class BJ_2577 {
	public static void main(String []args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int A, B, C;
		int total;
		String[] tt;
		int[] count = new int[10];
		
		A = Integer.parseInt(br.readLine());
		B = Integer.parseInt(br.readLine());
		C = Integer.parseInt(br.readLine());
		
		total = A*B*C;
		
		tt = (Integer.toString(total)).split("");
		
		for(int i = 0; i < tt.length; i++)
		{
			switch(tt[i])
			{
				case "0":
					count[0]++;
					break;
				case "1":
					count[1]++;
					break;
				case "2":
					count[2]++;
					break;
				case "3":
					count[3]++;
					break;
				case "4":
					count[4]++;
					break;
				case "5":
					count[5]++;
					break;
				case "6":
					count[6]++;
					break;
				case "7":
					count[7]++;
					break;
				case "8":
					count[8]++;
					break;
				case "9":
					count[9]++;
					break;
			}
		}
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		for(int i = 0; i < 10; i++)
		{
			bw.write(count[i] + "\n");
		}
		
		bw.flush();
		bw.close();
	}
}
