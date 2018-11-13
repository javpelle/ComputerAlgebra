package elem;

public class Entero implements Elem {

	private int elem;

	public Entero(int elem) {
		this.elem = elem;
	}
	
	public Elem clone() {
		return new Entero(elem);
	}

	public int getElem() {
		return elem;
	}

	public void setElem(int elem) {
		this.elem = elem;
	}

	public int getAbsElem() {
		return Math.abs(elem);
	}

	public String toString() {
		return String.valueOf(elem);
	}

}
