//BaekJoon11022
//ÀÛ¼ºÀÚ : yazbyz
//20200531

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BJ_11022 {
	public static void main(String []args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for(int i = 0 ; i < T; i++)
		{
			bw.write("Case #" + (i+1) + ": " + array[i] + "\n");
		}
		bw.flush();
		bw.close();
	}
}
