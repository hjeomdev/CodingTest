//BaekJoon15552
//ÀÛ¼ºÀÚ : yazbyz
//20200531

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BJ_15552 {
	public static void main(String []args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T;
		int[][] array;
		
		T = Integer.parseInt(br.readLine());
		array = new int[T][3];
		
		for(int i = 0; i < T; i++) {
			String temp = br.readLine();
			String[] arrTemp = temp.split(" ");
			
			array[i][0] = Integer.parseInt(arrTemp[0]);
			array[i][1] = Integer.parseInt(arrTemp[1]);
			array[i][2] = array[i][0] + array[i][1];
		}
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for(int i = 0; i < T; i++)
		{
			bw.write(array[i][2] + "\n");	
		}
        bw.flush();
		bw.close();
	}
}
