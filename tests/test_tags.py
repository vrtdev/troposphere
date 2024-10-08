import unittest

from troposphere import If, Sub, Tag, Tags
from troposphere.autoscaling import Tags as ASTags


class TestTags(unittest.TestCase):
    def test_TagAddition(self):
        tags = Tags(foo="foo")
        tags += Tags(bar="bar")
        tags = tags + Tags(baz="baz")
        result = [
            {"Value": "foo", "Key": "foo"},
            {"Value": "bar", "Key": "bar"},
            {"Value": "baz", "Key": "baz"},
        ]
        self.assertEqual(tags.to_dict(), result)

    def test_TagConditional(self):
        tags = Tags(
            {"foo": "foo"}, If("MyCondition", Tag("bar", "bar"), Tag("baz", "baz"))
        )
        result = [
            {
                "Fn::If": [
                    "MyCondition",
                    {"Key": "bar", "Value": "bar"},
                    {"Key": "baz", "Value": "baz"},
                ]
            },
            {"Value": "foo", "Key": "foo"},
        ]
        self.assertEqual(tags.to_dict(), result)

    def test_ASTagAddition(self):
        tags = ASTags(foo=("fooval", True))
        tags += ASTags(bar=("barval", False))
        tags = tags + ASTags(baz="bazval")
        result = [
            {"Value": "fooval", "Key": "foo", "PropagateAtLaunch": True},
            {"Value": "barval", "Key": "bar", "PropagateAtLaunch": False},
            {"Value": "bazval", "Key": "baz", "PropagateAtLaunch": True},
        ]
        self.assertEqual(tags.to_dict(), result)

    def test_Unsortable(self):
        result = [{"Key": {"Fn::Sub": "somestring"}, "Value": "val"}]
        tags = Tags({Sub("somestring"): "val"})
        self.assertEqual(tags.to_dict(), result)

    def test_Formats(self):
        result = [
            {"Value": "bar", "Key": "bar"},
            {"Value": "baz", "Key": "baz"},
            {"Value": "foo", "Key": "foo"},
        ]
        tags = Tags(bar="bar", baz="baz", foo="foo")
        self.assertEqual(tags.to_dict(), result)
        tags = Tags({"bar": "bar", "baz": "baz", "foo": "foo"})
        self.assertEqual(tags.to_dict(), result)
        tags = Tags(**{"bar": "bar", "baz": "baz", "foo": "foo"})
        self.assertEqual(tags.to_dict(), result)
        result = [{"Key": "test-tag", "Value": "123456"}]
        tags = Tags({"test-tag": "123456"})
        self.assertEqual(tags.to_dict(), result)

        with self.assertRaises(TypeError):
            Tags(1)
        with self.assertRaises(TypeError):
            Tags("tag")
        with self.assertRaises(TypeError):
            Tags("key", "value")
        with self.assertRaises(TypeError):
            Tags({}, "key", "value")

    def test_json_tags(self):
        from troposphere.batch import ContainerProperties, JobDefinition

        JobDefinition(
            "myjobdef",
            Type="container",
            ContainerProperties=ContainerProperties(
                Image="image",
                Vcpus=2,
                Memory=2000,
                Command=["echo", "foobar"],
            ),
            Tags={"foo": "bar"},
        )

        with self.assertRaises(TypeError):
            JobDefinition(
                "myjobdef",
                Type="container",
                ContainerProperties=ContainerProperties(
                    Image="image",
                    Vcpus=2,
                    Memory=2000,
                    Command=["echo", "foobar"],
                ),
                Tags=Tags({"foo": "bar"}),
            )

        with self.assertRaises(TypeError):
            JobDefinition(
                "myjobdef",
                Type="container",
                ContainerProperties=ContainerProperties(
                    Image="image",
                    Vcpus=2,
                    Memory=2000,
                    Command=["echo", "foobar"],
                ),
                Tags="string",
            )


if __name__ == "__main__":
    unittest.main()
