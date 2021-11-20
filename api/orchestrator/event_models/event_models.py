from api.orchestrator.event_models.attendance import EventModelAttendance
from api.orchestrator.event_models.bulk import EventModelBulk
from api.orchestrator.event_models.channel import EventModelChannelMixin
from api.orchestrator.event_models.citizen import EventModelCitizen
from api.orchestrator.event_models.documents import EventModelDocuments
from api.orchestrator.event_models.routers import EventModelRouters
from api.orchestrator.event_models.service import EventModelServiceMixin
from api.orchestrator.event_models.skill import EventModelSkillMixin


class EventModels(EventModelBulk,
                  EventModelAttendance,
                  EventModelDocuments,
                  EventModelCitizen,
                  EventModelRouters,
                  EventModelSkillMixin,
                  EventModelChannelMixin,
                  EventModelServiceMixin):

    def __init__(self):
        super(EventModels, self).__init__()

