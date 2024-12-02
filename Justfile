activate:
    . venv/bin/activate

test: activate
    find . | entr -ccs 'pytest -s'

run day part: activate
    python run.py {{ day }} {{ part }}
