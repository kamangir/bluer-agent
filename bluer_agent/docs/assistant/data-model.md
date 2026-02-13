# assistant: data-model

[Conversation](../../assistant/classes/conversation/one.py)

```python
class Conversation:
    self.object_name: str
    self.subject: str
    self.metadata: Dict[str, Any]
    self.list_of_interactions: List[Interaction]
```

[Interaction, Reply](../../assistant/classes/interaction.py)

```python
class Interaction:
    self.question: str = question
    self.list_of_replies: List[Reply]
```

```python
class Reply:
    self.id: str
    self.content: str
    self.list_of_interactions: List[Interaction]
```

