package Projects;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.InvalidElementStateException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import java.lang.String;
public class Activity3 {
    public static void main(String[] args) {

        WebDriverManager.firefoxdriver().setup();
        // Create a new instance of the Firefox driver
        WebDriver driver = new FirefoxDriver();
        driver.get("https://alchemy.hguy.co/lms");

        String text1 = driver.findElement(By.cssSelector("h3.uagb-ifb-title")).getText();

        if (text1.equals("Actionable Training")) {
            System.out.println("True");
        }
        else
        {
            System.out.println("False");
        }
        driver.quit();


    }



}
