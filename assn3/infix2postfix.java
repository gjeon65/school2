/* @author Geun Jeon
 * CS 265 
 * Assignment 3
 * 2017-11-29
 * 
 * for instructions, @param
 * https://www.cs.drexel.edu/~kschmidt/CS265/Assignments/Java-Calc/
 * In short, make infix to postfix calculator. Take a text file with
 * expressions and evaluate using infix
 * to postfix.
 * 
 * Also, I did this assignment on Eclipse and applied here at PuTTy. There
 * is a major crashes and errors.
 * I played around to fix it but I can't seem to find solution.
 * Version checks out, implemented classes into one file.   
 */

package assn3;

import java.io.*;
import java.util.*;

public class infix2postfix{
	public String infixToPostfix(String infix) {
        Stack operatorStack = new Stack();  
        char c;       
        StringTokenizer parser = new StringTokenizer(infix,"+-*/%() ",true);
        StringBuffer postfix = new StringBuffer(infix.length());
        while (parser.hasMoreTokens()) {     
        	String token = parser.nextToken();
        	c = token.charAt(0);         
         if ( (token.length() == 1) && isOperator(c) ) {    
            while (!operatorStack.empty() &&
                !getPrec(((String)operatorStack.peek()).charAt(0), c))
           
               postfix.append(" ").append((String)operatorStack.pop());
            if (c==')') {
                  String operator = (String)operatorStack.pop();
                  while (operator.charAt(0)!='(') {
                     postfix.append(" ").append(operator);
                     operator = (String)operatorStack.pop();  
                  }
            }
            else
               {operatorStack.push(token);}
         }
         else if ( (token.length() == 1) && isWhitespace(c) ) {   
             }
         else { 
           postfix.append(" ").append(token);  
         }
       }
      while (!operatorStack.empty())
         {postfix.append(" ").append((String)operatorStack.pop());}
   
      return postfix.toString();
 }
	
	private static final char Add = '+';
	private static final char Sub = '-';
	private static final char Mult = '*';
	private static final char Div = '/';
	private static final char Mod ='%';



   private boolean isOperator(char c) { 

     return c == '+'  ||  c == '-'  ||  c == '*'  ||  c == '/'  ||  c == '%'
           || c=='(' || c==')';
   
   }

   private boolean isWhitespace(char c) {  

     return c == ' ';
   
   }

   private boolean getPrec(char op1, char op2) {

      switch (op1) {

         case '+':
         case '-':
            return !(op2=='+' || op2=='-') ;

         case '*':
         case '/':
         case '%':
            return  op2=='(';

         

         case '(': return true;

         default:  
            return false;
      }
 
   } 

   

   public int evaluate(String expr) {

	       Stack stack = new Stack();
	        int op1, op2, result = 0;
	        String token;
	        StringTokenizer tokenizer = new StringTokenizer(expr);

	        while (tokenizer.hasMoreTokens()) {
	            token = tokenizer.nextToken();
	            char c = token.charAt(0); 
	            if (isOperator(c)) {
	                op2 = ((Integer) stack.pop()).intValue();
	                op1 = ((Integer) stack.pop()).intValue();
	                result = evalSingleOp(token.charAt(0), op1, op2);
	                stack.push(new Integer(result));
	            }
	            else
	                stack.push(new Integer(Integer.parseInt(token)));
	        }

	        result = ((Integer) stack.pop()).intValue();
	        return result;
	    }
   
   private int evalSingleOp(char operation, int op1, int op2) {
	        int result = 0;

	        switch (operation) {
	            case Add :
	                result = op1 + op2;
	                break;
	            case Sub :
	                result = op1 - op2;
	                break;
	            case Mult :
	                result = op1 * op2;
	                break;
	            case Div :
	                result = op1 / op2;
	            case Mod :
	                result = (int) Math.floorMod(op1,op2);
	        }

	        return result;
	    }


public static void main(String[] args) {  

	try{
		File file = new File("./input.infix");
		FileReader fileReader = new FileReader(file);
		BufferedReader bufferedReader = new BufferedReader(fileReader);
		StringBuffer stringBuffer = new StringBuffer();
		String line;
		while ((line = bufferedReader.readLine()) != null) {
			infix2postfix converter = new infix2postfix();
			stringBuffer.append(line);
			stringBuffer.append("\n");
			System.out.println("input: \t\t"+line);
			System.out.println("postfix: \t"+converter.infixToPostfix(line));
			String infixed = converter.infixToPostfix(line);
			System.out.println("Evalute: \t" + converter.infixToPostfix(line)+ 
					" = "+converter.evaluate(infixed));
		}
		fileReader.close();
		
		
	} catch (IOException e){
		e.printStackTrace();
	}
   
   infix2postfix converter = new infix2postfix();

  
} 
   

}
