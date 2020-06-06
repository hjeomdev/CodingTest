//BaekJoon3052
//ÀÛ¼ºÀÚ : yazbyz
//20200606

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;

public class BJ_3052 {
	public static void main(String []args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[] As = new int[10];
		int B = 42;
		Map<Integer, Integer> map = new HashMap<Integer, Integer>();
		
		for(int i = 0; i < 10; i++)
		{
			As[i] = Integer.parseInt(br.readLine());
			
			int result = As[i] % B;
			if(map.containsKey(result))
			{
				map.put(result, map.get(result)+1);
			} else {
				map.put(result, 1);
			}
		}
	
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		bw.write(Integer.toString(map.size()));
		
		bw.flush();
		bw.close();
	}
}
