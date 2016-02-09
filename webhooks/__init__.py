from tornado.web import Application
from webhooks._default import DefaultHandler

# Single Handler Apps
all_handlers = [
    (r"/", DefaultHandler),
]

# Multi Handler Apps
# all_handlers.extend(handlers_list)

app = Application(all_handlers)
