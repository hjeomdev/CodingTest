//BaekJoon31546
//ÀÛ¼ºÀÚ : yazbyz
//20200606

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BJ_1546 {
	public static void main(String []args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N;
		int[] score;
		int M = 1;
		double[] newScore;
		double newAverage;
		
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
		
		double total = 0;
		for(int i = 0; i < N; i++)
		{
			newScore[i] = ((double)score[i]/M)*100;
			total += newScore[i];
		}
		
		newAverage = total/N;
	
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		bw.write(Double.toString(newAverage));
		
		bw.flush();
		bw.close();
	}
}
