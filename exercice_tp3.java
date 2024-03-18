public class exercice_tp3 {
    class exceptionNegatif extends Exception {
        private int val;

        public exceptionNegatif(int val) {
            this.val = val;
        }

        public string toString() {
            return val + " est negative";
        }
    }

    public class fact {
        public static int calcul(int n) {
            int f = 1;
            for (int i = 2; i <= n; i++) {
                f = f * i;
            }
            return f;
        }

        public static void main(string[] args) {
            int x = Integer.parseInt(args[0]);
            System.out.println(x + "!= " + calcul(x));
        }
    }
}