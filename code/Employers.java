import java.util.ArrayList;

public class Employers {

    private ArrayList<Employer> employers;
    public boolean check(String email, String password) {
        for (int i = 0; i < employers.size(); i++) {
            if (employers.get(i).check(email, password))
                return true;
        }
        return false;
    }
    public Employers() {
        employers = new ArrayList<Employer>();
        employers.add(new Employer("John Smith", "john.smith@uts.com", "super123", new Employees()));
        employers.add(new Employer("Jane Doe", "jave.doe@uts.com", "user222", new Employees()));
    }
}
