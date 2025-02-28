import unittest
from student_info import find_ID, find_name, StudentInfoError

class TestStudentInfo(unittest.TestCase):

    def setUp(self):
        self.students = {
            "Aaryn": "aaminyard582",
            "Goku":  "gthompson764",
            "Vegeta": "vgriffin931",
            "Luffy":  "ljohnson427",
            "Zoro":   "zcarter358",
            "Nami":   "nroberts639",
            "Sanji":  "sallen823",
            "Chopper": "cwhite234",
            "Robin":  "rgreen567",
            "Franky": "fclark890",
            "Brook":  "bmartin123",
            "Usopp":  "ujackson456",
            "Jinbe":  "jlewis789",
            "Shanks": "swalker012",
        }

    def test_find_ID_success(self):
        self.assertEqual(find_ID("Goku", self.students), "gthompson764")

    def test_find_ID_failure(self):
        with self.assertRaises(StudentInfoError):
            find_ID("Naruto", self.students)

    def test_find_name_success(self):
        self.assertEqual(find_name("ljohnson427", self.students), "Luffy")

    def test_find_name_failure(self):
        with self.assertRaises(StudentInfoError):
            find_name("unknown_id", self.students)

if __name__ == "__main__":
    unittest.main()