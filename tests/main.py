from filestore_guagua import FileStore


if __name__ == "__main__":
    fs = FileStore()
    print(fs.get_project_root())
    print(fs.base_dir)
    fs.saveJSON("test", {"name": "guagua"})
    print(fs.readJSON("test"))
    fs.saveData("test.txt", b"hello world")
    print(fs.openData("test.txt"))
    fs.create_json_files(
        ["batch/test1", "batch/test2"],
        [{"name": "guagua1"}, {"name": "guagua2"}],
    )
