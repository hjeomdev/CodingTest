//BaekJoon10817
//작성자 : yazbyz
//20200603

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class BJ_10817 {
	public static void main(String []args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String s;
		String[] S = new String[3];
		int[] ABC = new int[3];
		
		s = br.readLine();
		S = s.split(" ");
		for(int i = 0; i < ABC.length; i++)
		{
			ABC[i] = Integer.parseInt(S[i]);
		}
		
		//Arrays.sort(배열명) : 숫자, 영문, 한글 배열 모두 올림차순 정렬 가능
		Arrays.sort(ABC);
		
		/*Arrays.sort(인자값, int fromIndex, int toIndex)
		* 인자값
		* 1. primitive data type array(byte[], char[], double[], long[], int[], float[]
		* 2. Object array(Integer[], Double[], Character[]) 
		*/
		//Arrays.sort(배열명, Collections.reverseOrder()) : 내림차순 정렬
		
			
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(ABC[1] + "\n");
		bw.flush();
		bw.close();
	}
	
}
