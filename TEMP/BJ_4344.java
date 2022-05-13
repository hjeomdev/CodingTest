//BaekJoon4344
//ÀÛ¼ºÀÚ : yazbyz
//20200609

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BJ_4344 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int C, N;
		int[] score;
		double[] average;
		double[] ratio;
		
		C = Integer.parseInt(br.readLine());
		
		average = new double[C];
		ratio = new double[C];
		
		for(int i = 0; i < C; i++)
		{
			String temp = br.readLine();
			String[] tmp = temp.split(" ");
			
			N = Integer.parseInt(tmp[0]);
			double total = 0;
			
			for(int j = 1; j <= N; j++)
				total += Integer.parseInt(tmp[j]);
			average[i] = total / N;
			
			for(int j = 1; j <= N; j++)
				if(Integer.parseInt(tmp[j]) > average[i])
					ratio[i]++;					
			ratio[i] = (ratio[i] / N) * 100;
		}
		
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		for(int i = 0; i < C; i++)
		{
			bw.write(String.format("%.3f", ratio[i]) + "%\n");
		}
		bw.flush();
		bw.close();
		

	}

}
