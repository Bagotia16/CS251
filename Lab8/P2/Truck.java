

public class Truck extends Vehicle{

	public Truck() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Truck(String regNo, String manufacturer, String owner, double co2, double co, double hc,
			String pollutionStatus) {
		super(regNo, manufacturer, owner, co2, co, hc, pollutionStatus);
		// TODO Auto-generated constructor stub
	}

	public void checkPollutionStatus(){
		double co2Level = getCo2();
		double coLevel = getCo();
		double hcLevel = getHc();
		if(co2Level <= 25 && coLevel <= 0.8 && hcLevel <= 1000)
		{
			this.setPollutionStatus("PASS");
		}
		else
		{
			this.setPollutionStatus("FAIL");
		}
	}

}
