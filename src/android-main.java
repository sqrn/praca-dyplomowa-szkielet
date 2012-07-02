public class Main extends Activity implements OnClickListener{
    private String user_email;
    private String user_password;
    private String serv_addr;
    private SharedPreferences preferences;
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        View loginButton = findViewById(R.id.login_button);
        loginButton.setOnClickListener(this);
    }
    private void loadPreferences() {
        preferences = getSharedPreferences("pl.wit.edu.preferences", 
            MODE_PRIVATE);
        user_email = preferences.getString("preferences_account_name", "");
        user_password = preferences.getString("preferences_password", "");
        serv_addr = preferences.getString("preferences_server_address", "");
    }
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        super.onCreateOptionsMenu(menu);
        MenuInflater menuInflater = getMenuInflater();
        menuInflater.inflate(R.menu.menu, menu);
        return true;
    }
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        switch(item.getItemId()) {
        case R.id.menu_preferences:
            startActivity(new Intent(this, MyPreferences.class));
            return true;
        case R.id.menu_quit:
            System.exit(0);
            break;
        }
        return false;
    }
    @Override
    public void onClick(View v) {
        switch(v.getId()) {
        case R.id.login_button:
            loadPreferences();
            if(user_email == "" || user_password == "") {
                Toast.makeText(this, "Nie można zalogować", 
                    Toast.LENGTH_SHORT).show();
                startActivity(new Intent(this, MyPreferences.class));
            } else {
                User user = new User(user_email, user_password);
                user.setServAddr(serv_addr);
                Toast.makeText(this, "Loguję jako: "+user_email , 
                    Toast.LENGTH_SHORT).show();
                try {
                    user.tryLogin();
                    startActivity(
                        new Intent(this, Geolocation.class)
                    );  
                }
                catch (IOException e) {
                    Toast.makeText(this, 
                        "Wystąpił problem z połączeniem", 
                        Toast.LENGTH_LONG).show();
                }
            }
            break;
        }
    }
}
