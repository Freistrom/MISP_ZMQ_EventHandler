from .message import Message
import json


class Event(Message):
    """The MISP Event Model"""

    def from_json(self, json):
        event = Event()
        #for misp_event in json:
        event.id = json["Event"]["id"]
        event.orgc_id = json["Event"]["orgc_id"]
        event.org_id = json["Event"]["org_id"]
        event.date = json["Event"]["id"]
        event.threat_level_id = json["Event"]["id"]
        event.info = json["Event"]["id"]
        event.published = json["Event"]["id"]
        event.uuid = json["Event"]["id"]
        event.attribute_count = json["Event"]["id"]
        event.analyses = json["Event"]["id"]
        event.timestamp = json["Event"]["id"]
        event.distribution = json["Event"]["id"]
        event.proposal_email_lock = json["Event"]["id"]
        event.locked = json["Event"]["id"]
        event.publish_timestamp = json["Event"]["id"]
        event.sharing_group_id = json["Event"]["id"]
        event.event_creator_email = json["Event"]["id"]
        event.disable_correlation = json["Event"]["id"]
        event.id = json["Event"]["id"]
        event.id = json["Event"]["id"]
        return event

    def to_json(self):
        return json.dumps(self.__dict__)
