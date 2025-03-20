package Projects;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.InvalidElementStateException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import java.lang.String;
import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Activity9 {

    public static void main(String[] args){

    WebDriverManager.firefoxdriver().setup();
    // Create a new instance of the Firefox driver
    WebDriver driver = new FirefoxDriver();
    driver.get("https://alchemy.hguy.co/lms");

    driver.findElement(By.xpath("//a[contains(text(),'Account')]")).click();
    System.out.println(driver.getTitle());
    driver.findElement(By.xpath("//a[@class='ld-login ld-login ld-login-text ld-login-button ld-button']")).click();
    driver.findElement(By.id("user_login")).sendKeys("root");
    driver.findElement(By.id("user_pass")).sendKeys("pa$$w0rd");
    driver.findElement(By.id("wp-submit")).click();

    driver.findElement(By.xpath("//a[contains(text(),'All Courses')]")).click();

    System.out.println(driver.getTitle());

        driver.findElement(By.xpath("/html/body/div/div/div/div/main/article/div/section[2]/div[2]/div/div/div/div[2]/article/div[2]/p[2]/a")).click();
        driver.findElement(By.xpath("//div[@id='ld-expand-91']")).click();
        driver.findElement(By.xpath("/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div/a/div[2]")).click();

driver.quit();

    }


}
