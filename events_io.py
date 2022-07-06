import typing
from pathlib import Path
from yaml import safe_load_all
from app import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    img = db.Column(db.String)
    link_watch = db.Column(db.String)
    link_twitter = db.Column(db.String)
    link_googlecal = db.Column(db.String, unique=True)
    date = db.Column(db.String(80))

    def __repr__(self) -> str:
        return f"<Event: {self.name}>"


def get_all_events() -> typing.List[Event]:
    return Event.query.all()


def read_events_from_file(path_to_file: typing.Union[Path, str]) -> typing.List[Event]:
    events: typing.List[Event] = []
    if not path_to_file:
        path_to_file = Path(__file__).parent / "static" / "events.yaml"
    with open(path_to_file) as events_file:
        all_events_gen = safe_load_all(events_file)
        for event_pairs_list in all_events_gen:
            event_dict: typing.Dict[str, str] = {
                key: val for d in event_pairs_list for key, val in d.items()
            }
            events.append(Event(**event_dict))
    return events


def db_init(events: typing.List[Event]) -> None:
    db.drop_all()
    db.create_all()
    for event in events:
        db.session.add(event)
    db.session.commit()
