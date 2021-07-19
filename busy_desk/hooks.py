from . import __version__ as app_version

app_name = "busy_desk"
app_title = "Busy Desk"
app_publisher = "Jide Olayinka"
app_description = "Custom integration to enhenance easy flow"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "spryng.managed@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/busy_desk/css/busy_desk.css"
# app_include_js = "/assets/busy_desk/js/busy_desk.js"

# include js, css files in header of web template
# web_include_css = "/assets/busy_desk/css/busy_desk.css"
# web_include_js = "/assets/busy_desk/js/busy_desk.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "busy_desk/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Custom Jinja Filters
# ----------

jenv = {
	"methods": [
		"format_value:busy_desk.api.frappe_format_value"
	]
}

# Installation
# ------------

# before_install = "busy_desk.install.before_install"
# after_install = "busy_desk.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "busy_desk.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------
# jd:call==> in cronjob send_toeach_director
# "busy_desk.api.send_balances"
scheduler_events = {
	"cronstom":{
		"18 15 * * 1-6":[
			"busy_desk.tasks.cronstom"			
		]
	}
	# "all": [
	# 	"busy_desk.tasks.all"
	# ],
	# "daily": [
	# 	"busy_desk.tasks.daily"
	# ],
	# "hourly": [
	# 	"busy_desk.tasks.hourly"
	# ],
	# "weekly": [
	# 	"busy_desk.tasks.weekly"
	# ]
	# "monthly": [
	# 	"busy_desk.tasks.monthly"
	# ]
}

# Testing
# -------

# before_tests = "busy_desk.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "busy_desk.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "busy_desk.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"busy_desk.auth.validate"
# ]

fixtures = [
    {"dt":"Custom Field", 
	"filters": [
		["dt", "in", ("Contact")], ["fieldname", "in", ("is_customer_statement_contact","enable_torecieve_report")]]}
]

