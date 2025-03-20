package Projects;
import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.InvalidElementStateException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import java.lang.String;
public class Activity2 {

    public static void main(String[] args) {

        WebDriverManager.firefoxdriver().setup();
        // Create a new instance of the Firefox driver
        WebDriver driver = new FirefoxDriver();
        driver.get("https://alchemy.hguy.co/lms");

        String text1 = driver.findElement(By.tagName("h1")).getText();

        if (text1.equals("Learn from Industry Experts"))
        {
            System.out.println("True");


        }
        else
        {
            System.out.println("False");
        }
        driver.quit();


    }

}
