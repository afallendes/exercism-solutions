public class SalaryCalculator {
    public double multiplierPerDaysSkipped(int daysSkipped) {
        return daysSkipped > 5 ? .85 : 1;
    }

    public int multiplierPerProductsSold(int productsSold) {
        return productsSold > 20 ? 13 : 10;
    }

    public double bonusForProductSold(int productsSold) {
        return productsSold * multiplierPerProductsSold(productsSold);
    }

    public double finalSalary(int daysSkipped, int productsSold) {
        double salary = 1000 * multiplierPerDaysSkipped(daysSkipped);
        double bonus = bonusForProductSold(productsSold);
        return salary + bonus > 2000 ? 2000 : salary + bonus;        
    } 
}
