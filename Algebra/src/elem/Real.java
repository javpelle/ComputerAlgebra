package elem;

public class Real implements Elem {

	private double elem;

	public Real(double elem) {
		this.elem = elem;
	}
	
	public Elem clone() {
		return new Real(elem);
	}

	public double getElem() {
		return elem;
	}

	public void setElem(double elem) {
		this.elem = elem;
	}

	public String toString() {
		return String.valueOf(elem);
	}

}
