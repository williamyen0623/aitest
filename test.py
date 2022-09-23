import facebook
graph = facebook.GraphAPI(access_token='EAAGwg103BWkBAKkDsP1r07BtUM87Dv6TkJnmMhyZA0CScNBpOYHZCoLfAmkopSTrgRL0FiLupH4AMBimE1BRqZCFzgaZAnxiRzRRTIKgWgmYgyFXxVnctV131ct03bO8NIJqJIg7ZCOjZBZBteg7jscO8xhoQaY9WOIKD3pXoZABSao4dUV0yneMRc3OsircuzYCs78weCKJNvmuqOkW935DO2DMzcwSAMY5vgBC2IZBs9KGsENY4Ce3e', version='3.1')

# Post something!
   # Add a link and write a message about it.
graph.put_object(
    parent_object="me",
    connection_name="feed",
    message="This is a great website. Everyone should visit it.",
    link="https://www.facebook.com")