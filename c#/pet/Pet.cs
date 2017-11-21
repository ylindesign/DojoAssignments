namespace pet {
    public class pet {
        public int Happy { get;set; }
        public int Full { get;set; }
        public int Energy { get;set; }
        public int Meals { get;set; }

        public pet() {
            Happy = 20;
            Full = 20;
            Energy = 50;
            Meals = 3;
        }

        // public void Feed(pet pet) {
        //     Current = HttpContext.Session.GetObjectFromJson<pet>("pet");
        // }
    }
}