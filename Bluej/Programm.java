
import sum.kern.*;

public class Programm
{
    // Objekte
    Bildschirm derBildschirm;
    Stift meinStift;
    Figur dreieck;

    // Konstruktor
    public Programm()
    {
        derBildschirm = new Bildschirm();
        meinStift = new Stift();
        dreieck = new Dreieck(derBildschirm, meinStift);
    }

    // Dienste
    public void fuehreAus()
    {
        dreieck.draw(50);      
    }
    public void aufraeumen()
    {
        meinStift.gibFrei();
        derBildschirm.gibFrei();
    }
}