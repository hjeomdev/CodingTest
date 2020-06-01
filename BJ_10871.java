//BaekJoon10871
//ÀÛ¼ºÀÚ : yazbyz
//20200601

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BJ_10871 {
	public static void main(String []args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N, X;
		int[] array;
		
		String temp = br.readLine();
		String[] arrTemp = temp.split(" ");
		
		N = Integer.parseInt(arrTemp[0]);
		X = Integer.parseInt(arrTemp[1]);
		
		array = new int[N];
		
		temp = br.readLine();
		arrTemp = temp.split(" ");
		for(int i = 0; i < N; i++) 
		{
			array[i] = Integer.parseInt(arrTemp[i]);
		}
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for(int i = 0 ; i < N; i++)
		{
			if(array[i] < X)
			{
				bw.write(Integer.toString(array[i]) + " ");
			}
		}
		bw.flush();
		bw.close();
	}
}
