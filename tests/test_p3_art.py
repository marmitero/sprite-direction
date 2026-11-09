import tempfile
import unittest
from pathlib import Path
from PIL import Image
from tools.import_p3_art import import_art, import_equipped_walk_se, COL_TO_DIR
from tools.sprite_pipeline import validate

class P3IllustratedArtTests(unittest.TestCase):
    def test_authored_source_imports_eight_distinct_views(self):
        source=Path("assets/characters/classes/shared_humanoid_art_v2/idle_8_directions.png")
        self.assertTrue(source.is_file())
        with tempfile.TemporaryDirectory() as tmp:
            output=Path(tmp)
            result=import_art(source,output)
            self.assertEqual(result["frame_count"],16)
            self.assertEqual(len(set(result["runtime_direction_order"])),8)
            check=validate(output,"shared_humanoid_art_v2")
            self.assertEqual(check["frames"],16)
            self.assertEqual(check["animations"],16)
            self.assertFalse(result["p4_authorized"])
            self.assertIn("full walk animation",result["uncompleted_components"])
    def test_equipped_walk_se_has_eight_illustrated_frames_and_preview(self):
        art=Path("assets/characters/classes/shared_humanoid_art_v2/walk_SE_8_frame_art_reference.png")
        self.assertTrue(art.is_file())
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            record=import_equipped_walk_se(art,root)
            self.assertEqual(record["frames"],8)
            self.assertEqual(validate(root,"humanoid_equipped_walk_se_reference")["frames"],8)
            self.assertTrue((root/"humanoid_equipped_walk_se_reference_walk_SE.gif").is_file())

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
