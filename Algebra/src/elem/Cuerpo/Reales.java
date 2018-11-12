package elem.Cuerpo;

import elem.Elem;
import elem.Real;

public class Reales extends Cuerpo {

	private static Real cero = new Real(0);
	private static Real uno = new Real(1);

	@Override
	public boolean igual(Elem e1, Elem e2) {
		return ((Real) e1).getElem() == ((Real) e2).getElem();
	}

	@Override
	public Elem suma(Elem e1, Elem e2) {
		return new Real(((Real) e1).getElem() + ((Real) e2).getElem());
	}

	@Override
	public Elem resta(Elem e1, Elem e2) {
		return new Real(((Real) e1).getElem() - ((Real) e2).getElem());
	}

	@Override
	public Elem producto(Elem e1, Elem e2) {
		return new Real(((Real) e1).getElem() * ((Real) e2).getElem());
	}

	@Override
	public Elem division(Elem e1, Elem e2) {
		return new Real(((Real) e1).getElem() / ((Real) e2).getElem());
	}

	@Override
	public Elem getCero() {
		return cero;
	}

	@Override
	public Elem getUno() {
		return uno;
	}

}
