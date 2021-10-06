public class Session {
    private Employers employers;
    
    public Session() {
        employers = new Employers();
    };
    private static void MainMenu() {
        System.out.println("STP Payroll Management System:");
        System.out.println("L- Login");
        System.out.println("X- Exit");
    };
    private static void Exit() {
        System.out.println("");
        System.out.print("Session Terminated!");
    };
    private boolean login() {
        String email = Utils.string("Email");
        String password = Utils.string("Password");
        if (employers.check(email, password)) {
            return true;
        }        
        System.out.println("Incorrect employer details!");
        return false;
    }    
    private static void employerMenu() {
        System.out.println("Employer Menu: ");
        System.out.println("C- Add Employee");
        System.out.println("R- View Employee");
        System.out.println("U- Update Employee");
        System.out.println("D- Delete Employee");
        System.out.println("V- View Employees");
        System.out.println("S- STP Menu");
        System.out.println("X- Logout");

    }
    private static void STPMenu() {
        System.out.print("STP Menu: ");
        System.out.print("F- Find PAYG Report");
        System.out.print("V- View STP Report");
        System.out.print("A- Archive STP Report");
        System.out.print("R- Retrieve STP Report");
        System.out.print("S- Show STP Log");
        System.out.print("X- Close");

    }
    private void process() {
        MainMenu();
        while (true) {
            char choice = Utils.choice("Command (L/X)");
            if (choice == 'L') {
                if (login()) {
                    employerMenu();
                    choice = Utils.choice("Session Admin: "+" - Menu Commands (C/R/U/D/V/S/X)");
                }
            }
            else if (choice == 'X') {
                Exit();
                return;
            }
        }

    }
    public static void main(String[] args) {
        Session session = new Session();
        session.process();
    }
}
