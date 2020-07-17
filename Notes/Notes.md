# Django Crash Course

## Why Django
Django is boring (mature)

Type out the code examples - build up the muscle memory!

## Hello World Project

If you're messing with manage.py, you're over-engineering your project.

ALLOWED_HOSTS is something to evaluate if you're having problems.

Even practice projects may go into production, so use a password manager.

Django admin is the only place that tracks stuff, everything else is untracked in DB.

Fixtures should not be used for serialization, use factory boy instead.

### Homepage App

apps.py will help with configuration.

General convention is to put templates in the project level directory instead of app level. Third party apps keep
 templates in the app level.
 
Create the view, then the template. Prevents you from creating orphan templates.

Templates are INTENTIONALLY stupid.

#### apps.py
When we need to use signals (similar to db triggers), we use the name for configuration
Think of it as referencing for globals
Should be scaffolding we don't touch

##### Variables in templates

You can insert variables or methods 
If method, don't use () if method, call from view.{method_name}
View object is always passed in with context_data

#### Context Data

Context data is inherited by the view.
Context is a type of dictionary.

## EveryCheese Project

"~update" naming convention: convention that prevents people from creating a username like "update"

Use the tag references in templates if you're having formatting errors. Don't reinvent the wheel with the templates.

If you're having performance issues, it's super likely due to DB queries

Make tests as simple and as stupid as possible

Squash migrations before going to production

Sometimes the test DB isn't erased at the end of testing. If a test refuses to fix or a field isn't present, try
 checking that.
 
Play the test coverage game.
 
You can use Django with FastAPI
 
### Class Based Views

