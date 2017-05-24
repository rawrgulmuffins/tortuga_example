"""This is a demo of how it would be possible to add a language method to
turtle that would load translations and create appropriate global objects
(like tortuga) in the language of the intended user.

NOTE: There's some issues with this, such as TurtleStandIn has functions
      instead of methods because we're building a Frankensteinian monster.
      We'll just have to learn how to build better monsters.
"""
from pathlib import Path
import importlib.util
import os

def turtle_creator(name):
    class TurtleStandIn:
        # Pretend like there's many nice methods to override in here.
        pass

        def import_test():
            print("I imported correctly.")

    TurtleStandIn.__name__ = name
    return TurtleStandIn

def load_language(language: str):
    """If the requested language has a translation file
    """
    language_file = language + ".py"
    plugin_path = Path(os.path.realpath(__file__)).parents[0] / "translations" / language_file

    # This section taken from
    # https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
    spec = importlib.util.spec_from_file_location("translation_file", str(plugin_path))
    translation_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(translation_module)

    # Tortuga setup goes here

    hatchling = turtle_creator(translation_module.__module_name__)

    for spanish_name in translation_module._LANGUAGE_IDENTIFIERS.values():
        # We'll need to grab the English name from the real turtle and then
        # grab the method we care about and use that as the value in setattr
        setattr(hatchling, spanish_name, "Put Turtle English Method Here.")

        # NOTE: Potentially we'll have to do some shenanigans to make these
        #       bound methods.

    print(hatchling)

    globals()[hatchling.__name__] = hatchling

    print(tortuga.import_test())
    print(type(tortuga.import_test))
    return translation_module.__language__, translation_module.__module_name__


if __name__ == "__main__":
    print(load_language("spanish"))
