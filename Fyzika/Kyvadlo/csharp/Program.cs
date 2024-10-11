using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Vítejte v programu pro výpočet jízdy vlaku");

        // Vstupní údaje
        Console.Write("Zadejte vzdálenost v kilometrech: ");
        double vzdalenost = double.Parse(Console.ReadLine());

        Console.Write("Zadejte maximální rychlost vlaku v km/h: ");
        double maxRychlost = double.Parse(Console.ReadLine());

        Console.Write("Zadejte počet zastávek: ");
        int pocetZastavek = int.Parse(Console.ReadLine());

        Console.Write("Zadejte průměrnou dobu zastávky v minutách: ");
        double dobaZastavky = double.Parse(Console.ReadLine());

        Console.Write("Zadejte spotřebu paliva v litrech na 100 km: ");
        double spotrebaPaliva = double.Parse(Console.ReadLine());

        // Výpočty
        double casJizdyHodiny = vzdalenost / maxRychlost;
        double casZastavekHodiny = (pocetZastavek * dobaZastavky) / 60;
        double celkovyCasHodiny = casJizdyHodiny + casZastavekHodiny;

        double prumernaRychlost = vzdalenost / celkovyCasHodiny;

        double celkovaSpotreba = (spotrebaPaliva / 100) * vzdalenost;

        // Výstup
        Console.WriteLine("\nVýsledky výpočtu:");
        Console.WriteLine($"Celkový čas jízdy: {celkovyCasHodiny:F2} hodin");
        Console.WriteLine($"Průměrná rychlost: {prumernaRychlost:F2} km/h");
        Console.WriteLine($"Celková spotřeba paliva: {celkovaSpotreba:F2} litrů");

        Console.ReadLine(); // Čekání na stisk klávesy před ukončením
    }
}