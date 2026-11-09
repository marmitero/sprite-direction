"""P2 smoke/integrity tests. Uses generated geometric pixels ONLY for tool testing.

These are not production art and are not committed as assets.
"""
import json
import tempfile
import unittest
from pathlib import Path
from PIL import Image

from tools.sprite_pipeline import build, validate, DIRECTIONS


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.src = self.base / "frames"
        self.dst = self.base / "build"

    def frame(self, animation, direction, i, rgba=(190, 70, 30, 255),
              size=(64, 64), box=(25, 13, 32, 37)):
        folder = self.src / animation / direction
        folder.mkdir(parents=True, exist_ok=True)
        img = Image.new("RGBA", size, (0, 0, 0, 0))
        img.paste(rgba, box)
        img.save(folder / f"{i:03d}.png")

    def test_build_trim_and_validate(self):
        for direction in DIRECTIONS:
            for i in range(3):
                self.frame("idle", direction, i)
        result = build(self.src, self.dst, "goblin_test", atlas_size=128, padding=2)
        self.assertEqual(len(result["frames"]), 24)
        self.assertGreaterEqual(len(result["atlases"]), 2)
        self.assertEqual(validate(self.dst, "goblin_test")["status"], "PASS")
        frame = next(f for f in result["frames"] if f["id"] == "idle/N/000")
        self.assertEqual(frame["sprite_source_size"],
                         {"x": 25, "y": 13, "w": 7, "h": 24})
        self.assertEqual(frame["pivot"], {"x": 32, "y": 63})
        self.assertEqual(frame["duration_ms"], 83)

    def test_reject_non_rgba(self):
        folder = self.src / "walk" / "N"
        folder.mkdir(parents=True)
        Image.new("RGB", (16, 16), (0, 0, 0)).save(folder / "000.png")
        with self.assertRaisesRegex(ValueError, "RGBA"):
            build(self.src, self.dst, "invalid")

    def test_reject_missing_index(self):
        self.frame("idle", "N", 0)
        self.frame("idle", "N", 2)
        with self.assertRaisesRegex(ValueError, "consecutive"):
            build(self.src, self.dst, "broken")

    def test_empty_frame_and_gif(self):
        folder = self.src / "idle" / "fixed"
        folder.mkdir(parents=True)
        Image.new("RGBA", (64, 64), (0, 0, 0, 0)).save(folder / "000.png")
        self.frame("idle", "fixed", 1)
        data = build(self.src, self.dst, "blacksmith_test", make_gif=True)
        self.assertTrue(data["frames"][0]["empty"])
        self.assertTrue((self.dst / "blacksmith_test_idle_fixed.gif").exists())
        self.assertEqual(validate(self.dst, "blacksmith_test")["frames"], 2)

    def test_detect_tampered_atlas(self):
        self.frame("walk", "SE", 0)
        build(self.src, self.dst, "atlas_test")
        atlas = self.dst / "atlas_test_atlas_000.png"
        image = Image.open(atlas)
        image.putpixel((0, 0), (255, 255, 255, 255))
        image.save(atlas)
        with self.assertRaisesRegex(ValueError, "modified atlas"):
            validate(self.dst, "atlas_test")

    def test_reject_input_output_nesting(self):
        self.frame("idle", "N", 0)
        with self.assertRaisesRegex(ValueError, "cannot be"):
            build(self.src, self.src / "output", "invalid")


if __name__ == "__main__":
    unittest.main()
