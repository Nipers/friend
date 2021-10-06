public class Report {

    private String name;
    private double wages;
    private double tax;
    private double net;
    private double superannuation;

    public String toString() {
        String result = name + String.valueOf(wages) + String.valueOf(tax) + String.valueOf(net) + String.valueOf(superannuation);
        return result;
    };
    public Report(Employee employee) {
        name = employee.getName();
        wages = employee.getWage();
        tax = employee.getTax();
        net = employee.getNet();
        superannuation = employee.getSuperannuation();
    };
    
}
