import facebook
graph = facebook.GraphAPI(access_token='', version='3.1')

# Post something!
   # Add a link and write a message about it.
graph.put_object(
    parent_object="me",
    connection_name="feed",
    message="This is a great website. Everyone should visit it.",
    link="https://www.facebook.com")