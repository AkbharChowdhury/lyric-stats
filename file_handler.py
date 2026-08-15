class FileHandler:
    @staticmethod
    def read_file(file_path: str) -> str:
        with open(file_path) as f:
            lyrics = f.read()
        return lyrics