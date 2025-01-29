from app.database import *

def test_queue_save():
    create_queue_table()
    clear_data_table("queues")

    expect_queue = queue.Queue()
    expect_queue.put("string data1")
    expect_queue.put("string data2")

    test_queue = queue.Queue()
    test_queue.put("string data1")
    test_queue.put("string data2")

    save_queue_to_db("test_queue", test_queue)

    new_queue = load_queue_from_db("test_queue")

    assert expect_queue.queue == new_queue.queue