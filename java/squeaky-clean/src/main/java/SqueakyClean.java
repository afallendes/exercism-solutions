import java.util.regex.Pattern;

class SqueakyClean {

    static String clean(String identifier) {
        
        return Pattern
            .compile("-(.)") // capture first char after hyphen
            .matcher(
                identifier
                    .replaceAll("\\p{IsControl}", "CTRL")
                    .replaceAll("\\p{IsWhite_Space}", "_")
                    .replaceAll("[\\P{IsL}&&[^-_]]", "") // remove non-letters but keep '_' & '-'
                    .replaceAll("[\\p{InGreek}&&[^\\p{Lu}]]", "") // remove lowercase Greek letters
            )
            .replaceAll(m -> m.group(1).toUpperCase()); // replace match with uppercase first char after hyphen
    }
}
