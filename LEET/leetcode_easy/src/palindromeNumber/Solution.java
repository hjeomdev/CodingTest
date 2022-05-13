package palindromeNumber;

class Solution {
	public static boolean isPalindrome(int x) {
       /*
		// < 내 코드 전체 요약 : x를 문자열로 형변환해서 이용 >
        String[] num = Integer.toString(x).split("");
        
        for(int i = 0; i < num.length/2; i++) {
            if(!num[i].equals(num[num.length - i - 1])) {
                return false;
            }
        }
        return true;
		*/

		// another code from leetcode 
		// 설명 : 직접 그 수를 반대로 만들면서 확인
		int newX = 0;
        int temp = x;
        while(temp > 0){ //반복 조건 및 음수는 처음부터 거르는 조건 설정
            int remainder = temp%10;
            newX = newX *10 +remainder;
            temp = temp/10;
        }
        if(newX == x){
            return true;
        }
        
        
        return false;
    }

	public static void main(String[] args) {
		int num = 121;
		System.out.println(isPalindrome(num));
	}
}
