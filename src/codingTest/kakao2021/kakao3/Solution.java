package codingTest.kakao2021.kakao3;

import java.util.Stack;

class Solution {
    public static void main(String[] args) {
        String[] temp = new String[]{"D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"};
        String bob = solution(8, 2, temp);
        System.out.println(bob);
    }
    
    public static String solution(int n, int k, String[] cmd) {
        String answer = "";
        
        Table[] list = new Table[n];
        for(int i = 0; i < n; i++) {
        	list[i] = new Table();
        	list[i].id = i;
        	list[i].status = true;
        }
        
        int choose = k;
        Stack<Integer> resently = new Stack<>();
        
        for(int i = 0; i < cmd.length; i++) {
        	String[] temp = cmd[i].split(" ");

        	switch(temp[0]) {
        	case "U" :
        		int count = Integer.parseInt(temp[1]);
        		int indexfalse = 0;
        		for(int j = choose; j > choose - count; j--) {
        			if(list[choose].status == false) {
        				indexfalse += 1;
        			}
        		}
        		choose -= count + indexfalse;	
        		break;
        	case "D" :
        		do {
        			choose += Integer.parseInt(temp[1]);
        		} while(list[choose].status == false);
        		break;
        	case "C" :
        		list[choose].status = false;
        		resently.push(choose);
        		do {
        			choose += 1;
        			if(choose >= n) {
        				do {
        					choose -= 1;
        				}while(list[choose].status == false);
        			}
        		} while(list[choose].status == false);
        		
        		break;
        	case "Z" :
        		int index = resently.pop();
        		list[index].status = true;
        		break;
        	}
        }
        
        for(int i = 0; i < n; i++) {
        	if(list[i].status == true) {
        		answer += "O";
        	} else {
        		answer += "X";
        	}
        }
        return answer;
    }
    
    static class Table {
        int id;
        boolean status; // true면 O, false면 X
    }
    
    
}