package elem.dfu;

import elem.Anillo;
import elem.dominioEuclideo.DominioEuclideo;
import elem.polinomio.Polinomio;

public abstract class DFU<T> implements Anillo<Polinomio<T>> {
	
	private DominioEuclideo<T> de;
	
	public DFU(DominioEuclideo<T> de) {
		this.de = de;
	}

	public Polinomio<T> mcd(Polinomio<T> e1, Polinomio<T> e2) {
		if (e2.size() > e1.size()) {
			return mcd(e2, e1);
		}
		return null;
	}
}
