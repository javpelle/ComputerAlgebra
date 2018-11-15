package elem.dominioEuclideo;

public class Enteros extends DominioEuclideo<Integer> {

	@Override
	public boolean igual(Integer e1, Integer e2) {
		return e1 == e2;
	}

	@Override
	public Integer suma(Integer e1, Integer e2) {
		return e1 + e2;
	}

	@Override
	public Integer resta(Integer e1, Integer e2) {
		return e1 - e2;
	}

	@Override
	public Integer producto(Integer e1, Integer e2) {
		return e1 * e2;
	}

	@Override
	public Integer division(Integer e1, Integer e2) {
		return e1 / e2;
	}

	@Override
	public int norma(Integer e) {
		return Math.abs(e);
	}

	@Override
	public Integer restoDiv(Integer e1, Integer e2) {
		return e1 % e2;
	}

	@Override
	public Integer getCero() {
		return 0;
	}

	@Override
	public Integer getUno() {
		return 1;
	}

	@Override
	public Integer clone(Integer elem) {
		return new Integer(elem);
	}

}