//BaekJoon4673
//ÀÛ¼ºÀÚ : yazbyz
//20200617

import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class BJ_4673 {
	
	static int N = 10000;
	static int[] numbers = new int[N];
	static int[] memo = new int[N];

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		
		for(int i = 0; i < N; i++)
		{
			numbers[i] = i + 1;
			memo[i] = 0;
		}
		
		for(int i = 0; i < N; i++)
			self_nonSelf(numbers[i]);
		
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for(int i = 0; i < N; i++)
			if(memo[i] == 0)
				bw.write(Integer.toString(numbers[i]) + "\n");
		
		bw.flush();
		bw.close();
	}
	
	static void self_nonSelf(int n) {
		int new_n = n;
		String str_n = Integer.toString(n);
		String[] strarr_n = str_n.split("");
		
		for(int i = 0; i < strarr_n.length; i++)
		{
			new_n += Integer.parseInt(strarr_n[i]);
		}
		
		if(new_n - 1 < N)
			memo[new_n - 1] = 1;
		
	}

}
