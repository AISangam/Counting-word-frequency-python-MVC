# Counting-word-frequency-python-MVC  
## Structure of the code-
I have followed mvc (model, view and controller) structure to build this app. Please look at the structure of the code from the screenshot from this link https://bit.ly/2ZHbHQg

<b>Understanding different files</b>
<ul>
<li><b><em>Manage.py</b></em>: Python file from where one can run app designed. Some times while you run the file manage.py you would be ecnountered with the error as raise_child_exception_type. Please see the screenshot added here for this error as https://bit.ly/2PBfSbv</li>
<li><b><em>__init__.py</b></em>: It helps in treating the files contained inside the directory as packages. This is the first file to be loaded in the module. It facilities importing other python files.</li>
  <li><b><em>settings.py</b></em>: One can mention the path of templates folder where .html files are placed and static folder where bootstrap, css and images are kept. Connection to the database is also implemented here. For example, in this code connection to mysql database is implemented using SQLAlchemy. Flask provides facilities of flask_login which can also mentioned here. Let us see these functions. Remember application run  __init__ file is run which in turns run the file settings.py 
<ol>
<li><b><em>Flask-Login</b></em>: It provides user session management for flask. It stores active user id in the session and let you log them and log out easily. It protects user session not to be stolen by cookies.
<ul>
<li><b><em>Login Manager class of the Flask-login</b></em>: login_manager is the instance of the class (Login Manager)  which let your application to load the user from the ID. When the object (login_manager) is created, one have to configure it to the login with the below code  
  
```
login_manager.init_app(app)
```  

</li>
<li><b><em>user_loader</b></em>: It is a callback which is used to reload the user object from the user id which is stored in the session.
</li>
</ul>
<li><b><em>Database connection</b></em>: In settings.py, connection to database is acheieved using flask_sqlalchemy. If there is any problem while integrating with mysql, please use pymysql along with mysql. Please see the below code. </li>

```
mysql+pymysql://root:''@localhost/frequency_occurence'
  ```
<li><b><em>Secret Key</b></em>: This is the secret key which is used with the flask application. frequency_occurence is the name of the database which i have created in the mysql database.
</li>
</ol>
<li><b><em>models.py</b></em>: This is the file where table inside the database is created. Name of the table inside the database (frequency_occurence) is user_details which have the following columns
  <ul> 
    <li>username, password, email</li>
    <li><b><em>Flask authentication</b></em>: This is another authentication which one can use with in this file. These are as below:</li>
  </ul>  
  
  ``` 
  # Flask-Login integration
	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return self.id
  ``` 
  <li><b><em>urls.py</b></em>: This is the file which is used to create the endpoints. These are the routes which are created. </li>
  <li><b><em>views.py</b></em>: This is the file where the views are written which will be shown to the users. Routes are the end points whose functions are written in the views file.</li> 
<li><b><em>code_functions.py</b></em>: This is the file which is used to create the functions. When the functions are used in the view file these are imported from there.</li>  


```
def frequency_occurence(text): 
  words_tokens = word_tokenize(text.lower())
# print("Tokens or words of sentence are:", words_tokens)
# Load stop words
  stop_words = stopwords.words('english')
# print("Stop words are:", stop_words)

  recitified_words = [words  for words in words_tokens if words not in stop_words]
# print("Show the cleaned text", recitified_words)

# remove punctuation from the text using isalpha
  cleaned_words = [words for words in recitified_words if words.isalpha()]
# print(cleaned_words)

# removing article 'the' from the list
  tok_to_remove = "the"
  final_words = [words for words in cleaned_words if words not in tok_to_remove]
# print("final words are...", final_words)

  list_dupl_check= list()

  for words in final_words:
  	if words not in list_dupl_check:
  		list_dupl_check.append(words)
  
  final_dict = dict()
  for unique_words in list_dupl_check:
  	 final_dict[unique_words] = final_words.count(unique_words) 
  	 # final_list.append(final_words.count(unique_words))
  
  return (final_dict)
```


<li><b><em>Salient Features of this code</b></em>: There are two views which are shown to user.
	<ul>
		<li> View 1: In this view, user who are not registered can see the following details. These are the general details and they cannot see the app which I have developed which is to count the frequency of the cleaned words in the text. For better visualization please see the below screenshot</li>  </ul> 
	
		
		![screenshot_1](https://user-images.githubusercontent.com/35392729/56882652-dba72300-6a81-11e9-9b4d-cdee42e9e028.png)  
		
<ul>
<li> View 2: In this view, user who have registered and successfully login will see the app and they can play with that and have the option to logout from the app.   <li></ul>
	
	
	![screenshot2](https://user-images.githubusercontent.com/35392729/56882827-6720b400-6a82-11e9-832d-fae906e9f559.png)
		
</li>	

Once the user  are login with the right credentials, they can play with the app as below

![screenshot3](https://user-images.githubusercontent.com/35392729/56882995-fcbc4380-6a82-11e9-9001-73136a3069fd.png)  

![screenshot4](https://user-images.githubusercontent.com/35392729/56883013-0776d880-6a83-11e9-83c2-e81f1b2c07ac.png)


  


  
