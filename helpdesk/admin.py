from django.contrib import admin

from .models import Helpdesk
from .models import Helpdesk_Status
from .models import Helpdesk_Priority

from .models.helpdesk.admin import HelpdeskAdmin
from .models.helpdesk_status.admin import HelpdeskStatusAdmin
from .models.helpdesk_priority.admin import HelpdeskPriorityAdmin


admin.site.register(Helpdesk, HelpdeskAdmin)
admin.site.register(Helpdesk_Status, HelpdeskStatusAdmin)
admin.site.register(Helpdesk_Priority, HelpdeskPriorityAdmin)
