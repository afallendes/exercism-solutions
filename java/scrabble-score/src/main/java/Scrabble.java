class Scrabble {

    private String word;

    Scrabble(String word) {
        this.word = word.toUpperCase();
    }

    private boolean isFound(char c, String s) {
        return s.indexOf(c) >= 0;
    }

    int getScore() {
        char c;
        int totalScore = 0;
        
        for (int i = 0; i < word.length(); i++) {
            c = word.charAt(i);
            if ( isFound(c, "AEIOULNRST") ) {
                totalScore += 1;
            } else if ( isFound(c, "DG") ) {
                totalScore += 2;
            } else if ( isFound(c, "BCMP") ) {
                totalScore += 3;
            } else if ( isFound(c, "FHVWY") ) {
                totalScore += 4;
            } else if ( 'K' == c ) {
                totalScore += 5;
            } else if ( isFound(c, "JX") ) {
                totalScore += 8;
            } else if ( isFound(c, "QZ") ) {
                totalScore += 10;
            }
        }

        return totalScore;
    }

}
