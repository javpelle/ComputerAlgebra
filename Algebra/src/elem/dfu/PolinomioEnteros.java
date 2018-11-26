package elem.dfu;

import java.util.ArrayList;

import elem.dominioEuclideo.DominioEuclideo;
import elem.polinomio.Polinomio;

public class PolinomioEnteros extends DFU<Integer> {

	public PolinomioEnteros(DominioEuclideo<Integer> de) {
		super(de);
	}


	private static final Polinomio<Integer> cero = new Polinomio<Integer>(0);
	
	@Override
	public boolean igual(Polinomio<Integer> e1, Polinomio<Integer> e2) {
		if (e1.size() == e2.size()) {
			for (int i = 0; i < e1.size(); ++i) {
				if (e1.get(i) != e2.get(i)) {
					return false;
				}
			}
			return true;
		}
		return false;
	}


	@Override
	public Polinomio<Integer> suma(Polinomio<Integer> e1, Polinomio<Integer> e2) {
		Polinomio<Integer> nuevo;
		if (e1.size() > e2.size()) {
			nuevo = clone(e1);
			for (int i = 0; i < e2.size(); ++i) {
				nuevo.set(i, nuevo.get(i) + e2.get(i));
			}
		} else {
			nuevo = clone(e2);
			for (int i = 0; i < e1.size(); ++i) {
				nuevo.set(i, nuevo.get(i) + e1.get(i));
			}
		}
		return nuevo;		
	}

	@Override
	public Polinomio<Integer> resta(Polinomio<Integer> e1, Polinomio<Integer> e2) {
		Polinomio<Integer> nuevo;
		if (e1.size() > e2.size()) {
			nuevo = clone(e1);
			for (int i = 0; i < e2.size(); ++i) {
				nuevo.set(i, nuevo.get(i) - e2.get(i));
			}
		} else {
			nuevo = clone(e2);
			for (int i = 0; i < e1.size(); ++i) {
				nuevo.set(i, nuevo.get(i) - e1.get(i));
			}
		}
		return nuevo;	
	}

	@Override
	public Polinomio<Integer> producto(Polinomio<Integer> e1, Polinomio<Integer> e2) {
		Polinomio<Integer> nuevo = new Polinomio<Integer>(new ArrayList<Integer>());
		int nuevoSize = e1.size() + e2.size() - 1;
		for (int i = 0; i < nuevoSize; ++i) {
			nuevo.add(0);
		}
		for (int i = 0; i < e1.size(); ++i) {
			for (int j = 0; j < e2.size(); ++j) {
				nuevo.set(i + j, nuevo.get(i + j) + e1.get(i) * e2.get(j));
			}
		}
		return nuevo;
	}

	@Override
	public Polinomio<Integer> getCero() {
		return cero;
	}


	@Override
	public Polinomio<Integer> clone(Polinomio<Integer> e) {
		ArrayList<Integer> list = new ArrayList<Integer>();
		for (int i = 0; i < e.size(); ++i) {
			list.add(e.get(0));
		}
		return new Polinomio<Integer>(list);
	}
	
	

	
	


}
