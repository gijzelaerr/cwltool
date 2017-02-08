import unittest
import tempfile
import shutil
from os import path, mkdir


recursive_directory_cwl = """
cwlVersion: v1.0
class: CommandLineTool

requirements:
  - class: InlineJavascriptRequirement
  - class: InitialWorkDirRequirement
    listing:
      - entry: $(inputs.input_dir)
        entryname: flagged.ms
        writable: true

baseCommand: "touch"
arguments: ["file_inside_directory"]

inputs:
  input_dir: Directory

outputs:
  input_dir:
    type: Directory
    outputBinding:
      glob: flagged.ms
"""


class TestRecursiveInputDirectory(unittest.TestCase):
    """
    This test will assert if a writable input Directory is actually recursively marked as writable
    """
    def setUp(self):
        self.temppath = tempfile.mkdtemp()
        childdir = path.join(self.temppath, 'child_folder')
        childfile = path.join(self.temppath, 'child_file')
        childchildfile = path.join(childdir, 'childchild_file')
        mkdir(childdir)
        open(childfile, 'a').close()
        open(childchildfile, 'a').close()

    def tearDown(self):
        shutil.rmtree(self.temppath)

    def test_bla(self):
        print(self.temppath)