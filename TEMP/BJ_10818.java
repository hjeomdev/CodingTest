//BaekJoon10818
//ÀÛ¼ºÀÚ : yazbyz
//20200606

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class BJ_10818 {
	public static void main(String []args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N;
		ArrayList<Integer> array = new ArrayList<Integer>();
		
		N = Integer.parseInt(br.readLine());
		
		String tmp = br.readLine();
		String[] temp = new String[N];
		temp = tmp.split(" ");
		
		for(int i = 0; i < N; i++)
		{
			array.add(Integer.parseInt(temp[i]));
		}
		
		array.sort(null);
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		bw.write(array.get(0) + " " + array.get(N-1));
		
		
		bw.flush();
		bw.close();
	}
}
