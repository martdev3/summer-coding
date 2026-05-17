from todo import add_task, complete_task, delete_task, save_tasks, load_tasks

def test_add_task_appends_new_task():
    tasks = []

    add_task(tasks,'buy milk')

    assert len(tasks) == 1
    assert tasks[0]['text'] == 'buy milk'
    assert tasks[0]['done'] == False
    assert tasks[0]['id'] == 1

def test_add_task_rejects_empty_text():
    tasks = []
    add_task(tasks,'')
    assert len(tasks) == 0

def test_add_task_rejects_whitespace_only_text():
    tasks = []
    add_task(tasks, ' ')
    assert len(tasks) == 0

def test_add_task_assigns_sequential_ids():
    tasks = []
    add_task(tasks,'buy milk')
    add_task(tasks,'buy eggs')
    add_task(tasks, 'but beef')

    assert tasks[0]['id'] == 1
    assert tasks[1]['id'] == 2
    assert tasks[2]['id'] == 3

def test_complete_task_marks_existing_task_done():
    tasks = []
    add_task(tasks,'buy milk')
    complete_task(tasks, 1)
    assert tasks[0]['done'] == True

def test_complete_task_with_missing_id_does_not_crash():
    tasks = []
    complete_task(tasks,99)

def test_delete_task_removres_existing_task():
    tasks = []
    add_task(tasks, 'buy milk')
    add_task(tasks, 'buy eggs')
    delete_task(tasks, 1)
    assert len(tasks) == 1
    for task in tasks:
        assert task['text'] != 'buy milk'

def test_save_then_load_round_trip(tmp_path):
    test_file = tmp_path / 'tasks.json'
    
    original = [
        {'id': 1, 'text': 'test1', 'done': False},
        {'id': 2, 'text': 'test2', 'done': False}
        ]
    save_tasks(str(test_file), original)
    loaded = load_tasks(str(test_file))

    assert loaded == original

def test_load_tasks_returns_empty_list_when_file_missing(tmp_path):
    missing = tmp_path / 'does_not_exist.json'
    result = load_tasks(str(missing))
    assert result == []

