import java.util.stream.IntStream;

class DifferenceOfSquaresCalculator {

    int computeSquareOfSumTo(int input) {
        int s = IntStream.rangeClosed(1, input).sum();
        return s * s;
    }

    int computeSumOfSquaresTo(int input) {
        return IntStream
            .rangeClosed(1, input)
            .map(i -> i * i)
            .sum();
    }

    int computeDifferenceOfSquares(int input) {
        return computeSquareOfSumTo(input) - computeSumOfSquaresTo(input);
    }

}
