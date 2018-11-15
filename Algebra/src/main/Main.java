package main;

import elem.dominioEuclideo.Enteros;

public class Main {

	public static void main(String args[]) {
		Integer[] a = new Integer[] {3, 5, 7};
		Integer[] b = new Integer[] {4, 5, 33};
		Integer elem = (new Enteros()).chinoRestos(a, b);
		System.out.println(elem.toString());

	}

}
