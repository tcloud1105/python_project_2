import web
from Models import RegisterModel, LoginModel, Posts
import os

web.config.debug = False
urls = (
    '/','Home',
    '/register', 'Register',
    '/login','Login',
    '/logout','Logout',
    '/postregistration', 'PostRegistration',
    '/check-login', 'CheckLogin',
    '/post-activity', 'PostActivity',
    '/profile/(.*)/info','UserInfo',
    '/settings','UserSettings',
    'update-settings','UpdateSettings',
    '/profile/(.*)', 'UserProfile',
    '/submit-comment','SubmitComment',
    '/upload-image/(.*)','UploadImage'
)

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user',None})
session_data = session._initializer

render = web.template.render('Views/Templates/', base='MainLayout', globals={'session':session_data, 'current_user':session_data['user']})


# classes/routes
class Home:
    def GET(self):

        post_model = Posts.Posts()
        posts = post_model.get_all_posts()

        return render.Home(posts)

class Login:
    def GET(self):
        return render.Login()

class Register:
    def GET(self):
        return render.Register()

class PostRegistration:
    def POST(self):
        data = web.input()

        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username

class CheckLogin:
    def POST(self):
        data = web.input()
        login = LoginModel.LoginModel()

        isCorrect = login.check_user(data)

        if isCorrect:
            session_data['user'] = isCorrect
            return isCorrect

        return 'error'

class Logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None
        session.kill()
        return 'success'

class PostActivity:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']
        post_model = Posts.Posts()
        post_model.insert_post(data)

        return 'success'

class UserProfile:
    def GET(self,user):
        login = LoginModel.LoginModel()
        user_info = login.get_profile(user)

        post_model = Posts.Posts()
        posts = post_model.get_user_posts(user)

        return render.Profile(posts, user_info)

class UserInfo:
    def GET(self,user):
        login = LoginModel.LoginModel()
        user_info = login.get_profile(user)
        return render.Info(user_info)

class UserSettings:
    def GET(self, user):
        return render.Settings()

class UpdateSettings:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']

        setting_model = LoginModel.LoginModel()
        if setting_model.update_info(data):
            return 'success'
        else:
            return 'A fatal error has occurred.'

class SubmitComment:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']

        post_model = Posts.Posts()
        added_comment = post_model.add_comment(data)

        if added_comment:
            return added_comment
        else:
            return {"error": "403"}

class UploadImage:
    def POST(self,type):
        file = web.input(avatar={}, background={})

        file_dir = os.get_cwd()+"/static/uploads/"+ session_data['user']['username']

        if not os.path.exists(file_dir):
            os.makedir(file_dir)

        if "avatar" or "background" in file:
            filepath = file[type].filename.replace('\\', '/')
            filename = filepath.split('/')[-1]
            f = open(file_dir+"/"+filename, 'wb')
            f.write(file[type].file.read())
            f.close()

            update ={}
            update['type']= type
            update['img'] = '/static/uploads' + session_data["user"]["username"] +"/"+filename
            update['username'] = session_data['user']['username']

            account_model = LoginModel.LoginModel()
            update_avatar = account_model.update_image(update)

        raise web.seeother('/settings')

if __name__== "__main__":
     app.run()
