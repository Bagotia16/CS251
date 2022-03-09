

public class Car extends Vehicle{

	public Car() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Car(String regNo, String manufacturer, String owner, double co2, double co, double hc,
			String pollutionStatus) {
		super(regNo, manufacturer, owner, co2, co, hc, pollutionStatus);
		// TODO Auto-generated constructor stub
	}
	public void checkPollutionStatus(){
		double co2Level = getCo2();
		double coLevel = getCo();
		double hcLevel = getHc();
		if(co2Level <= 15 && coLevel <= 0.5 && hcLevel <= 750)
		{
			this.setPollutionStatus("PASS");
		}
		else
		{
			this.setPollutionStatus("FAIL");
		}
	}
	

}
