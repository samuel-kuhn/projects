import sum.kern.*;

public class Dreieck extends Polygon
{
    // Bezugsobjekte
    
    // Attribute

    // Konstruktor
    public Dreieck(Bildschirm pBildschirm, Stift pStift)
    {
        super(pBildschirm, pStift);
        
    }

    // Dienste
    @Override
    public void draw(int size)
    {
        kenntStift.bewegeBis(200,100);
        kenntStift.runter();
        for (int i = 0; i < 3; i++)
        {
            kenntStift.bewegeUm(size);
            kenntStift.dreheUm(120);
        }
        kenntStift.hoch();
    }

}
