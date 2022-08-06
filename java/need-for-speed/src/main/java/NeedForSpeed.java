class NeedForSpeed {
    private int speed;
    private int batteryDrain;
    private int battery = 100;
    private int distance = 0;
    
    public NeedForSpeed(int speed, int batteryDrain) {
        this.speed = speed;
        this.batteryDrain = batteryDrain;
    }

    public boolean batteryDrained() {
        return battery <= 0;
    }

    public int distanceDriven() {
        return distance;
    }

    public void drive() {
        if ( battery > 0 ) {
            distance += speed;
            battery -= batteryDrain;
        }
    }

    public static NeedForSpeed nitro() {
        return new NeedForSpeed(50, 4);
    }
}

class RaceTrack {
    private int distance;
    
    public RaceTrack(int distance) {
        this.distance = distance;
    }

    public boolean tryFinishTrack(NeedForSpeed car) {
        while ( true ) {
            car.drive();

            if ( car.distanceDriven() >= distance ) {
                return true;
            } else if ( car.batteryDrained() ) {
                return false;
            }
        }
    }
}
