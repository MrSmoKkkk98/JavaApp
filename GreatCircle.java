public class GreatCircle {
    public static void main(String[] args) {
        double x1 = Double.parseDouble(args[0]);
        double y1 = Double.parseDouble(args[1]);
        double x2 = Double.parseDouble(args[2]);
        double y2 = Double.parseDouble(args[3]);
        double x1InRad = Math.toRadians(x1);
        double y1InRad = Math.toRadians(y1);
        double x2InRad = Math.toRadians(x2);
        double y2InRad = Math.toRadians(y2);
        double sinX = Math.sin((x2InRad - x1InRad) / 2);
        double sinY = Math.sin((y2InRad - y1InRad) / 2);
        double sinXSquared = Math.pow(sinX, 2);
        double sinYSquared = Math.pow(sinY, 2);
        double formulaInBrackets = Math.sqrt(sinXSquared + Math.cos(x1InRad) * Math.cos(x2InRad) * sinYSquared);
        double arcSinFormula = Math.asin(formulaInBrackets);
        double r = 6371.0;
        double fullFormula = 2 * r * arcSinFormula;
        System.out.println(fullFormula + " kilometers");
    }
}