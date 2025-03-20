package Projects;
import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import java.lang.String;
import java.util.List;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Activity7 {

    public static void main(String[] args) {

        WebDriverManager.firefoxdriver().setup();
        // Create a new instance of the Firefox driver
        WebDriver driver = new FirefoxDriver();
        driver.get("https://alchemy.hguy.co/lms");
        driver.findElement(By.xpath("//a[contains(text(),'All Courses')]")).click();
        System.out.println(driver.getTitle());
        List<WebElement> elements= driver.findElements(By.xpath("//div[@class='ld-course-list-items row']/*"));



        System.out.println("Number of course :" + elements.size());
        driver.quit();


    }

}
