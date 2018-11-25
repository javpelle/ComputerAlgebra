package elem;

public class Complejo {

	private Double real;
	private Double compleja;

	public Complejo(Double real, Double compleja) {
		this.real = real;
		this.compleja = compleja;
	}

	public boolean igual(Complejo complejo2) {
		return real == complejo2.getReal() && compleja == complejo2.getCompleja();
	}

	public Complejo suma(Complejo complejo2) {
		return new Complejo(real + complejo2.getReal(), compleja + complejo2.getCompleja());
	}

	public Complejo resta(Complejo complejo2) {
		return new Complejo(real - complejo2.getReal(), compleja - complejo2.getCompleja());
	}

	public Complejo producto(Complejo complejo2) {
		return new Complejo(real * complejo2.getReal() - compleja * complejo2.getCompleja(),
				real * complejo2.getCompleja() + compleja * complejo2.getReal());
	}

	public Complejo division(Complejo complejo2) {
		Double a = real, b = compleja, c = complejo2.getReal(), d = complejo2.getCompleja();
		return new Complejo((a * c + b * d) / (c * c + d * d),
				(b * c - a * d) / (c * c + d * d));
	}
	
	public String toString() {
		if (compleja >= 0.0) {
			return real.toString() + " +" + compleja.toString() + "i"; 
		} else {
			return real.toString() + " " + compleja.toString() + "i"; 
		}
	}

	public Double getReal() {
		return real;
	}

	public Double getCompleja() {
		return compleja;
	}
}
