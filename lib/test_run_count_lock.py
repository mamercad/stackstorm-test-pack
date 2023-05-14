import os
from run_count_lock import RunCountLock

TMP_FILE = "/tmp/test_run_count_lock"

def test_create_file():
    if os.path.exists(TMP_FILE):
        os.unlink(TMP_FILE)
    rcl = RunCountLock(lock_path=TMP_FILE)
    assert rcl.count() == "0"

def test_increment():
    rcl = RunCountLock(lock_path=TMP_FILE)
    assert rcl.count() == "0"
    rcl.increment()
    assert rcl.count() == "1"
    rcl.increment()
    rcl.increment()
    assert rcl.count() == "3"
