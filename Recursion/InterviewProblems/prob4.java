/*
 * prob4.java
 * Copyright (C) 2019 victor <victor@archlinux>
 *
 * Distributed under terms of the MIT license.
 */

import java.util.*;

public class prob4
{
	public static void main(String[] args){

		List<Integer> coins = new ArrayList<Integer>();
		coins.add(1);
		coins.add(2);
		System.out.println(rec_coins(3,coins));

	}
	
	private static int rec_coins(int target, List<Integer> coins){
		
		int sum = 0;
		// Base case 
		//if (coins.contains(target))
		//	return 0;
		// Recursive case
		int coin = 0;
		for (int i=0; i<coins.size(); i++){
			coin = coins.get(i);
			// case 1 - if the coin is bigger then the targeet
			if (target < coin){
				coins.remove(i);
				return 0;
			}
			// case 2 - if coin can make up the target with summing itself
			if ( target % coin == 0)
				sum = 1;
			sum += rec_coins(target, coins);
			}
		return sum;
		}
			
}
	

