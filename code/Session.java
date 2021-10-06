public class Session {
    private Employers employers;
    
    public Session() {
        String.valueOf(employers);
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
        System.out.print("Incorrect employer details!");
        return false;
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
    public static void main(String[] args) {
        while (true) {
            MainMenu();
            char choice = Utils.choice("Command (L/X)");
            if (choice == 'L') {
                login();
            }
            else if (choice == 'X') {
                Exit();
                return;
            }
        }
    }
}
