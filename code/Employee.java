public class Employee {
    private String name;
    private String email;
    private String phone;
    private String address;
    private String TFN;
    private String type; 
    private int hours;
    private double payPerHour;
    private double income;
    private double rate;
    private double net;
    private double deduction;
    private double superannuation;
    private double superRate;
    private Employer employer;
    public Employee(int H, double pph) {
        payPerHour = pph;
        hours = H;
        income = hours * 52 * payPerHour;
        if (income >= 180000) {
            rate = 0.45;
        }
        else if (income >= 120000) {
            rate = 0.37;
        }
        else if (income >= 45000) {
            rate = 0.32;
        }
        else if (income >= 15000) {
            rate = 0.19;
        }
        else {
            rate = 0;
        }
        deduction = income * rate;
        net = income - deduction;
        superRate = 0.09;
        superannuation = income * superRate;
    }
    // public String Tostring() {
    //     return 
    // }
    public String getName() {
        return name;
    }
    public double getWage() {
        return income;
    }
    public double getTax() {
        return deduction;
    }
    public double getNet() {
        return net;
    }
    public double getSuperannuation() {
        return superannuation;
    }
}
