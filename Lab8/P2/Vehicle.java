

public class Vehicle {
	private String regNo;
	private String manufacturer;
	private String owner;
	private double co2;
	private double co;
	private double hc;
	private String pollutionStatus;

	public void checkPollutionStatus()
	{
//		System.out.println(this.pollutionStatus);

	}

	@Override
	public String toString() {
		return " Reg No:" + regNo + ", Manufacturer:" + manufacturer + ", Owner:" + owner + ", Pollution Status="
				+ pollutionStatus;
	}
	

	public Vehicle() {
		// TODO Auto-generated constructor stub
	}

	public Vehicle(String regNo, String manufacturer, String owner, double co2, double co, double hc,
			String pollutionStatus) {
		super();
		this.regNo = regNo;
		this.manufacturer = manufacturer;
		this.owner = owner;
		this.co2 = co2;
		this.co = co;
		this.hc = hc;
		this.pollutionStatus = pollutionStatus;
	}

	public String getRegNo() {
		return regNo;
	}

	public void setRegNo(String regNo) {
		this.regNo = regNo;
	}

	public String getManufacturer() {
		return manufacturer;
	}

	public void setManufacturer(String manufacturer) {
		this.manufacturer = manufacturer;
	}

	public String getOwner() {
		return owner;
	}

	public void setOwner(String owner) {
		this.owner = owner;
	}

	public double getCo2() {
		return co2;
	}

	public void setCo2(double co2) {
		this.co2 = co2;
	}

	public double getCo() {
		return co;
	}

	public void setCo(double co) {
		this.co = co;
	}

	public double getHc() {
		return hc;
	}

	public void setHc(double hc) {
		this.hc = hc;
	}

	public String getPollutionStatus() {
		return pollutionStatus;
	}

	public void setPollutionStatus(String pollutionStatus) {
		this.pollutionStatus = pollutionStatus;
	}
	
	

}
