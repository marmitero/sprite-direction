import tempfile,unittest
from pathlib import Path
from PIL import Image
from tools.import_approved_p3_reference import chroma_rgba
class ApprovedReferenceTests(unittest.TestCase):
 def test_chroma_removes_magenta_but_preserves_red_scarf_and_dark_hair(self):
  x=Image.new("RGB",(3,1),(255,0,255))
  x.putpixel((1,0),(150,35,48))
  x.putpixel((2,0),(50,42,52))
  y=chroma_rgba(x)
  self.assertEqual(y.getpixel((0,0))[3],0)
  self.assertEqual(y.getpixel((1,0)),(150,35,48,255))
  self.assertEqual(y.getpixel((2,0)),(50,42,52,255))
if __name__=="__main__":unittest.main()
