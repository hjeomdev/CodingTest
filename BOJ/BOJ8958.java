//BaekJoon8958
//�ۼ��� : yazbyz
//20200607

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BOJ8958 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N;
		int[] score;
		String[] OX;
		String[][] array;
		
		N = Integer.parseInt(br.readLine());
		
		score = new int[N];
		OX = new String[N];
		array = new String[N][80];
		
		for(int i = 0; i < N; i++)
		{
			OX[i] = br.readLine();
			array[i] = OX[i].split("");
		}
		
		for(int i = 0; i < N; i++)
		{
			int combo = 1;
			
			for(int j = 0; j < array[i].length; j++)
			{
				if(array[i][j].equals("O")) 
				{
					if(combo == 1)
					{
						score[i]++;
					} else {
						score[i] += combo;
					}
					combo++;
				}
				
				if(array[i][j].equals("X")) 
				{
					combo = 1;
				}
			}
			
		}
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		for(int i = 0; i < N; i++)
		{
			bw.write(score[i] + "\n");
		}
		bw.flush();
		bw.close();
		

	}

}
