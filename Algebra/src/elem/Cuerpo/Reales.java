package elem.Cuerpo;

public class Reales extends Cuerpo<Double> {

	@Override
	public boolean igual(Double e1, Double e2) {
		return e1 == e2;
	}

	@Override
	public Double suma(Double e1, Double e2) {
		return e1 + e2;
	}

	@Override
	public Double resta(Double e1, Double e2) {
		return e1 - e2;
	}

	@Override
	public Double producto(Double e1, Double e2) {
		return e1 * e2;
	}

	@Override
	public Double division(Double e1, Double e2) {
		return e1 / e2;
	}

	@Override
	public Double getCero() {
		return 0.0;
	}

	@Override
	public Double getUno() {
		return 1.0;
	}

}
