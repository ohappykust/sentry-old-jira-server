from sentry.rules import rules

from .actions.create_ticket import *  # noqa: F401,F403
from .actions.create_ticket import OldJiraServerCreateTicketAction
from .client import *  # noqa: F401,F403
from .integration import *  # noqa: F401,F403
from .search import *  # noqa: F401,F403
from .urls import *  # noqa: F401,F403
from .webhooks import *  # noqa: F401,F403

rules.add(OldJiraServerCreateTicketAction)
