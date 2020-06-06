//BaekJoon31546
//ÀÛ¼ºÀÚ : yazbyz
//20200606

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;

public class BJ_1546 {
	public static void main(String []args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N;
		int[] score;
		int M = 1;
		double[] newScore;
		int newAverage;
		
		N = Integer.parseInt(br.readLine());
		
		score = new int[N];
		newScore = new double[N];
		
		String[] temp = new String[N];
		String tmp = br.readLine();
		temp = tmp.split(" ");
		
		for(int i = 0; i < N; i++)
		{
			score[i] = Integer.parseInt(temp[i]);
			if(i == 0) 
			{
				M = score[0];
			}
			
			if(M < score[i])
			{
				M = score[i];
			}
		}
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int total = 0;
		for(int i = 0; i < N; i++)
		{
			newScore[i] = (score[i]/M)*100;
			bw.write(newScore[i]+"\n");
			total += newScore[i];
		}
		
		newAverage = total/N;
	
//		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		bw.write(Integer.toString(newAverage));
		
		bw.flush();
		bw.close();
	}
}
