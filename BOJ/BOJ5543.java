//BaekJoon5543
//�ۼ��� : yazbyz
//20200603

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BOJ5543 {
	public static void main(String []args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[] score = new int[5];
		int average = 0;
		int total = 0;
		
		for(int i = 0; i < 5 ; i++)
		{ 
			score[i] = Integer.parseInt(br.readLine());
			
			if(score[i] < 40) 
			{
				score[i] = 40;
			}
			
			total += score[i];
		}
		
		average = total / 5;
			
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(average + "\n");
		bw.flush();
		bw.close();
	}
	
}
