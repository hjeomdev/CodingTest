//BaekJoon10950
//작성자 : yazbyz

import java.io.BufferedReader;
import java.io.InputStreamReader;

//20200530 BaekJoon2753
//작성자 : yazbyz

public class BJ_10950 {
	public static void main(String []args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = 0;
		int[][] array;
		
		T = Integer.parseInt(br.readLine());
		
		array= new int[T][2];
		
		for(int i = 0; i < T; i++) {
			String temp = br.readLine();
			String[] arrTemp = temp.split(" ");
			array[i][0] = Integer.parseInt(arrTemp[0]);
			array[i][1] = Integer.parseInt(arrTemp[1]);
		}
		
		for(int i = 0; i < T; i++) {
			System.out.println(array[i][0] + array[i][1]);
		}
		
	}
}
