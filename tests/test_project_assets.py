import csv
import json
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATASETS = (
    PROJECT_ROOT / "atm_islemleri_tr.csv",
    PROJECT_ROOT / "atm_islemleri_tr_1yil.csv",
)
NOTEBOOK = PROJECT_ROOT / "atmproje1.ipynb"

EXPECTED_COLUMNS = {
    "islem_id",
    "zaman_damgasi",
    "musteri_id",
    "atm_id",
    "atm_konumu",
    "tutar",
    "durum",
    "hatali_deneme_sayisi",
    "islem_suresi_sn",
    "onceki_isleme_uzaklik_km",
    "saat",
    "haftanin_gunu",
    "saat_araligi",
    "anomali_mi",
}


class ProjectAssetTests(unittest.TestCase):
    def test_required_files_exist(self):
        for path in (*DATASETS, NOTEBOOK):
            with self.subTest(path=path.name):
                self.assertTrue(path.is_file())
                self.assertGreater(path.stat().st_size, 0)

    def test_dataset_schema_and_row_counts(self):
        for path in DATASETS:
            with self.subTest(path=path.name):
                with path.open("r", encoding="utf-8", newline="") as handle:
                    reader = csv.reader(handle)
                    header = next(reader)
                    row_count = sum(1 for _ in reader)

                self.assertEqual(set(header), EXPECTED_COLUMNS)
                self.assertEqual(len(header), len(EXPECTED_COLUMNS))
                self.assertEqual(row_count, 240_000)

    def test_notebook_structure_and_code_cells(self):
        notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))

        self.assertEqual(notebook.get("nbformat"), 4)
        self.assertGreater(len(notebook.get("cells", [])), 0)

        for index, cell in enumerate(notebook["cells"]):
            if cell.get("cell_type") != "code":
                continue

            source = "".join(cell.get("source", []))
            with self.subTest(cell=index):
                compile(source, f"{NOTEBOOK.name}:cell-{index}", "exec")

    def test_notebook_has_no_stored_error_outputs(self):
        notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
        errors = []

        for index, cell in enumerate(notebook.get("cells", [])):
            for output in cell.get("outputs", []):
                if output.get("output_type") == "error":
                    errors.append(
                        {
                            "cell": index,
                            "name": output.get("ename"),
                            "message": output.get("evalue"),
                        }
                    )

        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
