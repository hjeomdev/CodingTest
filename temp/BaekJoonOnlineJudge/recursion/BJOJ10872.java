// 팩토리얼 
// 10분

import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BJOJ10872 {
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		int result = factorial(n);

		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(result + "\n");
		bw.flush();
		bw.close();
	}

	public static int factorial(int n){
		if(n == 0 || n == 1) {
			return 1;
		}
		return n * factorial(n - 1);
	}
}