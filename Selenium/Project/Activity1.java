package Projects;

import dev.failsafe.internal.util.Assert;
import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.InvalidElementStateException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import java.lang.String;


public class Activity1 {

    public static void main(String[] args){

        WebDriverManager.firefoxdriver().setup();
        // Create a new instance of the Firefox driver
        WebDriver driver = new FirefoxDriver();
        driver.get("https://alchemy.hguy.co/lms");
        String homeTitle= driver.getTitle();
        System.out.println(homeTitle);
        if (homeTitle.trim().equals("Alchemy LMS – An LMS Application"))
        {
            System.out.println("true");

        }
        else {
            System.out.println("False");

        }
        driver.quit();

    }
}
