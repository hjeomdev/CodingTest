//BaekJoon2562
//ÀÛ¼ºÀÚ : yazbyz
//20200606

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BJ_2562 {
	public static void main(String []args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[] array = new int[10];
		int max = 0, maxIndex = 1;
		
		for(int i = 0; i < 9; i++)
		{
			array[i] = Integer.parseInt(br.readLine());
			
			if(i == 0)
				max = array[0];
			if(array[i] > max)
			{
				max = array[i];
				maxIndex = i + 1;
			}			
		}
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		bw.write(max + "\n" + maxIndex);
		
		
		bw.flush();
		bw.close();
	}
}
