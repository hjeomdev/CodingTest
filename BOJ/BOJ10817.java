//BaekJoon10817
//�ۼ��� : yazbyz
//20200603

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class BOJ10817 {
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
		
		//Arrays.sort(�迭��) : ����, ����, �ѱ� �迭 ��� �ø����� ���� ����
		Arrays.sort(ABC);
		
		/*Arrays.sort(���ڰ�, int fromIndex, int toIndex)
		* ���ڰ�
		* 1. primitive data type array(byte[], char[], double[], long[], int[], float[]
		* 2. Object array(Integer[], Double[], Character[]) 
		*/
		//Arrays.sort(�迭��, Collections.reverseOrder()) : �������� ����
		
			
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(ABC[1] + "\n");
		bw.flush();
		bw.close();
	}
	
}
