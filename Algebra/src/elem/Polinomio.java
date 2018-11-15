package elem;

import java.util.ArrayList;

public class Polinomio<T> {
	
	// en Z[x], 4x^2 -x +3 queda polinomio = [3, -1, 4]
	private ArrayList<T> polinomio;
	
	public String toString() {
		String aux = "";
		for (int i = polinomio.size() - 1; i >= 0; --i) {
			aux += sign(polinomio.get(i), i);
		}
		return null;
	}

	private String sign(T t, int i) {
		return  t + "x^" + String.valueOf(i);
	}
	
}
