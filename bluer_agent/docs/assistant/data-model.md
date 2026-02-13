# assistant: data-model

[Project](../../assistant/classes/project/one.py)

```python
class Project:
    self.object_name: str
    self.subject: str
    self.metadata: Dict[str, Any]
    self.list_of_requirements: List[Requirement]
```

[Requirement, Step](../../assistant/classes/requirement.py)

```python
class Requirement:
    self.question: str = question
    self.list_of_step: List[Step]
```

```python
class Step:
    self.id: str
    self.content: str
    self.list_of_requirements: List[Requirement]
```

