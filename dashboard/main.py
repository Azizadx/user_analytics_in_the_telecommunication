from multiapp import MultiApp
from pages import experience_analytics, user_behavoir, stisfaction

# Create MultiApp instance
app = MultiApp()

# Add pages to the app
app.add_app("User Behavoir", user_behavoir.app)
app.add_app("Experience analytics", experience_analytics.app)
app.add_app('User Satisfaction', stisfaction.app)


# Run the app
app.run()
