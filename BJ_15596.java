//BaekJoon15596
//작성자 : yazbyz
//20200609

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BJ_15596 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		int n;
		int[] a;
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		n = Integer.parseInt(br.readLine());
		
		a = new int[n];
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(Long.toString(sum(a)));
		bw.flush();
		bw.close();
	}
	
	static long sum(int[] a) {
		long total = 0;
		
		for(int i = 0; i < a.length; i++) 
		{
			total += a[i];
		}
		
		return total;
	}
	
//제출한 답	
//	public class Test {
//	    long sum(int[] a) {
//	        long ans = 0;
//	        for(int i = 0; i < a.length; i++) 
//			{
//				ans += a[i];
//			}
//	        return ans;
//	    }
//	}

}
