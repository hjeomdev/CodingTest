//BaekJoon4673
//ÀÛ¼ºÀÚ : yazbyz
//20200609

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BJ_4673 {
	
	static int N = 50;
	static int[] numbers = new int[N];

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		
		for(int i = 0; i < N; i++)
		{
			numbers[i] = i + 1;
		}
		
		for(int i = 0; i < N; i++)
			if(numbers[i] != 0)
				self_nonSelf(numbers[i]);
		
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for(int i = 0; i < N; i++)
			if(numbers[i] != 0)
				bw.write(Integer.toString(numbers[i]) + "\n");
		
		bw.flush();
		bw.close();
	}
	
	static void self_nonSelf(int n) {
		int origin_n = n;
		int new_n = n;
		
		for(int i = 0; origin_n > 0; i++)
		{
			new_n += origin_n % 10;
			origin_n -= origin_n%10;
		}
		
		if(new_n-1 <= N)
			numbers[new_n-1] = 0;
		
	}

}
