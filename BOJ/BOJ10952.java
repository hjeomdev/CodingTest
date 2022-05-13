//BaekJoon10952
//�ۼ��� : yazbyz
//20200601

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class BOJ10952 {
	public static void main(String []args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int A, B;
		ArrayList<Integer> list = new ArrayList<Integer>();
		
		do {
			String temp = br.readLine();
			String[] arrTemp = temp.split(" ");
			
			A = Integer.parseInt(arrTemp[0]);
			B = Integer.parseInt(arrTemp[1]);
			
			list.add(A + B);
		}while(A != 0 && B != 0);
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for(int i = 0; i < list.size() - 1; i++)
		{
			bw.write(list.get(i) + "\n");
		}
		bw.flush();
		bw.close();
	}
}
