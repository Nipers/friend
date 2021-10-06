import java.util.ArrayList;

public class Employees {

    private ArrayList<Employee> employees;
    public Employees() {
        employees = new ArrayList<Employee>();
        employees.add(new Employee("Thomas Muller", "thomas.muller@uts.com", "99991111", "Full-Time", "3 Byern St. Sydney 2001", "888-888", 40, 35));
        employees.add(new Employee("Alice Stefan", "alice.stefan@uts.com", "88881111", "Part-Time", "24 Pitt St. Sydney 2001", "777-123", 20, 29));
        employees.add(new Employee("Lucy Lu", "lucy.lu@uts.com", "98981100", "Casual", "11 Hunter St. Sydney 2100", "111-154", 20, 45));
        employees.add(new Employee("Andreas Brehme", "andreas.b@uts.com", "90001222", "Full-Time", "91 Sussex St. Sydney 2100", "172-288", 40, 33));
        employees.add(new Employee("Ruddy Voller", "ruddy.v@uts.com", "98980000", "Full-Time", "15 Stan St. Sydney 2100", "155-154", 40, 80));
        employees.add(new Employee("Monica Shwarz", "monica.s@uts.com", "92241188", "Casual", "155 Jones St. Sydney 2001", "110-194", 8, 20));
    }
    public void ToString() {
        for (int i = 0; i < employees.size(); i++) {
            System.out.println(employees.get(i).Tostring());
        }
        return;
    }
    
    public static void main(String[] args) {
        Employees e = new Employees();
        e.ToString();
        return;
    }

    
}
