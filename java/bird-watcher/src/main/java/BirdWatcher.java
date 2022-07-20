
class BirdWatcher {
    private final int[] birdsPerDay;

    public BirdWatcher(int[] birdsPerDay) {
        this.birdsPerDay = birdsPerDay.clone();
    }

    public int[] getLastWeek() {
        int[] lastWeek = {0, 2, 5, 3, 7, 8, 4};
        return lastWeek;
    }

    public int getToday() {
        return birdsPerDay.length > 0 ? birdsPerDay[birdsPerDay.length - 1] : 0;
    }

    public void incrementTodaysCount() {
        birdsPerDay[birdsPerDay.length - 1]++;
    }

    public boolean hasDayWithoutBirds() {
        for (int i : birdsPerDay) {
            if (i == 0) {
                return true;
            }
        }
        return false;
    }

    public int getCountForFirstDays(int numberOfDays) {
        int sumTotal = 0;

        for (int i = 0; i < birdsPerDay.length; i++) {
            if (i <= numberOfDays - 1) {
                sumTotal += birdsPerDay[i];
            }
        };
        
        return sumTotal;
    }

    public int getBusyDays() {
        int countBusyDays = 0;

        for (int i : birdsPerDay) {
            if (i >= 5) {
                countBusyDays++;
            }
        }

        return countBusyDays;
    }
}
