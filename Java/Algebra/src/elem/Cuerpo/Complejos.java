package elem.Cuerpo;

import elem.Complejo;

public class Complejos extends Cuerpo <Complejo> {
	
	private static final Complejo cero = new Complejo(0.0, 0.0);
	private static final Complejo uno = new Complejo(1.0, 0.0);

	@Override
	public boolean igual(Complejo e1, Complejo e2) {
		return e1.equals(e2);
	}

	@Override
	public Complejo suma(Complejo e1, Complejo e2) {
		return e1.suma(e2);
	}

	@Override
	public Complejo resta(Complejo e1, Complejo e2) {
		return e1.resta(e2);
	}

	@Override
	public Complejo producto(Complejo e1, Complejo e2) {
		return e1.producto(e2);
	}

	@Override
	public Complejo getCero() {
		return cero;
	}

	@Override
	public Complejo division(Complejo e1, Complejo e2) {
		return e1.division(e2);
	}

	@Override
	public Complejo getUno() {
		return uno;
	}

	@Override
	public Complejo clone(Complejo e) {
		return e.clone();
	}

}
