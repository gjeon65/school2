/*
* @author: Geun Jeon
* @date: 12-03-2017
* @Description: CS 265 lab 09
* @see https://www.cs.drexel.edu/~kschmidt/CS265/Labs/9.html
*
*/
import java.lang.*;
import java.io.*;
import java.util.*;

public class gInt {
	public int real=0;
	public int imag=0;
	
	public gInt(int r){
		real = r;
	}
	public gInt(int r, int i){
		real = r;
		imag = i;
	}
	public int real(){
		return real;
	}
	public int imag(){
		return imag;
	}
	public gInt add(gInt rhs) {
		gInt result = new gInt((real + rhs.real()),(imag + rhs.imag()));
		return result; 
	}
	public gInt multiply(gInt rhs) {
		gInt product = new gInt((real*rhs.real())-(imag*rhs.imag()),
				(real*rhs.imag())+(imag*rhs.real()));
		return product; 
	}
	public float norm() {
		return (float)Math.sqrt((real*real)+(imag*imag));
	}
	public static void main(String[] args)
	{
		//System.out.print("Test");
	}
	public boolean equals(Object obj)
	{
		if(obj instanceof gInt)
		{
			gInt tObj=(gInt)obj;
			return (tObj.real()==real() && tObj.imag()==imag());
		}
		return false;


	}
}

