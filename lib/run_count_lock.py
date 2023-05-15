import os
from datetime import datetime


class RunCountLock:
    def __init__(self, lock_path: str) -> None:
        self.now = datetime.now()
        self.lock_path = lock_path

        self.dirname = os.path.dirname(self.lock_path)
        if not os.path.exists(self.dirname):
            os.makedirs(self.dirname, exist_ok=True)

        self.basename = os.path.basename(self.lock_path)

        if not os.path.exists(self.lock_path):
            with open(self.lock_path, "w") as f:
                f.write("0\n")
                f.close()
        else:
            with open(self.lock_path, "r+") as f:
                if not len(f.readlines()):
                    f.write("0\n")
                    f.close()

        self.lock_file = open(self.lock_path, "r+")

    def count(self) -> int:
        self.lock_file.seek(0)
        return self.lock_file.readlines()[-1].strip()

    def increment(self):
        self.lock_file.write(str(int(self.count()) + 1) + "\n")


if __name__ == "__main__":
    rcl = RunCountLock(lock_path="/tmp/run_count_lock")
    print(rcl.count())
    rcl.increment()
    print(rcl.count())
    rcl.increment()
    print(rcl.count())
