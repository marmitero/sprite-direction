import tempfile
import unittest
from pathlib import Path
from PIL import Image
from tools.import_p3_art import import_art, COL_TO_DIR
from tools.sprite_pipeline import validate

class P3IllustratedArtTests(unittest.TestCase):
    def test_authored_source_imports_eight_distinct_views(self):
        source=Path("assets/characters/classes/shared_humanoid_art_v2/idle_8_directions.png")
        self.assertTrue(source.is_file())
        with tempfile.TemporaryDirectory() as tmp:
            output=Path(tmp)
            result=import_art(source,output)
            self.assertEqual(result["frame_count"],8)
            self.assertEqual(len(set(result["runtime_direction_order"])),8)
            check=validate(output,"shared_humanoid_art_v2")
            self.assertEqual(check["frames"],8)
            self.assertEqual(check["animations"],8)
            self.assertFalse(result["p4_authorized"])
            self.assertIn("walk animation",result["uncompleted_components"])
    def test_art_not_opaque_placeholder(self):
        source=Path("assets/characters/classes/shared_humanoid_art_v2/idle_8_directions.png")
        with Image.open(source) as img:
            self.assertEqual(img.size,(320,52))
            rgba=img.convert("RGBA")
            for i in range(8):
                frame=rgba.crop((i*40,0,(i+1)*40,52))
                alpha=frame.getchannel("A")
                self.assertIsNotNone(alpha.getbbox())
                self.assertEqual(alpha.getextrema()[0],0)
                self.assertGreater(len(frame.getcolors(40*52) or []),10)
if __name__=="__main__":
    unittest.main()
