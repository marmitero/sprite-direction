"""P3 checks: actual independently composited pixel layers in eight directions."""
import json
import tempfile
import unittest
from pathlib import Path
from PIL import Image
from tools.generate_p3_pilot import DIRECTIONS, LAYERS, draw_layer, generate
from tools.sprite_pipeline import validate

class P3PilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp=tempfile.TemporaryDirectory()
        cls.root=Path(cls.temp.name)
        cls.record=generate(cls.root)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_layers_and_8_directions(self):
        self.assertEqual(self.record["direction_order"],list(DIRECTIONS))
        self.assertEqual(len(LAYERS),7)
        for layer in LAYERS:
            b=self.record["builds"][layer]
            self.assertEqual(b["frames"],128)
            self.assertEqual(b["status"],"PASS")
            target=self.root/"assets"/"characters"/"classes"/"shared_humanoid"/layer
            result=validate(target, "shared_humanoid_"+layer)
            self.assertEqual(result["animations"],16)

    def test_each_layer_is_independent_rgba_and_aligned(self):
        for direction in DIRECTIONS:
            for animation in ("idle","walk"):
                for i in range(8):
                    for layer in LAYERS:
                        image=draw_layer(layer,direction,animation,i)
                        self.assertEqual(image.mode,"RGBA")
                        self.assertEqual(image.size,(64,72))
                        self.assertIsNotNone(image.getchannel("A").getbbox(),
                                             (layer,direction,animation,i))

    def test_walk_poses_change_without_changing_world_origin(self):
        for direction in DIRECTIONS:
            images=[draw_layer("body",direction,"walk",i).tobytes() for i in range(8)]
            self.assertGreater(len(set(images)),2)
        base=self.root/"assets"/"characters"/"classes"/"shared_humanoid"
        for layer in LAYERS:
            meta=json.loads((base/layer/f"shared_humanoid_{layer}.json").read_text())
            self.assertEqual({(x["pivot"]["x"],x["pivot"]["y"]) for x in meta["frames"]},{(32,71)})

    def test_visual_previews_generated(self):
        folder=self.root/"assets"/"characters"/"classes"/"shared_humanoid"
        with Image.open(folder/"p3_pilot_contact_sheet.png") as img:
            self.assertEqual(img.size,(1536,432))
        with Image.open(folder/"p3_walk_SE_equipped.gif") as gif:
            self.assertEqual(gif.n_frames,8)

if __name__=="__main__":
    unittest.main()
