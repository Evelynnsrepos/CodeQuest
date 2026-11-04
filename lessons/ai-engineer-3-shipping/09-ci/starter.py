import yaml


def check_workflow(text):
    return []


WORKFLOW = """name: tests
on: push
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: echo hi
"""
print(check_workflow(WORKFLOW))
