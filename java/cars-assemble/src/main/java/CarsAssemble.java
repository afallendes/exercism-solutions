public class CarsAssemble {

    private final int carsPerDay = 221;

    private double successRate(int speed) {
        if (speed == 0) {
            return 0;
        } else if (speed <= 4) {
            return 1.00;
        } else if (speed <= 8) {
            return 0.90;
        } else if (speed == 9) {
            return 0.80;
        } else {
            return 0.77;
        }
    }

    public double productionRatePerHour(int speed) {
        return carsPerDay * speed * successRate(speed);
    }

    public int workingItemsPerMinute(int speed) {
        return (int)Math.floor(productionRatePerHour(speed) / 60);
    }
}
