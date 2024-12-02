activate:
    . venv/bin/activate

test: activate
    pytest -s

test_k expr: activate
    find . | entr -ccs 'pytest -s -k {{ expr }}'

run day part: activate
    python run.py {{ day }} {{ part }}
