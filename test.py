import facebook
graph = facebook.GraphAPI(access_token='EAAGwg103BWkBAKkDsP1r07BtUM87Dv6TkJnmMhyZA0CScNBpOYHZCoLfAmkopSTrgRL0FiLupH4AMBimE1BRqZCFzgaZAnxiRzRRTIKgWgmYgyFXxVnctV131ct03bO8NIJqJIg7ZCOjZBZBteg7jscO8xhoQaY9WOIKD3pXoZABSao4dUV0yneMRc3OsircuzYCs78weCKJNvmuqOkW935DO2DMzcwSAMY5vgBC2IZBs9KGsENY4Ce3e', version='3.1')

# Post something!
attachment =  {
    'name':'Post Test',
    'caption': 'Check out this example',
    'description': 'This is a longer description of the attachment',
}

graph.put_wall_post(message='我是一個Graph API測試, 大推Python超好玩!', attachment=attachment)