import win32com.client
import pythoncom

def vytvor_zakladni_dwg(nazev_souboru):
    try:
        # Inicializace COM objektu
        acad = win32com.client.Dispatch("AutoCAD.Application")
        
        # Vytvoření nového dokumentu
        doc = acad.Documents.Add()
        
        # Získání modelového prostoru
        mspace = doc.ModelSpace
        
        # Přidání základního textu
        text = mspace.AddText("Základní výkres", win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (0, 0, 0)), 10)
        
        # Přidání základní čáry
        line = mspace.AddLine(win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (0, 0, 0)),
                              win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (100, 100, 0)))
        
        # Přidání základního kruhu
        circle = mspace.AddCircle(win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (50, 50, 0)), 25)
        
        # Uložení souboru jako DWG
        doc.SaveAs(nazev_souboru)
        
        print(f"DWG soubor '{nazev_souboru}' byl úspěšně vytvořen.")
    
    except Exception as e:
        print(f"Došlo k chybě při vytváření DWG souboru: {str(e)}")
    
    finally:
        # Zavření dokumentu a ukončení AutoCADu
        if 'doc' in locals():
            doc.Close(False)
        if 'acad' in locals():
            acad.Quit()

if __name__ == "__main__":
    vytvor_zakladni_dwg(f"zakladni_vykres.dwg")