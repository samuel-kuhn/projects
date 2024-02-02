import sum.kern.*;

public class Figur
{
    // Bezugsobjekte
    Stift kenntStift;
    Bildschirm kenntBildschirm;
    // Attribute

    // Konstruktor
    public Figur(Bildschirm pBildschirm, Stift pStift)
    {
        kenntStift = pStift;
        kenntBildschirm = pBildschirm;
    }

    // Dienste 
    public void draw(){}
    public void draw(int size){}
}
