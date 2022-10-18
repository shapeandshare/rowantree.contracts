import unittest

from src.rowantree.contracts import BaseModel, FeatureDetailType


class TestBaseModel(unittest.TestCase):
    def test_base_model(self):
        class TestModel(BaseModel):
            test_attribute: str
            some_type: FeatureDetailType

        test_dict: dict = {"testAttribute": "testValue", "someType": "A Shadowy Grove"}

        test_model = TestModel.parse_obj(test_dict)
        self.assertEqual(test_model.test_attribute, "testValue")
        self.assertEqual(test_model.some_type, FeatureDetailType.SHADOWY_GROVE)

        self.assertEqual(test_dict, test_model.dict(by_alias=True))


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(TestBaseModel())
