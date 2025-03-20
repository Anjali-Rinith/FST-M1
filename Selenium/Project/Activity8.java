package Projects;
import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.InvalidElementStateException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import java.lang.String;
import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Activity8 {
    public static void main(String[] args) {

        WebDriverManager.firefoxdriver().setup();
        // Create a new instance of the Firefox driver
        WebDriver driver = new FirefoxDriver();
        driver.get("https://alchemy.hguy.co/lms");

        driver.findElement(By.xpath("//a[contains(text(),'Contact')]")).click();

        driver.findElement(By.xpath("//input[@id='wpforms-8-field_0']")).sendKeys("AkhyaK");

        driver.findElement(By.xpath("//input[@id='wpforms-8-field_1']")).sendKeys("akhykris@in.ibm.com");
        driver.findElement(By.xpath("//input[@id='wpforms-8-field_3']")).sendKeys("FST");

        driver.findElement(By.xpath("//textarea[@id='wpforms-8-field_2']")).sendKeys("none");

        driver.findElement(By.xpath("//button[@id='wpforms-submit-8']")).click();

        String text1 = driver.findElement(By.id("wpforms-confirmation-8")).getText();

        System.out.println(text1);
    }
}
