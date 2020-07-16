# Django Crash Course

## First Day Notes

### Why Django
Django is boring (mature)

Type out the code examples - build up the muscle memory!

### Hello World Project

If you're messing with manage.py, you're over-engineering your project.

ALLOWED_HOSTS is something to evaluate if you're having problems.

Even practice projects may go into production, so use a password manager.

Django admin is the only place that tracks stuff, everything else is untracked in DB.

Fixtures should not be used for serialization, use factory boy instead.

#### Homepage App

apps.py will help with configuration.

General convention is to put templates in the project level directory instead of app level. Third party apps keep
 templates in the app level.
 
Create the view, then the template. Prevents you from creating orphan templates.

Templates are INTENTIONALLY stupid.

##### apps.py
When we need to use signals (similar to db triggers), we use the name for configuration
Think of it as referencing for globals
Should be scaffolding we don't touch

###### Variables in templates

You can insert variables or methods 
If method, don't use () if method, call from view.{method_name}
View object is always passed in with context_data

##### Context Data

Context data is inherited by the view.
Context is a type of dictionary.

## EveryCheese Project

