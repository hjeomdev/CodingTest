package codingTest.kakao2021.kakao1;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

class Solution {
	public static void main(String[] args) {
        int bob = solution("one4seveneight");
        System.out.println(bob);
    }
	
    public static int solution(String s) {
        int answer = 0;
        
        String[][] numbers = {{"0", "zero"}, {"1", "one"}, 
        		{"2", "two"}, {"3", "three"}, {"4", "four"},
        		{"5", "five"}, {"6", "six"}, {"7", "seven"},
        		{"8", "eight"}, {"9", "nine"}};
        
//        int count = 1;
//        for(int i = 0; i < numbers.length; i++) {
//        	// 숫자 
//        	if(s.lastIndexOf(numbers[i][0]) != -1) {
//            	answer += Integer.parseInt(numbers[i][0]) * Math.pow(10, count);
//            	s = s.replace(numbers[i][0], "");
//        	} 
//        	System.out.println(answer);
//        	
//        	// 영어 
//        	if(s.indexOf(numbers[i][1]) != -1) {
//            	answer += Integer.parseInt(numbers[i][0]) * Math.pow(10, s.indexOf(numbers[i][0]));
//            	s = s.replace(numbers[i][0], "");
//        	}
//        	System.out.println(answer);
//        }
        
//        List<Integer, Integer> temp = new List<Integer, Integer>();
//        int count = 0;
//        
//        // 숫자 
//        for(int i = 0; i < numbers.length; i++) {
//        	if(s.indexOf(numbers[i][0]) != -1) {
//        		temp[i][0] = s.indexOf(numbers[i][0]);
//        		temp[i][1] = Integer.parseInt(numbers[i][0]);
//        		count++;
//        	}
//        	
//        	System.out.println(temp[i]);
//            
//        }
//        
//        // 영어 
//        for(int i = 0; i < numbers.length; i++) {
//        	
//        	temp[i][0] = s.indexOf(numbers[i][1]);
//        	temp[i][1] = Integer.parseInt(numbers[i][0]);
//        	count++;
//        }
//        
//       Arrays.sort(temp, (o1, o2) -> {
//    	   if(o1[0] == o2[0]) {
//    		   return Integer.compare(o1[1], o2[1]);
//    	   } else {
//    		   return Integer.compare(o1[0], o2[0]);
//    	   }
//       });
//       
        
        return answer;
    }
}