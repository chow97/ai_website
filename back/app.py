from bardapi import Bard

token = 'WwgFJMdZMAY-wK5hEiqYlWy_ZJdQ0Aa-GY6Li3rbnCFIwi6j_jbC3Drpqp92B9ZDBfmz0Q.'
bard = Bard(token=token)
bard.get_answer("what are some common containers for web app development")['content']