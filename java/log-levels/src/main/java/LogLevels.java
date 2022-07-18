public class LogLevels {
    
    public static String message(String logLine) {
        return logLine.split(": ")[1].trim();
    }

    public static String logLevel(String logLine) {
        String t = logLine.split(": ")[0].trim();
        return t.substring(1, t.length() - 1).toLowerCase();
    }

    public static String reformat(String logLine) {
        return String.format("%s (%s)", message(logLine), logLevel(logLine));
    }
}
