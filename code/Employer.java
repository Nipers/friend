public class Employer {

    private String name;
    private String email;
    private String password;
    private Employees employees;
    private STP stp;

    public Employer(String Name, String Email, String Password, Employees Employees) {
        this.name = Name;
        email = Email;
        password = Password;
        employees = Employees;
    }

    public String ToString() {
        return name + "|" + email + "|" + password + "|" + employees + "|"+ stp;
    }
    
   
}
