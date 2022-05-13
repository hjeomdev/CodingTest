// 피보나치 
// 8분

import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BOJ10870 {
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		int result = fibonaci(n);

		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(result + "\n");
		bw.flush();
		bw.close();
	}

	public static int fibonaci(int n){
		if(n == 0) {
			return 0;
		} else if(n == 1) {
			return 1;
		} 

		return fibonaci(n - 2) + fibonaci(n - 1);
	}
}