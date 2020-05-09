INTRA_API = "https://intra-api.etna-alternance.net"
ETNA_API = "https://auth.etna-alternance.net"
AUTH_URL = "https://auth.etna-alternance.net/login"
MODULE_API = "https://modules-api.etna-alternance.net"
GSA_API = "https://gsa-api.etna-alternance.net"
TICKET_API = "https://tickets.etna-alternance.net/api"

IDENTITY_URL = ETNA_API + "/identity"
USER_INFO_URL = ETNA_API + "/api/users/{user_id}"
USER_PROMO_URL = INTRA_API + "/promo"
GRADES_URL = INTRA_API + "/terms/{promo_id}/students/{login}/marks"
NOTIF_URL = INTRA_API + "/students/{login}/informations"
ACTIVITY_URL = MODULE_API + "/students/{login}/currentactivities"
PICTURE_URL = ETNA_API + "/api/users/{login}/photo"
SEARCH_URL = MODULE_API + "/students/{login}/search"
ACTIVITIES_URL = MODULE_API + "/{module_id}/activities"
GROUPS_URL = INTRA_API + "/sessions/{module_id}/project/{project_id}/groups"
PROMOTION_URL = INTRA_API + "/trombi/{promo_id}"
GSA_EVENTS_URL = GSA_API + "/students/{login}/events"
GSA_LOGS_URL = GSA_API + "/students/{login}/logs"

EVENTS_URL = INTRA_API + "/students/{login}/events?end={end_date}&start={start_date}"
DECLARATION_URL = INTRA_API + "/modules/{module_id}/declareLogs"
DECLARATIONS_URL = GSA_API + "/students/{login}/declarations"

CONVERSATIONS_URL = INTRA_API + "/users/{user_id}/conversations"

TICKET_URL = TICKET_API + "/tasks/{task_id}.json"
TICKETS_URL = TICKET_API + "/tasks.json"
CLOSE_TICKET_URL = TICKET_API + "/tasks/{task_id}.json"
