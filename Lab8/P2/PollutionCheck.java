import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class PollutionCheck {
    static ArrayList<Vehicle> vehicles = new ArrayList<>();
    private static int findVehicle(String regNo)
    {
//        System.out.println("Hello");
//        System.out.println(vehicles.get(0).toString());
        for(int i=0;i<vehicles.size();i++)
        {
//            System.out.println("Another Hello");
//            System.out.println(vehicle.getRegNo());
            if(vehicles.get(i).getRegNo().equals(regNo))
            {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) throws FileNotFoundException {
        if(args.length < 3) {
            System.out.println("Error, usage: java PollutionCheck <vehicles-file> <pollution-file> <queries-file>");
            System.exit(1);
        }
        Scanner reader = new Scanner(new FileInputStream(args[0]));

        while(reader.hasNextLine()){
            String data = reader.nextLine();
            String[] dataValues = data.split(", ");
//            System.out.println("1."+dataValues[0]+ " 2."+dataValues[1]+ " 3."+dataValues[2]+" 4."+dataValues[3]);

            if(dataValues[3].equals("Car")){
                Vehicle temp = new Car(dataValues[0],dataValues[1],dataValues[2],0,0,0,"PENDING");
                vehicles.add(temp);

            }
            if(dataValues[3].equals("Truck")) {
                Vehicle temp = new Truck(dataValues[0], dataValues[1], dataValues[2], 0, 0, 0, "PENDING");
                vehicles.add(temp);

            }
        }
//        System.out.println(vehicles);
        reader = new Scanner(new FileInputStream(args[1]));

        while(reader.hasNextLine())
        {
            String data = reader.nextLine();
            String[] dataValues = data.split(", ");
//            System.out.println(vehicles.get(0).toString());
            int temp_index = findVehicle(dataValues[0]);
//            System.out.println(temp.toString());
            if(temp_index!=-1)
            {
                vehicles.get(temp_index).setCo2(Double.parseDouble(dataValues[1]));
                vehicles.get(temp_index).setCo(Double.parseDouble(dataValues[2]));
                vehicles.get(temp_index).setHc(Double.parseDouble(dataValues[3]));
                vehicles.get(temp_index).checkPollutionStatus();
            }
        }

        reader = new Scanner(new FileInputStream(args[2]));

        while(reader.hasNextLine())
        {
            String data = reader.nextLine();
            int temp_index = findVehicle(data);
            if(temp_index!=-1)
            {
                System.out.println(vehicles.get(temp_index).getPollutionStatus());
            }
            else
            {
                System.out.println("NOT REGISTERED");
            }

        }

//        for(Vehicle v: vehicles)
//        {
//            System.out.println(v.getHc());
//        }


//        System.out.println("Hello");
    }



}
