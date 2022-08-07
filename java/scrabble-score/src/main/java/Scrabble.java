import java.util.HashMap;

class Scrabble {

    private String word;

    private HashMap<String, Integer> scores = new HashMap<String, Integer>();

    Scrabble(String word) {
        this.word = word.toUpperCase();

        scores.put("AEIOULNRST", 1);
        scores.put("DG", 2);
        scores.put("BCMP", 3);
        scores.put("FHVWY", 4);
        scores.put("K", 5);
        scores.put("JX", 8);
        scores.put("QZ", 10);
    }

    private boolean isFound(char c, String s) {
        return s.indexOf(c) >= 0;
    }

    int getScore() {
        char c;
        int totalScore = 0;
		
		for (int i = 0; i < word.length(); i++) {
			c = word.charAt(i);
        
			for ( HashMap.Entry<String, Integer> e : scores.entrySet() ) {
				if ( isFound(c, e.getKey()) ) {
					totalScore += e.getValue();
				}
			}
		}

        return totalScore;
    }
}
