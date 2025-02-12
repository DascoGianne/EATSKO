#Dependencies
from tkinter import *
from PIL import ImageTk, Image
from customtkinter import *
import customtkinter as ctk 
from tkinter import messagebox
import json

# WINDOW
window = ctk.CTk()

#ACCOUNT FRAMES
login_page = Frame(window, bg='white')
create_page = Frame(window, bg='white')

# NAVIGATION FRAMES
homepage = Frame(window, bg='white')
categories_page = Frame(window, bg='white')
store_page = Frame(window, bg='white')
search_page = Frame(window, bg='white')

# CATEGORIES FRAMES
meals_page = Frame(window, bg='white')
drinks_page = Frame(window, bg='white')
dessert_page = Frame(window, bg='white')
snacks_page = Frame(window, bg='white')

# SEARCH FRAMES
cart_page = Frame(window, bg='white')

# NAVIGATION FUNCTION
def homeFunction():
    homepage.place(relheight=1, relwidth=1)
    categories_page.place_forget()
    store_page.place_forget()
    search_page.place_forget()
    meals_page.place_forget()
    drinks_page.place_forget()
    dessert_page.place_forget()
    snacks_page.place_forget()
    cart_page.place_forget()
    login_page.place_forget()
    create_page.place_forget()
    
    header_color.place(x=0, y=0)
    Logo_Button.place(x=0, y=0)
    header_name.place(x=200, y=10)
    homeButton.place(x=770, y=45)
    categoriesButton.place(x=880, y=45)
    storeButton.place(x=1050, y=45)
    searchButton.place(x=1170, y=45)
    logoutButton.place(x=1290, y=45)

    homeButton.config(bg='white', fg='#7d1418')
    categoriesButton.config(bg='#7d1418', fg='white')
    storeButton.config(bg='#7d1418', fg='white')
    searchButton.config(bg='#7d1418', fg='white')

def categoriesFunction():
    categories_page.place(relheight=1, relwidth=1)
    homepage.place_forget()
    store_page.place_forget()
    search_page.place_forget()
    meals_page.place_forget()
    drinks_page.place_forget()
    dessert_page.place_forget()
    snacks_page.place_forget()
    cart_page.place_forget()
    login_page.place_forget()
    create_page.place_forget()

    categoriesButton.config(bg='white', fg='#7d1418')
    homeButton.config(bg='#7d1418', fg='white')
    storeButton.config(bg='#7d1418', fg='white')
    searchButton.config(bg='#7d1418', fg='white')

def storeFunction():
    store_page.place(relheight=1, relwidth=1)
    homepage.place_forget()
    categories_page.place_forget()
    search_page.place_forget()
    meals_page.place_forget()
    drinks_page.place_forget()
    dessert_page.place_forget()
    snacks_page.place_forget()
    cart_page.place_forget()
    login_page.place_forget()
    create_page.place_forget()


    storeButton.config(bg='white', fg='#7d1418')
    homeButton.config(bg='#7d1418', fg='white')
    categoriesButton.config(bg='#7d1418', fg='white')
    searchButton.config(bg='#7d1418', fg='white')

def searchFunction():
    search_page.place(relheight=1, relwidth=1)
    homepage.place_forget()
    categories_page.place_forget()
    store_page.place_forget()
    meals_page.place_forget()
    drinks_page.place_forget()
    dessert_page.place_forget()
    snacks_page.place_forget()
    cart_page.place_forget()
    login_page.place_forget()
    create_page.place_forget()

    searchReset()

    searchButton.config(bg='white', fg='#7d1418')
    homeButton.config(bg='#7d1418', fg='white')
    categoriesButton.config(bg='#7d1418', fg='white')
    storeButton.config(bg='#7d1418', fg='white')

#USER ACCOUNT FUNCTIONS

#LOG IN PAGE
def loginPagefunction():
    login_page.place(relheight=1, relwidth=1)
    homepage.place_forget()
    categories_page.place_forget()
    search_page.place_forget()
    meals_page.place_forget()
    drinks_page.place_forget()
    dessert_page.place_forget()
    snacks_page.place_forget()
    store_page.place_forget()
    create_page.place_forget()
    logoutButton.place_forget()

    header_color.place_forget()
    Logo_Button.place_forget()
    header_name.place_forget()
    homeButton.place_forget()
    categoriesButton.place_forget()
    storeButton.place_forget()
    searchButton.place_forget()

#CREATE PAGE    
def createPagefunction():
    create_page.place(relheight=1, relwidth=1)
    homepage.place_forget()
    categories_page.place_forget()
    search_page.place_forget()
    meals_page.place_forget()
    drinks_page.place_forget()
    dessert_page.place_forget()
    snacks_page.place_forget()
    store_page.place_forget()
    login_page.place_forget()

#LOG IN FUNCTION
def loginfunction():
    global user
    global validuser

    validuser = 0
    user = loginUsername.get()
    ValidPassword = [{"password":loginPassword.get()}]
    with open('data.json', 'r') as f:
        people = json.loads(f.read())
    if user == '' or ValidPassword == '':
        messagebox.showerror(title="Try again", message="Please fill in the required fields")
    elif user != '' or ValidPassword != '':
        for key,val in people.items():
            if user == key and ValidPassword == val:
                validuser = 1
                homeFunction()
            elif user == key and ValidPassword != val:
                validuser = 1
                messagebox.showerror(title="Try again", message= "Wrong Credentials")
        if validuser != 1:
            messagebox.showerror(title="Try again", message= "Wrong Credentials")

#CREATE FUNCTION
def createfunction():
    global newUser
    global newPass
    global validCreate
    newUser = createUsername.get()
    newPass = createPassword.get()
    newUserSize = len(newUser)
    newPassSize = len(newPass)
    validCreate = 0
    
    #Opens json data file and Error Handler
    with open('data.json', 'r') as f:
        people = json.loads(f.read())
        if newUser == '' and newPass == '':
            messagebox.showerror(title="Invalid input", message="Please fill in the required fields")
        elif newUser == '' and newPass != '':
            messagebox.showerror(title="Invalid input", message="Username Field Required")
        elif newUser != '' and newPass == '':
            messagebox.showerror(title="Invalid input", message="Password Field Required")
        elif newUserSize < 5 or newPassSize < 5:
            messagebox.showerror(title="Failed", message="Please provide atleast 5 characters for both fields")
        elif newUser != '' and newPass != '':
            for key,val in people.items():
                if newUser != key:
                    validCreate = 1
                elif newUser == key:
                        validCreate = 0
                        messagebox.showerror(title="Failed", message=newUser + " already exist")
                        break
        
        if validCreate == 1 and newUserSize >= 5 and newPassSize >= 5:
            with open('data.json', 'r') as f:
                    data = json.loads(f.read())
                    data[newUser] = [{"password":newPass}]
                    accounts = json.dumps(data, indent=4)
                    with open('data.json', 'w') as f:
                        f.write(accounts)
                    validCreate = 0
                    messagebox.showinfo(title="Success", message="You have successfully created an account")


#Rating function
def star_rate1 ():
    global star_count
    star_rate_unshaded()
    star_label1.config(text = "★")
    star_count = 1

def star_rate2 ():
    global star_count
    star_rate_unshaded()
    star_label1.config(text = "★")
    star_label2.config(text = "★")
    star_count = 2


def star_rate3 ():
    global star_count
    star_rate_unshaded()
    star_label1.config(text = "★")
    star_label2.config(text = "★")
    star_label3.config(text = "★")
    star_count = 3

def star_rate4 ():
    global star_count
    star_rate_unshaded()
    star_label1.config(text = "★")
    star_label2.config(text = "★")
    star_label3.config(text = "★")
    star_label4.config(text = "★")
    star_count = 4

def star_rate5 ():
    global star_count
    star_rate_unshaded()
    star_label1.config(text = "★")
    star_label2.config(text = "★")
    star_label3.config(text = "★")
    star_label4.config(text = "★")
    star_label5.config(text = "★")
    star_count = 5

def star_rate_unshaded ():
    star_label1.config(text = "☆")
    star_label2.config(text = "☆")
    star_label3.config(text = "☆")
    star_label4.config(text = "☆")
    star_label5.config(text = "☆")

def submit():
    global star_count
    count = star_count

    if count == 0:
           messagebox.showwarning("Warning!",f"Please select rating before you submit!")
    elif count == 1:
           messagebox.showinfo("Rate our App!",f"Thank you for the {count} star rating!")
    else:
        messagebox.showinfo("Rate our App!",f"Thank you for the {count} stars rating!")


    ratelabel.destroy()
    star_label1.destroy()
    star_label2.destroy()
    star_label3.destroy()
    star_label4.destroy()
    star_label5.destroy()
    submit_button.destroy()

    ratelabel1 = Label(homeScrollbar, text = "Thank you!")
    ratelabel1.config(font = ('Raleway',14,'bold'))    
    ratelabel1.config(fg = ('white'))
    ratelabel1.config(bg = '#7d1418')
    ratelabel1.place(x=1225,y=1180)

# CATEGORIES FUNCTION

#MEALS PAGE
def mealFunction():
    homepage.place_forget()
    meals_page.place(relheight=1, relwidth=1)
    categories_page.place_forget()
    drinks_page.place_forget()
    dessert_page.place_forget()
    snacks_page.place_forget()
    cart_page.place_forget()

#DRINKS PAGE
def drinksFunction():
    drinks_page.place(relheight=1, relwidth=1)
    homepage.place_forget()
    categories_page.place_forget()
    meals_page.place_forget()
    dessert_page.place_forget()
    snacks_page.place_forget()
    cart_page.place_forget()

#DESSERT PAGE
def dessertFunction():
    dessert_page.place(relheight=1, relwidth=1)
    homepage.place_forget()
    categories_page.place_forget()
    meals_page.place_forget()
    drinks_page.place_forget()
    snacks_page.place_forget()
    cart_page.place_forget()

#SNACKS PAGE
def snacksFunction():
    snacks_page.place(relheight=1, relwidth=1)
    homepage.place_forget()
    categories_page.place_forget()
    meals_page.place_forget()
    drinks_page.place_forget()
    dessert_page.place_forget()
    cart_page.place_forget()

# STORES FUNCTION
def cuadroFunction():
    cdjmenu = Toplevel()
    canvas = Canvas(cdjmenu, width=790, height=259)
    canvas.pack(expand=YES, fill=BOTH)
    cuadroMenu = PhotoImage(file='images/CUADRO DE J MENU.png')
    canvas.create_image(0, 0, image=cuadroMenu, anchor=NW)
    canvas.cuadroMenu = cuadroMenu

def davidFunction():
    dwmenu = Toplevel()
    canvas = Canvas(dwmenu, width=700, height=560)
    canvas.pack(expand=YES, fill=BOTH)
    davidMenu = PhotoImage(file='images/DAVIDS WINGS MENU.png')
    canvas.create_image(0, 0, image=davidMenu, anchor=NW)
    canvas.davidMenu = davidMenu

def koffiFunction():
    kmenu = Toplevel()
    canvas = Canvas(kmenu, width=708, height=491)
    canvas.pack(expand=YES, fill=BOTH)
    koffiMenu = PhotoImage(file='images/KOFICCINO MENU.png')
    canvas.create_image(0, 0, image=koffiMenu, anchor=NW)
    canvas.waffleMenu = koffiMenu

def waffleFunction():
    wmenu = Toplevel()
    canvas = Canvas(wmenu, width=400, height=496)
    canvas.pack(expand=YES, fill=BOTH)
    waffleMenu = PhotoImage(file='images/WAFFLE TIME MENU.png')
    canvas.create_image(0, 0, image=waffleMenu, anchor=NW)
    canvas.waffleMenu = waffleMenu

def yummybFunction():
    ybmenu = Toplevel()
    yummyCanvas = Canvas(ybmenu, width=710, height=296, confine=TRUE)
    yummyCanvas.pack(expand=YES, fill=BOTH)
    yummybMenu = PhotoImage(file='images/YUMMY BURGER MENU.png')
    yummyCanvas.create_image(0, 0, image=yummybMenu, anchor=NW)
    yummyCanvas.yummybMenu = yummybMenu


# WINDOW
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 1400
appHeight = 860
x = (screenWidth / 2) - (appWidth / 2)
y = (screenHeight / 2) - (appHeight / 2)
window.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
window.title("EATSKO")

# ICON
window.iconbitmap('ICON LOGO.ico')

#LOGIN BACKGROUND
loginBg_image = Image.open("images/desktop login.png") 
loginBgResized = loginBg_image.resize((1440,900))
loginBg_photo = ImageTk.PhotoImage(loginBgResized)
loginBg_label = Label(login_page, image=loginBg_photo)
loginBg_label.place(x=0, y=0, relwidth=1, relheight=1)

createBg_image = Image.open("images/desktop login.png") 
createBgResized = createBg_image.resize((1440,900))
createBg_photo = ImageTk.PhotoImage(createBgResized)
createBg_label = Label(create_page, image=createBg_photo)
createBg_label.place(x=0, y=0, relwidth=1, relheight=1)

#LOGIN PAGE WIDGETS
loginUsername = ctk.CTkEntry(login_page, width=326, corner_radius=20, bg_color="#5c0403")
loginUsername.configure(placeholder_text = "Username", fg_color ="White", border_color = "#7d1418")
loginUsername.configure(placeholder_text_color = "#7d1418",text_color="black")
loginUsername.place(relx=0.5,rely=0.70, anchor= CENTER)

loginPassword = ctk.CTkEntry(login_page, width=326, corner_radius=20, bg_color="#5c0403")
loginPassword.configure(placeholder_text = "Password", fg_color ="White", border_color = "#7d1418")
loginPassword.configure(placeholder_text_color = "#7d1418",text_color="black", show="*")
loginPassword.place(relx=0.5,rely=0.75, anchor= CENTER)

loginImagePath = Image.open("images/loginpic.png")
loginImageResize = loginImagePath.resize((95,15))
loginButton = ImageTk.PhotoImage(loginImageResize)
loginpic = Button(login_page, bd=0,text="Button", image=loginButton,borderwidth=0,highlightthickness=0, bg='white', command=lambda: loginfunction())
loginpic.place(relx=0.5,rely=0.80, anchor= CENTER)

createImagePath = Image.open("images/createaccpic.png")
createImageResize = createImagePath.resize((100,20))
createButton = ImageTk.PhotoImage(createImageResize)
createpic = Button(login_page, bd=0,text="Button",image=createButton,borderwidth=0,highlightthickness=0, bg='white', command=lambda: createPagefunction())
createpic.place(relx=0.5,rely=0.83, anchor= CENTER)

#CREATE PAGE WIDGETS
createUsername = ctk.CTkEntry(create_page, width=326, corner_radius=20, bg_color="#5c0403")
createUsername.configure(placeholder_text = "Username", fg_color ="White", border_color = "#7d1418")
createUsername.configure(placeholder_text_color = "#7d1418",text_color="#7d1418")
createUsername.place(relx=0.5,rely=0.70, anchor= CENTER)

createPassword = ctk.CTkEntry(create_page, width=326, corner_radius=20, bg_color="#5c0403")
createPassword.configure(placeholder_text = "Password", fg_color ="White", border_color = "#7d1418")
createPassword.configure(placeholder_text_color = "#7d1418",text_color="black", show="*")
createPassword.place(relx=0.5,rely=0.75, anchor= CENTER)

create1ImagePath = Image.open("images/createaccpic.png")
create1ImageResize = create1ImagePath.resize((100,20))
create1Button = ImageTk.PhotoImage(create1ImageResize)
create1pic = Button(create_page, bd=0,text="Button",image=create1Button,borderwidth=0,highlightthickness=0, bg='white', command=lambda: createfunction())
create1pic.place(relx=0.5,rely=0.80, anchor= CENTER)

alreadyButton = Button(create_page,text="Already have an account?", bd=0,highlightthickness=0, bg='white', command=lambda: loginPagefunction())
alreadyButton.config(font = ('Arial', 8,'bold'), fg="white",bg = "#5c0403")
alreadyButton.place(relx=0.5,rely=0.83, anchor= CENTER)

# SCROLLBAR
homeScrollbar = ctk.CTkScrollableFrame(homepage, width=500, height=500, corner_radius=0, fg_color='white')
homeScrollbar.place(x=0, y=0, relwidth=1, relheight=1)

# HEADER
header_color = Label(window, text="")
header_color.config(font=('Times new roman', 22, 'bold', 'italic'))
header_color.config(fg=('white'))
header_color.config(bg='#7d1418')
header_color.place(x=0, y=0)
header_color.config(padx=1000)
header_color.config(pady=30)

# LOGO BUTTON
original_logo = Image.open("images/LOGO BUTTON.png")
L_Button = ImageTk.PhotoImage(original_logo)
Logo_Button = Button(window, text="Button", image=L_Button, bd=0,
                     highlightthickness=0, bg='white', command=lambda: homeFunction())
Logo_Button.place(x=0, y=0)

#EATSKO LABEL
header_name = Label(window, text="EATSKO ", font=('Shrikhand', 40, 'bold'),
                    fg=('white'), bg='#7d1418')
header_name.place(x=200, y=10)

# NAVIGATION MENU

#HOME BUTTON
homeButton = Button(window, command=lambda: homeFunction())
homeButton.config(text="|   Home ", bd=0)
homeButton.config(font=('Raleway', 15, 'bold'))
homeButton.config(fg=('black'))
homeButton.config(bg='white', activebackground='white')
homeButton.place(x=770, y=45)

#CATEGORIES BUTTON
categoriesButton = Button(window, command=lambda: categoriesFunction())
categoriesButton.config(text="|    Categories ", bd=0)
categoriesButton.config(font=('Raleway', 15, 'bold'))
categoriesButton.config(fg=('white'))
categoriesButton.config(bg='#7d1418')
categoriesButton.place(x=880, y=45)

#STORE BUTTON
storeButton = Button(window, command=lambda: storeFunction())
storeButton.config(text="|    Stores ", bd=0)
storeButton.config(font=('Raleway', 15, 'bold'))
storeButton.config(fg=('white'))
storeButton.config(bg='#7d1418')
storeButton.place(x=1050, y=45)

#SEARCH BUTTON
searchButton = Button(window, command=lambda: searchFunction())
searchButton.config(text="|    Search ", bd=0)
searchButton.config(font=('Raleway', 15, 'bold'))
searchButton.config(fg=('white'))
searchButton.config(bg='#7d1418')
searchButton.place(x=1170, y=45)

#LOGOUT BUTTON
logoutButton = Button(window, command=lambda: loginPagefunction())
logoutButton.config(text="|    Logout    |", bd=0)
logoutButton.config(font=('Raleway', 15, 'bold'))
logoutButton.config(fg=('white'))
logoutButton.config(bg='#7d1418')
logoutButton.place(x=1290, y=45)


#FOOTER
footerImagePath = PhotoImage(file="images/FOOTER1.png")
footerFrame = Frame(homeScrollbar, width=1440, height=133, bg='red')
footerFrame.grid(row=100, columnspan=10)
footerImageLabel = Label(footerFrame, image=footerImagePath)
footerImageLabel.place(x=0, y=0, relwidth=1, relheight=1)

loginPagefunction()

#HOMEPAGE WIDGETS

#tagline
labelTagline = Label(homeScrollbar, text="Eats very good")
labelTagline.config(font=('Shrikhand', 40, 'bold'))
labelTagline.config(fg='#7d1418', bg='white')
labelTagline.grid(row=1, column=2, columnspan=4, pady=(100, 0))

#FEWA
recoCategory = Image.open("images/FEWA1.png")
recoButton = ImageTk.PhotoImage(recoCategory)
recoPicture = Button(homeScrollbar, text="Button", image=recoButton, bd=0, borderwidth=0,
                     highlightthickness=0, bg='white', activebackground='white', command = lambda: reco1Redirect())
recoPicture.grid(row=3, column=2, padx=0, pady=(0, 100))

#Chicken
reco1Category = Image.open("images/RECO1.png")
reco1Button = ImageTk.PhotoImage(reco1Category)
reco1Picture = Button(homeScrollbar, text="Button", image=reco1Button, bd=0,
                      highlightthickness=0, bg='white', activebackground='white', command = lambda: reco2Redirect())
reco1Picture.grid(row=3, column=3, padx=0, pady=(0, 100))

#Froyo
reco2Category = Image.open("images/RECO2.png")
reco2Button = ImageTk.PhotoImage(reco2Category)
reco2Picture = Button(homeScrollbar, text="Button", image=reco2Button, bd=0,
                      highlightthickness=0, bg='white', activebackground='white',  command = lambda: reco3Redirect())
reco2Picture.grid(row=3, column=4, padx=0, pady=(0, 100))

#Burger
reco3Category = Image.open("images/RECO3.png")
reco3Button = ImageTk.PhotoImage(reco3Category)
reco3Picture = Button(homeScrollbar, text="Button", image=reco3Button, bd=0,
                      highlightthickness=0, bg='white', activebackground='white',  command = lambda: reco4Redirect())
reco3Picture.grid(row=3, column=5, padx=(20,0), pady=(0, 100))

#categories label
labelStore = Label(homeScrollbar, text="Categories ")
labelStore.config(font=('Shrikhand', 40, 'bold', 'italic'))
labelStore.config(fg='#7d1418', bg='white')
labelStore.grid(row=5, column=2, pady=(0, 10))

#meals in homepage
mealB = PhotoImage(file="images/MEALS.png")
mealPicture = Button(homeScrollbar, image=mealB, bd=0,
                     highlightthickness=0, bg='white', command=lambda: mealFunction())
mealPicture.grid(row=7, column=2, padx=(0, 0), pady=(10, 100), sticky='e')

#drinks in homepage
drinksB = PhotoImage(file="images/DRINKS.png")
drinksPicture = Button(homeScrollbar, image=drinksB, bd=0,
                       highlightthickness=0, bg='white', command=lambda: drinksFunction())
drinksPicture.grid(row=7, column=3, padx=(20, 20), pady=(10, 100))

#snacks in homepage
snacksB = PhotoImage(file="images/SNACKS.png")
snacksPicture = Button(homeScrollbar, image=snacksB, bd=0,
                       highlightthickness=0, bg='white', command=lambda: snacksFunction())
snacksPicture.grid(row=7, column=4, padx=(0, 10), pady=(10, 100), sticky='w')

#dessert in homepage
dessertB = PhotoImage(file="images/DESSERT.png")
dessertPicture = Button(homeScrollbar, image=dessertB, bd=0,
                        highlightthickness=0, bg='white', command=lambda: dessertFunction())
dessertPicture.grid(row=7, column=5, padx=(0, 0), pady=(10, 100), sticky='w')

#Rate our app na label
ratelabel = Label(homeScrollbar, text = "Rate our app!")
ratelabel.config(font = ('Raleway',16,'bold'))    
ratelabel.config(fg = ('white'))
ratelabel.config(bg = '#7d1418')
ratelabel.place(x=1198, y=1140)

star_label1 = Button(homeScrollbar, text="☆", borderwidth=0, highlightthickness=0, bg="#7d1418")
star_label1.config(font=('Arial', 18, 'bold'), fg="yellow", command=star_rate1)
star_label1.place(x=1170, y=1170)


star_label2 = Button(homeScrollbar, text="☆", borderwidth=0, highlightthickness=0, bg="#7d1418")
star_label2.config(font=('Arial', 18, 'bold'), fg="yellow", command=star_rate2)
star_label2.place(x=1210, y=1170)


star_label3 = Button(homeScrollbar, text="☆", borderwidth=0, highlightthickness=0, bg="#7d1418")
star_label3.config(font=('Arial', 18, 'bold'), fg="yellow", command=star_rate3)
star_label3.place(x=1250, y=1170)


star_label4 = Button(homeScrollbar, text="☆", borderwidth=0, highlightthickness=0, bg="#7d1418")
star_label4.config(font=('Arial', 18, 'bold'), fg="yellow", command=star_rate4)
star_label4.place(x=1290, y=1170)


star_label5 = Button(homeScrollbar, text="☆", borderwidth=0, highlightthickness=0, bg="#7d1418")
star_label5.config(font=('Arial', 18, 'bold'), fg="yellow", command=star_rate5)
star_label5.place(x=1330, y=1170)


#submit
submit_button = Button(homeScrollbar, text="Submit", borderwidth=0, highlightthickness=0, bg="#7d1418")
submit_button.config(font=('Arial', 16), fg="white", command = submit)
submit_button.place(x= 1230, y = 1203)

# CATEGORIES PAGE WIDGETS

#label categories
labelStore = Label(categories_page, text="Categories ")
labelStore.config(font=('Shrikhand', 40, 'bold', 'italic'))
labelStore.config(fg='#7d1418', bg='white')
labelStore.place(x=550, y=100)

# MEALS BUTTON IN CATEGORIES PAGE
mealCategory = Image.open("images/MEALS.png")
mealButton = ImageTk.PhotoImage(mealCategory)
mealPicture = Button(categories_page, text="Button", image=mealButton, bd=0,
                     highlightthickness=0, bg='white', command=lambda: mealFunction())
mealPicture.place(x=180, y=200)

# DRINKS BUTTON IN CATEGORIES PAGE
drinksCategory = Image.open("images/DRINKS.png")
drinksButton = ImageTk.PhotoImage(drinksCategory)
drinksPicture = Button(categories_page, text="Button", image=drinksButton, bd=0,
                       highlightthickness=0, bg='white', command=lambda: drinksFunction())
drinksPicture.place(x=450, y=200)

# SNACKS BUTTON IN CATEGORIES PAGE
snacksCategory = Image.open("images/SNACKS.png")
snacksButton = ImageTk.PhotoImage(snacksCategory)
snacksPicture = Button(categories_page, text="Button", image=snacksButton, bd=0,
                       highlightthickness=0, bg='white', command=lambda: snacksFunction())
snacksPicture.place(x=720, y=200)

# DESSERT BUTTON IN CATEGORIES PAGE
dessertCategory = Image.open("images/DESSERT.png")
dessertButton = ImageTk.PhotoImage(dessertCategory)
dessertPicture = Button(categories_page, text="Button", image=dessertButton, bd=0,
                        highlightthickness=0, bg='white', command=lambda: dessertFunction())
dessertPicture.place(x=990, y=200)

#label "what are you craving"
label = Label(categories_page, text="What are you \n craving?  ")
label.config(font=('Shrikhand', 40, 'bold', 'italic'))
label.config(fg='#7d1418', bg='white')
label.place(x=500, y=580)

# MEALS WIDGETS

#meals label
mealslabelStore = Label(meals_page, text="Meals ")
mealslabelStore.config(font=('Shrikhand', 40, 'bold', 'italic'))
mealslabelStore.config(fg='#7d1418', bg='white')
mealslabelStore.place(x=550, y=120)

# RETURN BUTTON
backLogo = Image.open("images/BACK BUTTON.png")
backImage = ImageTk.PhotoImage(backLogo)
backButton = Button(meals_page, text="Button", image=backImage, bd=0,
                    highlightthickness=0, bg='white', command=lambda: categoriesFunction())
backButton.place(x=150, y=100)

#Meals IMAGE PATHS
mealsImagePath = Image.open("CATEGORIES PICS/Meals_categories/1.png")
meals1ImagePath = Image.open("CATEGORIES PICS/Meals_categories/2.png")
meals2ImagePath = Image.open("CATEGORIES PICS/Meals_categories/3.png")
meals3ImagePath = Image.open("CATEGORIES PICS/Meals_categories/4.png")
meals4ImagePath = Image.open("CATEGORIES PICS/Meals_categories/5.png")
meals5ImagePath = Image.open("CATEGORIES PICS/Meals_categories/6.png")
meals6ImagePath = Image.open("CATEGORIES PICS/Meals_categories/7.png")
meals7ImagePath = Image.open("CATEGORIES PICS/Meals_categories/8.png")
meals8ImagePath = Image.open("CATEGORIES PICS/Meals_categories/9.png")
meals9ImagePath = Image.open("CATEGORIES PICS/Meals_categories/10.png")
meals10ImagePath = Image.open("CATEGORIES PICS/Meals_categories/11.png")
meals11ImagePath = Image.open("CATEGORIES PICS/Meals_categories/12.png")

#meals frame
mealsFrame = Frame(meals_page, bg = 'white', width=1440, height = 650)
mealsFrame.place(x = 0, y = 190)

# meals scrollbar
mealsScrollbar = ctk.CTkScrollableFrame(mealsFrame, width = 1440, height = 500, corner_radius = 0, fg_color='white')
mealsScrollbar.place(x = 0, y = 0, relwidth = 1, relheight = 1)

#display pictures of meals
meals_categoriesImageResize = mealsImagePath.resize((250,250))
meals_categoriesImageResized = ImageTk.PhotoImage(meals_categoriesImageResize)
meals_categoriesImageSearch = Label(mealsScrollbar, image=meals_categoriesImageResized)
meals_categoriesImageSearch.grid(row = 0, column = 2, padx = (200,0),  sticky = 'w')

meals1_categoriesImageResize = meals1ImagePath.resize((250,250))
meals1_categoriesImageResized = ImageTk.PhotoImage(meals1_categoriesImageResize)
meals1_categoriesImageSearch = Label(mealsScrollbar, image=meals1_categoriesImageResized)
meals1_categoriesImageSearch.grid(row = 0, column = 3, padx = (40,0),  sticky = 'e')

meals2_categoriesImageResize = meals2ImagePath.resize((250,250))
meals2_categoriesImageResized = ImageTk.PhotoImage(meals2_categoriesImageResize)
meals2_categoriesImageSearch = Label(mealsScrollbar, image=meals2_categoriesImageResized)
meals2_categoriesImageSearch.grid(row = 0, column = 4, padx = (40,0),  sticky = 'w')

meals3_categoriesImageResize = meals3ImagePath.resize((250,250))
meals3_categoriesImageResized = ImageTk.PhotoImage(meals3_categoriesImageResize)
meals3_categoriesImageSearch = Label(mealsScrollbar, image=meals3_categoriesImageResized)
meals3_categoriesImageSearch.grid(row = 0, column = 5, padx = (40,0),  sticky = 'e')

meals4_categoriesImageResize = meals4ImagePath.resize((250,250))
meals4_categoriesImageResized = ImageTk.PhotoImage(meals4_categoriesImageResize)
meals4_categoriesImageSearch = Label(mealsScrollbar, image=meals4_categoriesImageResized)
meals4_categoriesImageSearch.grid(row = 1, column = 2, padx = (200,0), pady = (30,0), sticky = 'w')

meals5_categoriesImageResize = meals5ImagePath.resize((250,250))
meals5_categoriesImageResized = ImageTk.PhotoImage(meals5_categoriesImageResize)
meals5_categoriesImageSearch = Label(mealsScrollbar, image=meals5_categoriesImageResized)
meals5_categoriesImageSearch.grid(row = 1, column = 3, padx = (40,0), pady = (30,0), sticky = 'e')

meals6_categoriesImageResize = meals6ImagePath.resize((250,250))
meals6_categoriesImageResized = ImageTk.PhotoImage(meals6_categoriesImageResize)
meals6_categoriesImageSearch = Label(mealsScrollbar, image=meals6_categoriesImageResized)
meals6_categoriesImageSearch.grid(row = 1, column = 4, padx = (40,0), pady = (30,0), sticky = 'w')

meals7_categoriesImageResize = meals7ImagePath.resize((250,250))
meals7_categoriesImageResized = ImageTk.PhotoImage(meals7_categoriesImageResize)
meals7_categoriesImageSearch = Label(mealsScrollbar, image=meals7_categoriesImageResized)
meals7_categoriesImageSearch.grid(row = 1, column = 5, padx = (40,0), pady = (30,0), sticky = 'e')

meals8_categoriesImageResize = meals8ImagePath.resize((250,250))
meals8_categoriesImageResized = ImageTk.PhotoImage(meals8_categoriesImageResize)
meals8_categoriesImageSearch = Label(mealsScrollbar, image=meals8_categoriesImageResized)
meals8_categoriesImageSearch.grid(row = 2, column = 2, padx = (200,0), pady = (30,0), sticky = 'w')

meals9_categoriesImageResize = meals9ImagePath.resize((250,250)) #480x270 #250x250
meals9_categoriesImageResized = ImageTk.PhotoImage(meals9_categoriesImageResize)
meals9_categoriesImageSearch = Label(mealsScrollbar, image=meals9_categoriesImageResized)
meals9_categoriesImageSearch.grid(row = 2, column = 3, padx = (40,0), pady = (30,0),  sticky = 'e')

meals10_categoriesImageResize = meals10ImagePath.resize((250,250)) #480x270
meals10_categoriesImageResized = ImageTk.PhotoImage(meals10_categoriesImageResize)
meals10_categoriesImageSearch = Label(mealsScrollbar, image=meals10_categoriesImageResized)
meals10_categoriesImageSearch.grid(row = 2, column = 4, padx = (40,0), pady = (30,0),  sticky = 'e')

meals11_categoriesImageResize = meals11ImagePath.resize((250,250)) #480x270
meals11_categoriesImageResized = ImageTk.PhotoImage(meals11_categoriesImageResize)
meals11_categoriesImageSearch = Label(mealsScrollbar, image=meals11_categoriesImageResized)
meals11_categoriesImageSearch.grid(row = 2, column = 5, padx = (40,0), pady = (30,0),  sticky = 'e')


# DRINKS WIDGETS

#drinks label
drinkslabelStore = Label(drinks_page, text="Drinks ")
drinkslabelStore.config(font=('Shrikhand', 40, 'bold', 'italic'))
drinkslabelStore.config(fg='#7d1418', bg='white')
drinkslabelStore.place(x=550, y=120)

#return button
back1Logo = Image.open("images/BACK BUTTON.png")
back1Image = ImageTk.PhotoImage(back1Logo)
back1Button = Button(drinks_page, text="Button", image=back1Image, bd=0,
                     highlightthickness=0, bg='white', command=lambda: categoriesFunction())
back1Button.place(x=150, y=100)

#DRINKS IMAGE PATHS
drinksImagePath = Image.open("CATEGORIES PICS/drinks_categories/1.png")
drinks1ImagePath = Image.open("CATEGORIES PICS/drinks_categories/2.png")
drinks2ImagePath = Image.open("CATEGORIES PICS/drinks_categories/3.png")
drinks3ImagePath = Image.open("CATEGORIES PICS/drinks_categories/4.png")
drinks4ImagePath = Image.open("CATEGORIES PICS/drinks_categories/5.png")
drinks5ImagePath = Image.open("CATEGORIES PICS/drinks_categories/6.png")
drinks6ImagePath = Image.open("CATEGORIES PICS/drinks_categories/7.png")
drinks7ImagePath = Image.open("CATEGORIES PICS/drinks_categories/8.png")
drinks8ImagePath = Image.open("CATEGORIES PICS/drinks_categories/9.png")
drinks9ImagePath = Image.open("CATEGORIES PICS/drinks_categories/10.png")
drinks10ImagePath = Image.open("CATEGORIES PICS/drinks_categories/11.png")
drinks11ImagePath = Image.open("CATEGORIES PICS/drinks_categories/12.png")
drinks12ImagePath = Image.open("CATEGORIES PICS/drinks_categories/13.png")

#drinks frame
drinksFrame = Frame(drinks_page, bg = 'white', width=1440, height = 650)
drinksFrame.place(x = 0, y = 190)

#drinks scrollbar
drinksScrollbar = ctk.CTkScrollableFrame(drinksFrame, width = 1440, height = 500, corner_radius = 0, fg_color='white')
drinksScrollbar.place(x = 0, y = 0, relwidth = 1, relheight = 1)

#display pictures of drinks
drinks_categoriesImageResize = drinksImagePath.resize((250,250))
drinks_categoriesImageResized = ImageTk.PhotoImage(drinks_categoriesImageResize)
drinks_categoriesImageSearch = Label(drinksScrollbar, image=drinks_categoriesImageResized)
drinks_categoriesImageSearch.grid(row = 0, column = 2, padx = (200,0),  sticky = 'e')

drinks1_categoriesImageResize = drinks1ImagePath.resize((250,250))
drinks1_categoriesImageResized = ImageTk.PhotoImage(drinks1_categoriesImageResize)
drinks1_categoriesImageSearch = Label(drinksScrollbar, image=drinks1_categoriesImageResized)
drinks1_categoriesImageSearch.grid(row = 0, column = 3, padx = (40,0),  sticky = 'e')

drinks2_categoriesImageResize = drinks2ImagePath.resize((250,250))
drinks2_categoriesImageResized = ImageTk.PhotoImage(drinks2_categoriesImageResize)
drinks2_categoriesImageSearch = Label(drinksScrollbar, image=drinks2_categoriesImageResized)
drinks2_categoriesImageSearch.grid(row = 0, column = 4, padx = (40,0),  sticky = 'e')

drinks3_categoriesImageResize = drinks3ImagePath.resize((250,250))
drinks3_categoriesImageResized = ImageTk.PhotoImage(drinks3_categoriesImageResize)
drinks3_categoriesImageSearch = Label(drinksScrollbar, image=drinks3_categoriesImageResized)
drinks3_categoriesImageSearch.grid(row = 0, column = 5, padx = (40,0),  sticky = 'e')

drinks4_categoriesImageResize = drinks4ImagePath.resize((250,250))
drinks4_categoriesImageResized = ImageTk.PhotoImage(drinks4_categoriesImageResize)
drinks4_categoriesImageSearch = Label(drinksScrollbar, image=drinks4_categoriesImageResized)
drinks4_categoriesImageSearch.grid(row = 1, column = 2, padx = (40,0), pady = (30,0),  sticky = 'e')

drinks5_categoriesImageResize = drinks5ImagePath.resize((250,250))
drinks5_categoriesImageResized = ImageTk.PhotoImage(drinks5_categoriesImageResize)
drinks5_categoriesImageSearch = Label(drinksScrollbar, image=drinks5_categoriesImageResized)
drinks5_categoriesImageSearch.grid(row = 1, column = 3, padx = (40,0), pady = (30,0),  sticky = 'e')

drinks6_categoriesImageResize = drinks6ImagePath.resize((250,250))
drinks6_categoriesImageResized = ImageTk.PhotoImage(drinks6_categoriesImageResize)
drinks6_categoriesImageSearch = Label(drinksScrollbar, image=drinks6_categoriesImageResized)
drinks6_categoriesImageSearch.grid(row = 1, column = 4, padx = (40,0), pady = (30,0),  sticky = 'e')

drinks7_categoriesImageResize = drinks7ImagePath.resize((250,250))
drinks7_categoriesImageResized = ImageTk.PhotoImage(drinks7_categoriesImageResize)
drinks7_categoriesImageSearch = Label(drinksScrollbar, image=drinks7_categoriesImageResized)
drinks7_categoriesImageSearch.grid(row = 1, column = 5, padx = (40,0), pady = (30,0),  sticky = 'e')


# SNACKS WIDGETS

#snacks label
snackslabelStore = Label(snacks_page, text="Snacks ")
snackslabelStore.config(font=('Shrikhand', 40, 'bold', 'italic'))
snackslabelStore.config(fg='#7d1418', bg='white')
snackslabelStore.place(x=550, y=120)

#return button
back2Logo = Image.open("images/BACK BUTTON.png")
back2Image = ImageTk.PhotoImage(back2Logo)
back2Button = Button(snacks_page, text="Button", image=back2Image, bd=0,
                     highlightthickness=0, bg='white', command=lambda: categoriesFunction())
back2Button.place(x=150, y=100)

#Snacks Image Paths
snacksImagePath = Image.open("CATEGORIES PICS/snacks_categories/1.png")
snacks1ImagePath = Image.open("CATEGORIES PICS/snacks_categories/2.png")
snacks2ImagePath = Image.open("CATEGORIES PICS/snacks_categories/3.png")
snacks3ImagePath = Image.open("CATEGORIES PICS/snacks_categories/4.png")
snacks4ImagePath = Image.open("CATEGORIES PICS/snacks_categories/5.png")
snacks5ImagePath = Image.open("CATEGORIES PICS/snacks_categories/6.png")
snacks6ImagePath = Image.open("CATEGORIES PICS/snacks_categories/7.png")
snacks7ImagePath = Image.open("CATEGORIES PICS/snacks_categories/8.png")
snacks8ImagePath = Image.open("CATEGORIES PICS/snacks_categories/9.png")
snacks9ImagePath = Image.open("CATEGORIES PICS/snacks_categories/10.png")
snacks10ImagePath = Image.open("CATEGORIES PICS/snacks_categories/11.png")
snacks11ImagePath = Image.open("CATEGORIES PICS/snacks_categories/12.png")
snacks12ImagePath = Image.open("CATEGORIES PICS/snacks_categories/13.png")
snacks13ImagePath = Image.open("CATEGORIES PICS/snacks_categories/14.png")
snacks14ImagePath = Image.open("CATEGORIES PICS/snacks_categories/15.png")
snacks15ImagePath = Image.open("CATEGORIES PICS/snacks_categories/16.png")
snacks16ImagePath = Image.open("CATEGORIES PICS/snacks_categories/17.png")
snacks17ImagePath = Image.open("CATEGORIES PICS/snacks_categories/18.png")
snacks18ImagePath = Image.open("CATEGORIES PICS/snacks_categories/19.png")
snacks19ImagePath = Image.open("CATEGORIES PICS/snacks_categories/20.png")
snacks20ImagePath = Image.open("CATEGORIES PICS/snacks_categories/21.png")
snacks21ImagePath = Image.open("CATEGORIES PICS/snacks_categories/22.png")
snacks22ImagePath = Image.open("CATEGORIES PICS/snacks_categories/23.png")
snacks23ImagePath = Image.open("CATEGORIES PICS/snacks_categories/24.png")
snacks24ImagePath = Image.open("CATEGORIES PICS/snacks_categories/25.png")
snacks25ImagePath = Image.open("CATEGORIES PICS/snacks_categories/26.png")
snacks26ImagePath = Image.open("CATEGORIES PICS/snacks_categories/27.png")
snacks27ImagePath = Image.open("CATEGORIES PICS/snacks_categories/28.png")
snacks28ImagePath = Image.open("CATEGORIES PICS/snacks_categories/29.png")
snacks29ImagePath = Image.open("CATEGORIES PICS/snacks_categories/30.png")
snacks30ImagePath = Image.open("CATEGORIES PICS/snacks_categories/31.png")

#snacks frame
snacksFrame = Frame(snacks_page, bg = 'white', width=1440, height = 650)
snacksFrame.place(x = 0, y = 190)

#snacks scrollbar
snacksScrollbar = ctk.CTkScrollableFrame(snacksFrame, width = 1440, height = 500, corner_radius = 0, fg_color='white')
snacksScrollbar.place(x = 0, y = 0, relwidth = 1, relheight = 1)

#display pictures of snacks
snacks_categoriesImageResize = snacksImagePath.resize((250,250))
snacks_categoriesImageResized = ImageTk.PhotoImage(snacks_categoriesImageResize)
snacks_categoriesImageSearch = Label(snacksScrollbar, image=snacks_categoriesImageResized)
snacks_categoriesImageSearch.grid(row = 0, column = 2, padx = (200,0),  sticky = 'e')

snacks1_categoriesImageResize = snacks1ImagePath.resize((250,250))
snacks1_categoriesImageResized = ImageTk.PhotoImage(snacks1_categoriesImageResize)
snacks1_categoriesImageSearch = Label(snacksScrollbar, image=snacks1_categoriesImageResized)
snacks1_categoriesImageSearch.grid(row = 0, column = 3, padx = (40,0),  sticky = 'e')

snacks2_categoriesImageResize = snacks2ImagePath.resize((250,250))
snacks2_categoriesImageResized = ImageTk.PhotoImage(snacks2_categoriesImageResize)
snacks2_categoriesImageSearch = Label(snacksScrollbar, image=snacks2_categoriesImageResized)
snacks2_categoriesImageSearch.grid(row = 0, column = 4, padx = (40,0),  sticky = 'e')

snacks3_categoriesImageResize = snacks3ImagePath.resize((250,250))
snacks3_categoriesImageResized = ImageTk.PhotoImage(snacks3_categoriesImageResize)
snacks3_categoriesImageSearch = Label(snacksScrollbar, image=snacks3_categoriesImageResized)
snacks3_categoriesImageSearch.grid(row = 0, column = 5, padx = (40,0),  sticky = 'e')

snacks4_categoriesImageResize = snacks4ImagePath.resize((250,250))
snacks4_categoriesImageResized = ImageTk.PhotoImage(snacks4_categoriesImageResize)
snacks4_categoriesImageSearch = Label(snacksScrollbar, image=snacks4_categoriesImageResized)
snacks4_categoriesImageSearch.grid(row = 1, column = 2, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks5_categoriesImageResize = snacks5ImagePath.resize((250,250))
snacks5_categoriesImageResized = ImageTk.PhotoImage(snacks5_categoriesImageResize)
snacks5_categoriesImageSearch = Label(snacksScrollbar, image=snacks5_categoriesImageResized)
snacks5_categoriesImageSearch.grid(row = 1, column = 3, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks6_categoriesImageResize = snacks6ImagePath.resize((250,250))
snacks6_categoriesImageResized = ImageTk.PhotoImage(snacks6_categoriesImageResize)
snacks6_categoriesImageSearch = Label(snacksScrollbar, image=snacks6_categoriesImageResized)
snacks6_categoriesImageSearch.grid(row = 1, column = 4, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks7_categoriesImageResize = snacks7ImagePath.resize((250,250))
snacks7_categoriesImageResized = ImageTk.PhotoImage(snacks7_categoriesImageResize)
snacks7_categoriesImageSearch = Label(snacksScrollbar, image=snacks7_categoriesImageResized)
snacks7_categoriesImageSearch.grid(row = 1, column = 5, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks8_categoriesImageResize = snacks8ImagePath.resize((250,250))
snacks8_categoriesImageResized = ImageTk.PhotoImage(snacks8_categoriesImageResize)
snacks8_categoriesImageSearch = Label(snacksScrollbar, image=snacks8_categoriesImageResized)
snacks8_categoriesImageSearch.grid(row = 2, column = 2, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks9_categoriesImageResize = snacks9ImagePath.resize((250,250))
snacks9_categoriesImageResized = ImageTk.PhotoImage(snacks9_categoriesImageResize)
snacks9_categoriesImageSearch = Label(snacksScrollbar, image=snacks9_categoriesImageResized)
snacks9_categoriesImageSearch.grid(row = 2, column = 3, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks10_categoriesImageResize = snacks10ImagePath.resize((250,250))
snacks10_categoriesImageResized = ImageTk.PhotoImage(snacks10_categoriesImageResize)
snacks10_categoriesImageSearch = Label(snacksScrollbar, image=snacks10_categoriesImageResized)
snacks10_categoriesImageSearch.grid(row = 2, column = 4, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks11_categoriesImageResize = snacks11ImagePath.resize((250,250))
snacks11_categoriesImageResized = ImageTk.PhotoImage(snacks11_categoriesImageResize)
snacks11_categoriesImageSearch = Label(snacksScrollbar, image=snacks11_categoriesImageResized)
snacks11_categoriesImageSearch.grid(row = 2, column = 5, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks12_categoriesImageResize = snacks12ImagePath.resize((250,250))
snacks12_categoriesImageResized = ImageTk.PhotoImage(snacks12_categoriesImageResize)
snacks12_categoriesImageSearch = Label(snacksScrollbar, image=snacks12_categoriesImageResized)
snacks12_categoriesImageSearch.grid(row = 3, column = 2, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks13_categoriesImageResize = snacks13ImagePath.resize((250,250))
snacks13_categoriesImageResized = ImageTk.PhotoImage(snacks13_categoriesImageResize)
snacks13_categoriesImageSearch = Label(snacksScrollbar, image=snacks13_categoriesImageResized)
snacks13_categoriesImageSearch.grid(row = 3, column = 3, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks14_categoriesImageResize = snacks14ImagePath.resize((250,250))
snacks14_categoriesImageResized = ImageTk.PhotoImage(snacks14_categoriesImageResize)
snacks14_categoriesImageSearch = Label(snacksScrollbar, image=snacks14_categoriesImageResized)
snacks14_categoriesImageSearch.grid(row = 3, column = 4, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks15_categoriesImageResize = snacks15ImagePath.resize((250,250))
snacks15_categoriesImageResized = ImageTk.PhotoImage(snacks15_categoriesImageResize)
snacks15_categoriesImageSearch = Label(snacksScrollbar, image=snacks15_categoriesImageResized)
snacks15_categoriesImageSearch.grid(row = 3, column = 5, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks16_categoriesImageResize = snacks16ImagePath.resize((250,250))
snacks16_categoriesImageResized = ImageTk.PhotoImage(snacks16_categoriesImageResize)
snacks16_categoriesImageSearch = Label(snacksScrollbar, image=snacks16_categoriesImageResized)
snacks16_categoriesImageSearch.grid(row = 4, column = 2, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks17_categoriesImageResize = snacks17ImagePath.resize((250,250))
snacks17_categoriesImageResized = ImageTk.PhotoImage(snacks17_categoriesImageResize)
snacks17_categoriesImageSearch = Label(snacksScrollbar, image=snacks17_categoriesImageResized)
snacks17_categoriesImageSearch.grid(row = 4, column = 3, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks18_categoriesImageResize = snacks18ImagePath.resize((250,250))
snacks18_categoriesImageResized = ImageTk.PhotoImage(snacks18_categoriesImageResize)
snacks18_categoriesImageSearch = Label(snacksScrollbar, image=snacks18_categoriesImageResized)
snacks18_categoriesImageSearch.grid(row = 4, column = 4, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks19_categoriesImageResize = snacks19ImagePath.resize((250,250))
snacks19_categoriesImageResized = ImageTk.PhotoImage(snacks19_categoriesImageResize)
snacks19_categoriesImageSearch = Label(snacksScrollbar, image=snacks19_categoriesImageResized)
snacks19_categoriesImageSearch.grid(row = 4, column = 5, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks20_categoriesImageResize = snacks20ImagePath.resize((250,250))
snacks20_categoriesImageResized = ImageTk.PhotoImage(snacks20_categoriesImageResize)
snacks20_categoriesImageSearch = Label(snacksScrollbar, image=snacks20_categoriesImageResized)
snacks20_categoriesImageSearch.grid(row = 5, column = 2, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks21_categoriesImageResize = snacks21ImagePath.resize((250,250))
snacks21_categoriesImageResized = ImageTk.PhotoImage(snacks21_categoriesImageResize)
snacks21_categoriesImageSearch = Label(snacksScrollbar, image=snacks21_categoriesImageResized)
snacks21_categoriesImageSearch.grid(row = 5, column = 3, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks22_categoriesImageResize = snacks22ImagePath.resize((250,250))
snacks22_categoriesImageResized = ImageTk.PhotoImage(snacks22_categoriesImageResize)
snacks22_categoriesImageSearch = Label(snacksScrollbar, image=snacks22_categoriesImageResized)
snacks22_categoriesImageSearch.grid(row = 5, column = 4, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks23_categoriesImageResize = snacks23ImagePath.resize((250,250))
snacks23_categoriesImageResized = ImageTk.PhotoImage(snacks23_categoriesImageResize)
snacks23_categoriesImageSearch = Label(snacksScrollbar, image=snacks23_categoriesImageResized)
snacks23_categoriesImageSearch.grid(row = 5, column = 5, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks24_categoriesImageResize = snacks24ImagePath.resize((250,250))
snacks24_categoriesImageResized = ImageTk.PhotoImage(snacks24_categoriesImageResize)
snacks24_categoriesImageSearch = Label(snacksScrollbar, image=snacks24_categoriesImageResized)
snacks24_categoriesImageSearch.grid(row = 6, column = 2, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks25_categoriesImageResize = snacks25ImagePath.resize((250,250))
snacks25_categoriesImageResized = ImageTk.PhotoImage(snacks25_categoriesImageResize)
snacks25_categoriesImageSearch = Label(snacksScrollbar, image=snacks25_categoriesImageResized)
snacks25_categoriesImageSearch.grid(row = 6, column = 3, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks26_categoriesImageResize = snacks26ImagePath.resize((250,250))
snacks26_categoriesImageResized = ImageTk.PhotoImage(snacks26_categoriesImageResize)
snacks26_categoriesImageSearch = Label(snacksScrollbar, image=snacks26_categoriesImageResized)
snacks26_categoriesImageSearch.grid(row = 6, column = 4, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks27_categoriesImageResize = snacks27ImagePath.resize((250,250))
snacks27_categoriesImageResized = ImageTk.PhotoImage(snacks27_categoriesImageResize)
snacks27_categoriesImageSearch = Label(snacksScrollbar, image=snacks27_categoriesImageResized)
snacks27_categoriesImageSearch.grid(row = 6, column = 5, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks28_categoriesImageResize = snacks28ImagePath.resize((250,250))
snacks28_categoriesImageResized = ImageTk.PhotoImage(snacks28_categoriesImageResize)
snacks28_categoriesImageSearch = Label(snacksScrollbar, image=snacks28_categoriesImageResized)
snacks28_categoriesImageSearch.grid(row = 7, column = 2, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks29_categoriesImageResize = snacks29ImagePath.resize((250,250))
snacks29_categoriesImageResized = ImageTk.PhotoImage(snacks29_categoriesImageResize)
snacks29_categoriesImageSearch = Label(snacksScrollbar, image=snacks29_categoriesImageResized)
snacks29_categoriesImageSearch.grid(row = 7, column = 3, padx = (40,0), pady = (30,0),  sticky = 'e')

snacks30_categoriesImageResize = snacks30ImagePath.resize((250,250))
snacks30_categoriesImageResized = ImageTk.PhotoImage(snacks30_categoriesImageResize)
snacks30_categoriesImageSearch = Label(snacksScrollbar, image=snacks30_categoriesImageResized)
snacks30_categoriesImageSearch.grid(row = 7, column = 4, padx = (40,0), pady = (30,0),  sticky = 'e')

# DESSERT WIDGETS

# dessert label
labelStore = Label(dessert_page, text="Dessert ")
labelStore.config(font=('Shrikhand', 40, 'bold', 'italic'))
labelStore.config(fg='#7d1418', bg='white')
labelStore.place(x=550, y=120)

#return button
back4Logo = Image.open("images/BACK BUTTON.png")
back4Image = ImageTk.PhotoImage(back4Logo)
back4Button = Button(dessert_page, text="Button", image=back4Image, bd=0,
                     highlightthickness=0, bg='white', command=lambda: categoriesFunction())
back4Button.place(x=150, y=100)

#dessert image paths
dessertImagePath = Image.open("CATEGORIES PICS/dessert2_categories/1.png")
dessert1ImagePath = Image.open("CATEGORIES PICS/dessert2_categories/2.png")
dessert2ImagePath = Image.open("CATEGORIES PICS/dessert2_categories/3.png")
dessert3ImagePath = Image.open("CATEGORIES PICS/dessert2_categories/4.png")
dessert4ImagePath = Image.open("CATEGORIES PICS/dessert2_categories/5.png")
dessert5ImagePath = Image.open("CATEGORIES PICS/dessert2_categories/6.png")

#dessert frame
dessertFrame = Frame(dessert_page, bg = 'white', width=1440, height = 610)
dessertFrame.place(x = 0, y = 190)

#dessert scrollbar
dessertScrollbar = ctk.CTkScrollableFrame(dessertFrame, width = 1440, height = 500, corner_radius = 0, fg_color='white')
dessertScrollbar.place(x = 0, y = 0, relwidth = 1, relheight = 1)

#display pictures of dessert
dessert_categoriesImageResize = dessertImagePath.resize((250,250)) #480x270
dessert_categoriesImageResized = ImageTk.PhotoImage(dessert_categoriesImageResize)
dessert_categoriesImageSearch = Label(dessertScrollbar, image=dessert_categoriesImageResized)
dessert_categoriesImageSearch.grid(row = 0, column = 2, padx = (200,0), pady = (30,0), sticky = 'e')

dessert1_categoriesImageResize = dessert1ImagePath.resize((250,250))
dessert1_categoriesImageResized = ImageTk.PhotoImage(dessert1_categoriesImageResize)
dessert1_categoriesImageSearch = Label(dessertScrollbar, image=dessert1_categoriesImageResized)
dessert1_categoriesImageSearch.grid(row = 0, column = 3, padx = (40,0), pady = (30,0),  sticky = 'e')

dessert2_categoriesImageResize = dessert2ImagePath.resize((250,250))
dessert2_categoriesImageResized = ImageTk.PhotoImage(dessert2_categoriesImageResize)
dessert2_categoriesImageSearch = Label(dessertScrollbar, image=dessert2_categoriesImageResized)
dessert2_categoriesImageSearch.grid(row = 0, column = 4, padx = (40,0), pady = (30,0),  sticky = 'e')

dessert3_categoriesImageResize = dessert3ImagePath.resize((250,250))
dessert3_categoriesImageResized = ImageTk.PhotoImage(dessert3_categoriesImageResize)
dessert3_categoriesImageSearch = Label(dessertScrollbar, image=dessert3_categoriesImageResized)
dessert3_categoriesImageSearch.grid(row = 0, column = 5, padx = (40,0), pady = (30,0),  sticky = 'e')  

dessert4_categoriesImageResize = dessert4ImagePath.resize((250,250))
dessert4_categoriesImageResized = ImageTk.PhotoImage(dessert4_categoriesImageResize)
dessert4_categoriesImageSearch = Label(dessertScrollbar, image=dessert4_categoriesImageResized)
dessert4_categoriesImageSearch.grid(row = 1, column = 2, padx = (200,0), pady = (30,0),  sticky = 'w')

dessert5_categoriesImageResize = dessert5ImagePath.resize((250,250))
dessert5_categoriesImageResized = ImageTk.PhotoImage(dessert5_categoriesImageResize)
dessert5_categoriesImageSearch = Label(dessertScrollbar, image=dessert5_categoriesImageResized)
dessert5_categoriesImageSearch.grid(row = 1, column = 3, padx = (40,0), pady = (30,0),  sticky = 'e')


# STORE PAGE WIDGET

#stores label
labelStore = Label(store_page, text="Stores ")
labelStore.config(font=('Shrikhand', 40, 'bold', 'italic'))
labelStore.config(fg='#7d1418', bg='white')
labelStore.place(x=620, y=120)

#cuadro de j button
cdjCategory = Image.open("images/CUADRO DE J.png")
cdjButton = ImageTk.PhotoImage(cdjCategory)
cdjPicture = Button(store_page, text="Button", image=cdjButton, bd=0,
                    highlightthickness=0, bg='white', command=lambda: cuadroFunction())
cdjPicture.place(x=70, y=230)

#cuadro de j rating
cdjRate = Image.open("images/RAtING STARS/1.png")
cdjRating = ImageTk.PhotoImage(cdjRate)
cdjRateStar = Label(store_page, image=cdjRating, bd=0,
                    highlightthickness=0, bg='white', )
cdjRateStar.place(x=110, y=550)

#david's wing button
dwCategory = Image.open("images/DAVIDS WINGS.png")
dwButton = ImageTk.PhotoImage(dwCategory)
dwPicture = Button(store_page, text="Button", image=dwButton, bd=0,
                   highlightthickness=0, bg='white', command=lambda: davidFunction())
dwPicture.place(x=340, y=230)

#david's wing rating
dwRate = Image.open("images/RAtING STARS/2.png")
dwRating = ImageTk.PhotoImage(dwRate)
dwRateStar = Label(store_page, image=dwRating, bd=0,
                    highlightthickness=0, bg='white', )
dwRateStar.place(x=380, y=550)


#koficcino button
koffiCategory = Image.open("images/KOFICCINO.png")
koffiButton = ImageTk.PhotoImage(koffiCategory)
koffiPicture = Button(store_page, text="Button", image=koffiButton, bd=0,
                      highlightthickness=0, bg='white', command=lambda: koffiFunction())
koffiPicture.place(x=610, y=230)

#koficcino rating
koffiRate = Image.open("images/RAtING STARS/3.png")
koffiRating = ImageTk.PhotoImage(koffiRate)
koffiRateStar = Label(store_page, image=koffiRating, bd=0,
                    highlightthickness=0, bg='white', )
koffiRateStar.place(x=650, y=550)

#waffle time button
waffleCategory = Image.open("images/WAFFLE TIME.png")
waffleButton = ImageTk.PhotoImage(waffleCategory)
wafflePicture = Button(store_page, text="Button", image=waffleButton, bd=0,
                       highlightthickness=0, bg='white', command=lambda: waffleFunction())
wafflePicture.place(x=880, y=230)

#waffle time rating
waffleRate = Image.open("images/RAtING STARS/4.png")
waffleRating = ImageTk.PhotoImage(waffleRate)
waffleRateStar = Label(store_page, image=waffleRating, bd=0,
                    highlightthickness=0, bg='white', )
waffleRateStar.place(x=930, y=550)

#yummy burgers button
yummyCategory = Image.open("images/YUMMY BURGERS.png")
yummyButton = ImageTk.PhotoImage(yummyCategory)
yummyPicture = Button(store_page, text="Button", image=yummyButton, bd=0,
                      highlightthickness=0, bg='white', command=lambda: yummybFunction())
yummyPicture.place(x=1150, y=230)

#yummy burgers rating
yummyRate = Image.open("images/RAtING STARS/4.png")
yummyRating = ImageTk.PhotoImage(yummyRate)
yummyRateStar = Label(store_page, image=yummyRating, bd=0,
                    highlightthickness=0, bg='white', )
yummyRateStar.place(x=1190, y=550)

# SEARCH WIDGETS
searchFrame = Frame(search_page, height=40, width=1125)
searchFrame.config(bg='#7d1418')
searchFrame.place(x=185, y=100)

#search entry
search_entry = ctk.CTkEntry(searchFrame, font=('Shrikhand', 14), width=1115, height=20, placeholder_text='Search')
search_entry.place(x=6, y=7)

#enter button bind
window.bind('<Return>', lambda e: userSearching())

#search frame
searchFrame = Frame(search_page, bg='white', width=1440, height=700)
searchFrame.place(x=0, y=157)

#search scrollbar
searchScrollbar = ctk.CTkScrollableFrame(searchFrame, width=1440, height=500, corner_radius=0, fg_color='white')
searchScrollbar.place(x=0, y=0, relwidth=1, relheight=1)

#SEARCH FILTER WIDGETS
filter = Label(search_page, text="Sort by: ")
filter.config(font=('Shrikhand', 25, 'bold'))
filter.config(fg='#7d1418', bg='white')
filter.place(x=30, y=180)

filter1 = Label(search_page, text="PRICE: ")
filter1.config(font=('Shrikhand', 25, 'bold'))
filter1.config(fg='#7d1418', bg='white')
filter1.place(x=30, y=250)

filterLHPrice = ctk.CTkButton(master = search_page, text = 'low - high', 
                            bg_color = '#7d1418', fg_color = '#7d1418', command = lambda: searchFilterLH())
filterLHPrice.place(x=30, y=300)

filterHLPrice = ctk.CTkButton(master = search_page, text = 'high - low', 
                            bg_color = '#7d1418', fg_color = '#7d1418', command = lambda: searchFilterHL())
filterHLPrice.place(x=30, y=330)

#ADD TO CART LUNCHBOX BUTTON
lunchboxImagePath = Image.open("images/lunchbox.png")
addtoCartImageResize = lunchboxImagePath.resize((50,50))
addtoCartImageResized = ImageTk.PhotoImage(addtoCartImageResize)
addtoCartImageSearch = Button(master = search_page, image=addtoCartImageResized, command = lambda: addtoCartFunction())
addtoCartImageSearch.place(x=30, y=700)

#add to cart frame
cartpageFrame = Frame(cart_page, bg = 'white', width=1440, height = 700)
cartpageFrame.place(x=0, y=157)

#add to cart scrollbar
cartpageScrollbar = ctk.CTkScrollableFrame(cartpageFrame, width = 1440, height = 500, corner_radius = 0, fg_color='white')
cartpageScrollbar.place(x = 0, y = 50)

#CART TOTAL
totalPrice = Label(cart_page, text="TOTAL: ")
totalPrice.config(font=('Shrikhand', 40, 'bold'), fg='#7d1418', bg='white')
totalPrice.place(x=500, y=100)

#DISPLAY OF TOTAL
o = ctk.CTkEntry(cart_page, font=('Shrikhand', 100), width=700, height=150)
o.place(x=500, y=180)

#CLEAR BUTTON
clearCartB = Button(cart_page, text="Clear", bd=0, font=('Shrikhand', 40, 'bold'),
                       highlightthickness=0, bg='#7d1418', command=lambda: cartClear())
clearCartB.place(x=1200, y=190)

#BACK BUTTON
back3Logo = Image.open("images/BACK BUTTON.png")
back3Image = ImageTk.PhotoImage(back3Logo)
back3Button = Button(cart_page, text="Button", image=back3Image, bd=0,
                     highlightthickness=0, bg='white', command=lambda: searchFunction())
back3Button.place(x=150, y=100)

#SEARCH FOOD IMAGE FILE PATHS
mealsImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/Meals_categories lunchbox/1.png")
meals1ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/Meals_categories lunchbox/2.png")
meals2ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/Meals_categories lunchbox/3.png")
meals3ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/Meals_categories lunchbox/4.png")
meals4ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/Meals_categories lunchbox/5.png")
meals5ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/Meals_categories lunchbox/6.png")
meals6ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/Meals_categories lunchbox/7.png")
meals7ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/Meals_categories lunchbox/8.png")
meals8ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/Meals_categories lunchbox/9.png")
meals9ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/Meals2_categories lunchbox/1.png")
meals10ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/Meals2_categories lunchbox/2.png")
meals11ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/Meals2_categories lunchbox/3.png")

drinksImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/drinks_categories lunchbox/1.png")
drinks1ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/drinks_categories lunchbox/2.png")
drinks2ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/drinks_categories lunchbox/3.png")
drinks3ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/drinks_categories lunchbox/4.png")
drinks4ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/drinks_categories lunchbox/5.png")
drinks5ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/drinks_categories lunchbox/6.png")
drinks6ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/drinks_categories lunchbox/7.png")
drinks7ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/drinks_categories lunchbox/8.png")
drinks8ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/drinks_categories lunchbox/9.png")
drinks9ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/drinks_categories lunchbox/10.png")
drinks10ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/drinks_categories lunchbox/11.png")
drinks11ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/drinks_categories lunchbox/12.png")
drinks12ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/drinks_categories lunchbox/13.png")

snacksImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/1.png")
snacks1ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/2.png")
snacks2ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/3.png")
snacks3ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/4.png")
snacks4ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/5.png")
snacks5ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/6.png")
snacks6ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/7.png")
snacks7ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/8.png")
snacks8ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/9.png")
snacks9ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/10.png")
snacks10ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/11.png")
snacks11ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/12.png")
snacks12ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/13.png")
snacks13ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/14.png")
snacks14ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/15.png")
snacks15ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/16.png")
snacks16ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/17.png")
snacks17ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/18.png")
snacks18ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/19.png")
snacks19ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/20.png")
snacks20ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/21.png")
snacks21ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/22.png")
snacks22ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/23.png")
snacks23ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/24.png")
snacks24ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/25.png")
snacks25ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/26.png")
snacks26ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/27.png")
snacks27ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/28.png")
snacks28ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/29.png")
snacks29ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/30.png")
snacks30ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/snacks_categories lunchbox/31.png")

dessertImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/dessert_categories lunchbox/1.png")
dessert1ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/dessert_categories lunchbox/2.png")
dessert2ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/dessert_categories lunchbox/3.png")
dessert3ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/dessert_categories lunchbox/4.png")
dessert4ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/dessert2_categories lunchbox/1.png")
dessert5ImagePathbox = Image.open("CATEGORIES PICS LUNCHBOX/dessert2_categories lunchbox/2.png")


# SEARCH FOOD IMAGE DISPLAY
mealsImageResize = mealsImagePathbox.resize((250, 250))
mealsImageResized = ImageTk.PhotoImage(mealsImageResize)
mealsImageSearch = Button(searchScrollbar, image=mealsImageResized, command=lambda: order_click(70, "mealsImageSearch"))


meals1ImageResize = meals1ImagePathbox.resize((250, 250))
meals1ImageResized = ImageTk.PhotoImage(meals1ImageResize)
meals1ImageSearch = Button(searchScrollbar, image=meals1ImageResized, command=lambda: order_click(70, "meals1ImageSearch"))


meals2ImageResize = meals2ImagePathbox.resize((250, 250))
meals2ImageResized = ImageTk.PhotoImage(meals2ImageResize)
meals2ImageSearch = Button(searchScrollbar, image=meals2ImageResized, command=lambda: order_click(70, "meals2ImageSearch"))


meals3ImageResize = meals3ImagePathbox.resize((250, 250))
meals3ImageResized = ImageTk.PhotoImage(meals3ImageResize)
meals3ImageSearch = Button(searchScrollbar, image=meals3ImageResized, command=lambda: order_click(70, "meals3ImageSearch"))


meals4ImageResize = meals4ImagePathbox.resize((250, 250))
meals4ImageResized = ImageTk.PhotoImage(meals4ImageResize)
meals4ImageSearch = Button(searchScrollbar, image=meals4ImageResized, command=lambda: order_click(70, "meals4ImageSearch"))


meals5ImageResize = meals5ImagePathbox.resize((250, 250))
meals5ImageResized = ImageTk.PhotoImage(meals5ImageResize)
meals5ImageSearch = Button(searchScrollbar, image=meals5ImageResized, command=lambda: order_click(70, "meals5ImageSearch"))


meals6ImageResize = meals6ImagePathbox.resize((250, 250))
meals6ImageResized = ImageTk.PhotoImage(meals6ImageResize)
meals6ImageSearch = Button(searchScrollbar, image=meals6ImageResized, command=lambda: order_click(80, "meals6ImageSearch"))


meals7ImageResize = meals7ImagePathbox.resize((250, 250))
meals7ImageResized = ImageTk.PhotoImage(meals7ImageResize)
meals7ImageSearch = Button(searchScrollbar, image=meals7ImageResized, command=lambda: order_click(80, "meals7ImageSearch"))


meals8ImageResize = meals8ImagePathbox.resize((250, 250))
meals8ImageResized = ImageTk.PhotoImage(meals8ImageResize)
meals8ImageSearch = Button(searchScrollbar, image=meals8ImageResized, command=lambda: order_click(80, "meals8ImageSearch"))


snacksImageResize = snacksImagePathbox.resize((250, 250))
snacksImageResized = ImageTk.PhotoImage(snacksImageResize)
snacksImageSearch = Button(searchScrollbar, image=snacksImageResized, command=lambda: order_click(34, "snacksImageSearch"))


snacks1ImageResize = snacks1ImagePathbox.resize((250, 250))
snacks1ImageResized = ImageTk.PhotoImage(snacks1ImageResize)
snacks1ImageSearch = Button(searchScrollbar, image=snacks1ImageResized, command=lambda: order_click(31, "snacks1ImageSearch"))


snacks2ImageResize = snacks2ImagePathbox.resize((250, 250))
snacks2ImageResized = ImageTk.PhotoImage(snacks2ImageResize)
snacks2ImageSearch = Button(searchScrollbar, image=snacks2ImageResized, command=lambda: order_click(26, "snacks2ImageSearch"))


snacks3ImageResize = snacks3ImagePathbox.resize((250, 250))
snacks3ImageResized = ImageTk.PhotoImage(snacks3ImageResize)
snacks3ImageSearch = Button(searchScrollbar, image=snacks3ImageResized, command=lambda: order_click(32, "snacks3ImageSearch"))


snacks4ImageResize = snacks4ImagePathbox.resize((250, 250))
snacks4ImageResized = ImageTk.PhotoImage(snacks4ImageResize)
snacks4ImageSearch = Button(searchScrollbar, image=snacks4ImageResized, command=lambda: order_click(24, "snacks4ImageSearch"))


snacks5ImageResize = snacks5ImagePathbox.resize((250, 250))
snacks5ImageResized = ImageTk.PhotoImage(snacks5ImageResize)
snacks5ImageSearch = Button(searchScrollbar, image=snacks5ImageResized, command=lambda: order_click(30, "snacks5ImageSearch"))


snacks6ImageResize = snacks6ImagePathbox.resize((250, 250))
snacks6ImageResized = ImageTk.PhotoImage(snacks6ImageResize)
snacks6ImageSearch = Button(searchScrollbar, image=snacks6ImageResized, command=lambda: order_click(35, "snacks6ImageSearch"))


snacks7ImageResize = snacks7ImagePathbox.resize((250, 250))
snacks7ImageResized = ImageTk.PhotoImage(snacks7ImageResize)
snacks7ImageSearch = Button(searchScrollbar, image=snacks7ImageResized, command=lambda: order_click(32, "snacks7ImageSearch"))


snacks8ImageResize = snacks8ImagePathbox.resize((250, 250))
snacks8ImageResized = ImageTk.PhotoImage(snacks8ImageResize)
snacks8ImageSearch = Button(searchScrollbar, image=snacks8ImageResized, command=lambda: order_click(35, "snacks8ImageSearch"))


snacks9ImageResize = snacks9ImagePathbox.resize((250, 250))
snacks9ImageResized = ImageTk.PhotoImage(snacks9ImageResize)
snacks9ImageSearch = Button(searchScrollbar, image=snacks9ImageResized, command=lambda: order_click(34, "snacks9ImageSearch"))


snacks10ImageResize = snacks10ImagePathbox.resize((250, 250))
snacks10ImageResized = ImageTk.PhotoImage(snacks10ImageResize)
snacks10ImageSearch = Button(searchScrollbar, image=snacks10ImageResized, command=lambda: order_click(32, "snacks10ImageSearch"))


snacks11ImageResize = snacks11ImagePathbox.resize((250, 250))
snacks11ImageResized = ImageTk.PhotoImage(snacks11ImageResize)
snacks11ImageSearch = Button(searchScrollbar, image=snacks11ImageResized, command=lambda: order_click(26, "snacks11ImageSearch"))


snacks12ImageResize = snacks12ImagePathbox.resize((250, 250))
snacks12ImageResized = ImageTk.PhotoImage(snacks12ImageResize)
snacks12ImageSearch = Button(searchScrollbar, image=snacks12ImageResized, command=lambda: order_click(23, "snacks12ImageSearch"))


snacks13ImageResize = snacks13ImagePathbox.resize((250, 250))
snacks13ImageResized = ImageTk.PhotoImage(snacks13ImageResize)
snacks13ImageSearch = Button(searchScrollbar, image=snacks13ImageResized, command=lambda: order_click(40, "snacks13ImageSearch"))


snacks14ImageResize = snacks14ImagePathbox.resize((250, 250))
snacks14ImageResized = ImageTk.PhotoImage(snacks14ImageResize)
snacks14ImageSearch = Button(searchScrollbar, image=snacks14ImageResized, command=lambda: order_click(40, "snacks14ImageSearch"))


snacks15ImageResize = snacks15ImagePathbox.resize((250, 250))
snacks15ImageResized = ImageTk.PhotoImage(snacks15ImageResize)
snacks15ImageSearch = Button(searchScrollbar, image=snacks15ImageResized, command=lambda: order_click(75, "snacks15ImageSearch"))


snacks16ImageResize = snacks16ImagePathbox.resize((250, 250))
snacks16ImageResized = ImageTk.PhotoImage(snacks16ImageResize)
snacks16ImageSearch = Button(searchScrollbar, image=snacks16ImageResized, command=lambda: order_click(35, "snacks16ImageSearch"))


snacks17ImageResize = snacks17ImagePathbox.resize((250, 250))
snacks17ImageResized = ImageTk.PhotoImage(snacks17ImageResize)
snacks17ImageSearch = Button(searchScrollbar, image=snacks17ImageResized, command=lambda: order_click(60, "snacks17ImageSearch"))


snacks18ImageResize = snacks18ImagePathbox.resize((250, 250))
snacks18ImageResized = ImageTk.PhotoImage(snacks18ImageResize)
snacks18ImageSearch = Button(searchScrollbar, image=snacks18ImageResized, command=lambda: order_click(30, "snacks18ImageSearch"))


snacks19ImageResize = snacks19ImagePathbox.resize((250, 250))
snacks19ImageResized = ImageTk.PhotoImage(snacks19ImageResize)
snacks19ImageSearch = Button(searchScrollbar, image=snacks19ImageResized, command=lambda: order_click(60, "snacks19ImageSearch"))


snacks20ImageResize = snacks20ImagePathbox.resize((250, 250))
snacks20ImageResized = ImageTk.PhotoImage(snacks20ImageResize)
snacks20ImageSearch = Button(searchScrollbar, image=snacks20ImageResized, command=lambda: order_click(80, "snacks20ImageSearch"))


snacks21ImageResize = snacks21ImagePathbox.resize((250, 250))
snacks21ImageResized = ImageTk.PhotoImage(snacks21ImageResize)
snacks21ImageSearch = Button(searchScrollbar, image=snacks21ImageResized, command=lambda: order_click(45, "snacks21ImageSearch"))


snacks22ImageResize = snacks22ImagePathbox.resize((250, 250))
snacks22ImageResized = ImageTk.PhotoImage(snacks22ImageResize)
snacks22ImageSearch = Button(searchScrollbar, image=snacks22ImageResized, command=lambda: order_click(23, "snacks22ImageSearch"))


snacks23ImageResize = snacks23ImagePathbox.resize((250, 250))
snacks23ImageResized = ImageTk.PhotoImage(snacks23ImageResize)
snacks23ImageSearch = Button(searchScrollbar, image=snacks23ImageResized, command=lambda: order_click(40, "snacks23ImageSearch"))


snacks24ImageResize = snacks24ImagePathbox.resize((250, 250))
snacks24ImageResized = ImageTk.PhotoImage(snacks24ImageResize)
snacks24ImageSearch = Button(searchScrollbar, image=snacks24ImageResized, command=lambda: order_click(23, "snacks24ImageSearch"))


snacks25ImageResize = snacks25ImagePathbox.resize((250, 250))
snacks25ImageResized = ImageTk.PhotoImage(snacks25ImageResize)
snacks25ImageSearch = Button(searchScrollbar, image=snacks25ImageResized, command=lambda: order_click(40, "snacks25ImageSearch"))


snacks26ImageResize = snacks26ImagePathbox.resize((250, 250))
snacks26ImageResized = ImageTk.PhotoImage(snacks26ImageResize)
snacks26ImageSearch = Button(searchScrollbar, image=snacks26ImageResized, command=lambda: order_click(20, "snacks26ImageSearch"))


snacks27ImageResize = snacks27ImagePathbox.resize((250, 250))
snacks27ImageResized = ImageTk.PhotoImage(snacks27ImageResize)
snacks27ImageSearch = Button(searchScrollbar, image=snacks27ImageResized, command=lambda: order_click(40, "snacks27ImageSearch"))


snacks28ImageResize = snacks28ImagePathbox.resize((250, 250))
snacks28ImageResized = ImageTk.PhotoImage(snacks28ImageResize)
snacks28ImageSearch = Button(searchScrollbar, image=snacks28ImageResized, command=lambda: order_click(48, "snacks28ImageSearch"))


snacks29ImageResize = snacks29ImagePathbox.resize((250, 250))
snacks29ImageResized = ImageTk.PhotoImage(snacks29ImageResize)
snacks29ImageSearch = Button(searchScrollbar, image=snacks29ImageResized, command=lambda: order_click(112, "snacks29ImageSearch"))


snacks30ImageResize = snacks30ImagePathbox.resize((250, 250))
snacks30ImageResized = ImageTk.PhotoImage(snacks30ImageResize)
snacks30ImageSearch = Button(searchScrollbar, image=snacks30ImageResized, command=lambda: order_click(72, "snacks30ImageSearch"))


drinksImageResize = drinksImagePathbox.resize((250, 250))
drinksImageResized = ImageTk.PhotoImage(drinksImageResize)
drinksImageSearch = Button(searchScrollbar, image=drinksImageResized, command=lambda: order_click(39, "drinksImageSearch"))

drinks1ImageResize = drinks1ImagePathbox.resize((250, 250))
drinks1ImageResized = ImageTk.PhotoImage(drinks1ImageResize)
drinks1ImageSearch = Button(searchScrollbar, image=drinks1ImageResized, command=lambda: order_click(49, "drinks1ImageSearch"))


drinks2ImageResize = drinks2ImagePathbox.resize((250, 250))
drinks2ImageResized = ImageTk.PhotoImage(drinks2ImageResize)
drinks2ImageSearch = Button(searchScrollbar, image=drinks2ImageResized, command=lambda: order_click(39, "drinks2ImageSearch"))


drinks3ImageResize = drinks3ImagePathbox.resize((250, 250))
drinks3ImageResized = ImageTk.PhotoImage(drinks3ImageResize)
drinks3ImageSearch = Button(searchScrollbar, image=drinks3ImageResized, command=lambda: order_click(49, "drinks3ImageSearch"))


drinks4ImageResize = drinks4ImagePathbox.resize((250, 250))
drinks4ImageResized = ImageTk.PhotoImage(drinks4ImageResize)
drinks4ImageSearch = Button(searchScrollbar, image=drinks4ImageResized, command=lambda: order_click(39, "drinks4ImageSearch"))


drinks5ImageResize = drinks5ImagePathbox.resize((250, 250))
drinks5ImageResized = ImageTk.PhotoImage(drinks5ImageResize)
drinks5ImageSearch = Button(searchScrollbar, image=drinks5ImageResized, command=lambda: order_click(49, "drinks5ImageSearch"))


drinks6ImageResize = drinks6ImagePathbox.resize((250, 250))
drinks6ImageResized = ImageTk.PhotoImage(drinks6ImageResize)
drinks6ImageSearch = Button(searchScrollbar, image=drinks6ImageResized, command=lambda: order_click(39, "drinks6ImageSearch"))


drinks7ImageResize = drinks7ImagePathbox.resize((250, 250))
drinks7ImageResized = ImageTk.PhotoImage(drinks7ImageResize)
drinks7ImageSearch = Button(searchScrollbar, image=drinks7ImageResized, command=lambda: order_click(49, "drinks7ImageSearch"))


drinks8ImageResize = drinks8ImagePathbox.resize((250, 250))
drinks8ImageResized = ImageTk.PhotoImage(drinks8ImageResize)
drinks8ImageSearch = Button(searchScrollbar, image=drinks8ImageResized, command=lambda: order_click(59, "drinks8ImageSearch"))


drinks9ImageResize = drinks9ImagePathbox.resize((250, 250))
drinks9ImageResized = ImageTk.PhotoImage(drinks9ImageResize)
drinks9ImageSearch = Button(searchScrollbar, image=drinks9ImageResized, command=lambda: order_click(69, "drinks9ImageSearch"))


drinks10ImageResize = drinks10ImagePathbox.resize((250, 250))
drinks10ImageResized = ImageTk.PhotoImage(drinks10ImageResize)
drinks10ImageSearch = Button(searchScrollbar, image=drinks10ImageResized, command=lambda: order_click(48, "drinks10ImageSearch"))


drinks11ImageResize = drinks11ImagePathbox.resize((250, 250))
drinks11ImageResized = ImageTk.PhotoImage(drinks11ImageResize)
drinks11ImageSearch = Button(searchScrollbar, image=drinks11ImageResized, command=lambda: order_click(48, "drinks11ImageSearch"))


drinks12ImageResize = drinks12ImagePathbox.resize((250, 250))
drinks12ImageResized = ImageTk.PhotoImage(drinks12ImageResize)
drinks12ImageSearch = Button(searchScrollbar, image=drinks12ImageResized, command=lambda: order_click(48, "drinks12ImageSearch"))


dessertImageResize = dessertImagePathbox.resize((250,250)) #480x270
dessertImageResized = ImageTk.PhotoImage(dessertImageResize)
dessertImageSearch = Button(searchScrollbar, image=dessertImageResized, command=lambda: order_click(39, "dessertImageSearch"))


dessert1ImageResize = dessert1ImagePathbox.resize((250,250))
dessert1ImageResized = ImageTk.PhotoImage(dessert1ImageResize)
dessert1ImageSearch = Button(searchScrollbar, image=dessert1ImageResized, command=lambda: order_click(59, "dessert1ImageSearch"))


dessert2ImageResize = dessert2ImagePathbox.resize((250,250))
dessert2ImageResized = ImageTk.PhotoImage(dessert2ImageResize)
dessert2ImageSearch = Button(searchScrollbar, image=dessert2ImageResized, command=lambda: order_click(79, "dessert2ImageSearch"))


dessert3ImageResize = dessert3ImagePathbox.resize((250,250))
dessert3ImageResized = ImageTk.PhotoImage(dessert3ImageResize)
dessert3ImageSearch = Button(searchScrollbar, image=dessert3ImageResized, command=lambda: order_click(99, "dessert3ImageSearch"))


meals9ImageResize = meals9ImagePathbox.resize((250,250)) #480x270 #520x310
meals9ImageResized = ImageTk.PhotoImage(meals9ImageResize)
meals9ImageSearch = Button(searchScrollbar, image=meals9ImageResized, command=lambda: order_click(70, "meals9ImageSearch"))


meals10ImageResize = meals10ImagePathbox.resize((250,250)) #480x270
meals10ImageResized = ImageTk.PhotoImage(meals10ImageResize)
meals10ImageSearch = Button(searchScrollbar, image=meals10ImageResized, command=lambda: order_click(75, "meals10ImageSearch"))


meals11ImageResize = meals11ImagePathbox.resize((250,250)) #480x270
meals11ImageResized = ImageTk.PhotoImage(meals11ImageResize)
meals11ImageSearch = Button(searchScrollbar, image=meals11ImageResized, command=lambda: order_click(335, "meals11ImageSearch"))


dessert4ImageResize = dessert4ImagePathbox.resize((250,250))
dessert4ImageResized = ImageTk.PhotoImage(dessert4ImageResize)
dessert4ImageSearch = Button(searchScrollbar, image=dessert4ImageResized, command=lambda: order_click(29, "dessert4ImageSearch"))


dessert5ImageResize = dessert5ImagePathbox.resize((250,250))
dessert5ImageResized = ImageTk.PhotoImage(dessert5ImageResize)
dessert5ImageSearch = Button(searchScrollbar, image=dessert5ImageResized, command=lambda: order_click(39, "dessert5ImageSearch"))


mealsImageSearch.grid(row=0, column=2, padx=(200, 0), sticky='w')
meals1ImageSearch.grid(row=0, column=3, padx=(40, 0), sticky='e')
meals2ImageSearch.grid(row=0, column=4, padx=(40, 0), sticky='w')
meals3ImageSearch.grid(row=0, column=5, padx=(40, 0), sticky='e')

meals4ImageSearch.grid(row=1, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
meals5ImageSearch.grid(row=1, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
meals6ImageSearch.grid(row=1, column=3, padx=(40, 0), pady=(30, 0), sticky='w')
meals7ImageSearch.grid(row=1, column=3, padx=(40, 0), pady=(30, 0), sticky='e')

meals8ImageSearch.grid(row=2, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
snacksImageSearch.grid(row=2, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
snacks1ImageSearch.grid(row=2, column=3, padx=(40, 0), pady=(30, 0), sticky='w')
snacks2ImageSearch.grid(row=2, column=3, padx=(40, 0), pady=(30, 0), sticky='e')

snacks3ImageSearch.grid(row=3, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
snacks4ImageSearch.grid(row=3, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
snacks5ImageSearch.grid(row=3, column=3, padx=(40, 0), pady=(30, 0), sticky='w')
snacks6ImageSearch.grid(row=3, column=3, padx=(40, 0), pady=(30, 0), sticky='e')

snacks7ImageSearch.grid(row=4, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
snacks8ImageSearch.grid(row=4, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
snacks9ImageSearch.grid(row=4, column=3, padx=(40, 0), pady=(30, 0), sticky='w')
snacks10ImageSearch.grid(row=4, column=3, padx=(40, 0), pady=(30, 0), sticky='e')

snacks11ImageSearch.grid(row=5, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
snacks12ImageSearch.grid(row=5, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
snacks13ImageSearch.grid(row=5, column=3, padx=(40, 0), pady=(30, 0), sticky='w')
snacks14ImageSearch.grid(row=5, column=3, padx=(40, 0), pady=(30, 0), sticky='e')

snacks15ImageSearch.grid(row=6, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
snacks16ImageSearch.grid(row=6, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
snacks17ImageSearch.grid(row=6, column=3, padx=(40, 0), pady=(30, 0), sticky='w')
snacks18ImageSearch.grid(row=6, column=3, padx=(40, 0), pady=(30, 0), sticky='e')

snacks19ImageSearch.grid(row=7, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
snacks20ImageSearch.grid(row=7, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
snacks21ImageSearch.grid(row=7, column=3, padx=(40, 0), pady=(30, 0), sticky='w')
snacks22ImageSearch.grid(row=7, column=3, padx=(40, 0), pady=(30, 0), sticky='e')

snacks23ImageSearch.grid(row=8, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
snacks24ImageSearch.grid(row=8, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
snacks25ImageSearch.grid(row=8, column=3, padx=(40, 0), pady=(30, 0), sticky='w')
snacks26ImageSearch.grid(row=8, column=3, padx=(40, 0), pady=(30, 0), sticky='e')

snacks27ImageSearch.grid(row=9, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
snacks28ImageSearch.grid(row=9, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
snacks29ImageSearch.grid(row=9, column=3, padx=(40, 0), pady=(30, 0), sticky='w')
snacks30ImageSearch.grid(row=9, column=3, padx=(40, 0), pady=(30, 0), sticky='e')

drinksImageSearch.grid(row=10, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
drinks1ImageSearch.grid(row=10, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
drinks2ImageSearch.grid(row=10, column=3, padx=(40, 0), pady=(30, 0), sticky='w')
drinks3ImageSearch.grid(row=10, column=3, padx=(40, 0), pady=(30, 0), sticky='e')

drinks4ImageSearch.grid(row=11, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
drinks5ImageSearch.grid(row=11, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
drinks6ImageSearch.grid(row=11, column=3, padx=(40, 0), pady=(30, 0), sticky='w')
drinks7ImageSearch.grid(row=11, column=3, padx=(40, 0), pady=(30, 0), sticky='e')

drinks8ImageSearch.grid(row=12, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
drinks9ImageSearch.grid(row=12, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
drinks10ImageSearch.grid(row=12, column=3, padx=(40, 0), pady=(30, 0), sticky='w')
drinks11ImageSearch.grid(row=12, column=3, padx=(40, 0), pady=(30, 0), sticky='e')

drinks12ImageSearch.grid(row=13, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
dessertImageSearch.grid(row = 13, column = 2, padx = (40,0), pady = (30,0), sticky = 'e')
dessert1ImageSearch.grid(row = 13, column = 3, padx = (40,0), pady = (30,0), sticky = 'w')
dessert2ImageSearch.grid(row = 13, column = 3, padx = (40,0), pady = (30,0),  sticky = 'e')

dessert3ImageSearch.grid(row = 14, column = 2, padx = (200,0), pady = (30,0),  sticky = 'w')  
meals9ImageSearch.grid(row = 14, column = 2, padx = (40,0), pady = (30,0),  sticky = 'e')
meals10ImageSearch.grid(row = 14, column = 3, padx = (40,0), pady = (30,0),  sticky = 'w')
meals11ImageSearch.grid(row = 14, column = 3, padx = (40,0), pady = (30,0),  sticky = 'e')

dessert4ImageSearch.grid(row = 15, column = 2, padx = (200,0), pady = (30,0),  sticky = 'w')
dessert5ImageSearch.grid(row = 15, column = 2, padx = (40,0), pady = (30,0),  sticky = 'e')

#NO RESULT
invalid_label = Label(searchScrollbar, text='Currently not available', font='Shriekhand, 20', width=20, height=10)

#SEARCH PAGE FUNCTIONS

#Function to Forget all images displayed
def searchForget():
    mealsImageSearch.grid_forget()
    meals1ImageSearch.grid_forget()
    meals2ImageSearch.grid_forget()
    meals3ImageSearch.grid_forget()
    meals4ImageSearch.grid_forget()
    meals5ImageSearch.grid_forget()
    meals6ImageSearch.grid_forget()
    meals7ImageSearch.grid_forget()
    meals8ImageSearch.grid_forget()
    drinksImageSearch.grid_forget()
    drinks1ImageSearch.grid_forget()
    drinks2ImageSearch.grid_forget()
    drinks3ImageSearch.grid_forget()
    drinks4ImageSearch.grid_forget()
    drinks5ImageSearch.grid_forget()
    drinks6ImageSearch.grid_forget()
    drinks7ImageSearch.grid_forget()
    drinks8ImageSearch.grid_forget()
    drinks9ImageSearch.grid_forget()
    drinks10ImageSearch.grid_forget()
    drinks11ImageSearch.grid_forget()
    drinks12ImageSearch.grid_forget()
    snacksImageSearch.grid_forget()
    snacks1ImageSearch.grid_forget()
    snacks2ImageSearch.grid_forget()
    snacks3ImageSearch.grid_forget()
    snacks4ImageSearch.grid_forget()
    snacks5ImageSearch.grid_forget()
    snacks6ImageSearch.grid_forget()
    snacks7ImageSearch.grid_forget()
    snacks8ImageSearch.grid_forget()
    snacks9ImageSearch.grid_forget()
    snacks10ImageSearch.grid_forget()
    snacks11ImageSearch.grid_forget()
    snacks12ImageSearch.grid_forget()
    snacks13ImageSearch.grid_forget()
    snacks14ImageSearch.grid_forget()
    snacks15ImageSearch.grid_forget()
    snacks16ImageSearch.grid_forget()
    snacks17ImageSearch.grid_forget()
    snacks18ImageSearch.grid_forget()
    snacks19ImageSearch.grid_forget()
    snacks20ImageSearch.grid_forget()
    snacks21ImageSearch.grid_forget()
    snacks22ImageSearch.grid_forget()
    snacks23ImageSearch.grid_forget()
    snacks24ImageSearch.grid_forget()
    snacks25ImageSearch.grid_forget()
    snacks26ImageSearch.grid_forget()
    snacks27ImageSearch.grid_forget()
    snacks28ImageSearch.grid_forget()
    snacks29ImageSearch.grid_forget()
    snacks30ImageSearch.grid_forget()
    dessertImageSearch.grid_forget()
    dessert1ImageSearch.grid_forget()
    dessert2ImageSearch.grid_forget()
    dessert3ImageSearch.grid_forget()  
    meals9ImageSearch.grid_forget()
    meals10ImageSearch.grid_forget()
    meals11ImageSearch.grid_forget()
    dessert4ImageSearch.grid_forget()
    dessert5ImageSearch.grid_forget()

#Function used in searching
def userSearching():
    search = search_entry.get()
    searchFood = search.lower()

    if searchFood == "":
        searchReset()

    elif searchFood == "burger" or searchFood == "burgers":
        searchForget()
        snacks12ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
        snacks13ImageSearch.grid(row=0, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
        snacks14ImageSearch.grid(row=0, column=4, padx=(40, 0), pady=(30, 0), sticky='w')
        snacks15ImageSearch.grid(row=0, column=5, padx=(40, 0), pady=(30, 0), sticky='e')
        snacks16ImageSearch.grid(row=1, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
        snacks17ImageSearch.grid(row=1, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
        snacks30ImageSearch.grid(row=1, column=4, padx=(40, 0), pady=(30, 0), sticky='w')

    elif searchFood == "fewa":
        searchForget()
        snacks19ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')
        snacks20ImageSearch.grid(row=0, column=3, padx=(40, 0), pady=(30, 0), sticky='e')

    elif searchFood == "footlong":
        searchForget()
        snacks21ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')
        snacks29ImageSearch.grid(row=0, column=3, padx=(40, 0), pady=(30, 0), sticky='e')

    elif searchFood == "hotdog":
        searchForget()
        snacks18ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')
        meals1ImageSearch.grid(row=0, column=3, padx=(40, 0), pady=(30, 0), sticky='e')

    elif searchFood == "chao fan" or searchFood == "chaofan"or searchFood == "chao":
        searchForget()
        mealsImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')
        meals1ImageSearch.grid(row=0, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
        meals2ImageSearch.grid(row=0, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
        meals3ImageSearch.grid(row=0, column=5, padx=(40, 0), pady=(30, 0), sticky='e')
        meals4ImageSearch.grid(row=1, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
        meals5ImageSearch.grid(row=1, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
        meals6ImageSearch.grid(row=1, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
        meals7ImageSearch.grid(row=1, column=5, padx=(40, 0), pady=(30, 0), sticky='e')
        meals8ImageSearch.grid(row=2, column=2, padx=(40, 0), pady=(30, 0), sticky='e')

    elif searchFood == "waffle"or searchFood == "waffles":
        searchForget()
        snacksImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')
        snacks1ImageSearch.grid(row=0, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
        snacks2ImageSearch.grid(row=0, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
        snacks3ImageSearch.grid(row=0, column=5, padx=(40, 0), pady=(30, 0), sticky='e')
        snacks4ImageSearch.grid(row=1, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
        snacks5ImageSearch.grid(row=1, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
        snacks6ImageSearch.grid(row=1, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
        snacks7ImageSearch.grid(row=1, column=5, padx=(40, 0), pady=(30, 0), sticky='e')
        snacks8ImageSearch.grid(row=2, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
        snacks9ImageSearch.grid(row=2, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
        snacks10ImageSearch.grid(row=2, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
        snacks11ImageSearch.grid(row=2, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    elif searchFood == "sandwich" or searchFood == "sandwiches":
        searchForget()
        snacks22ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')
        snacks23ImageSearch.grid(row=0, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
        snacks24ImageSearch.grid(row=0, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
        snacks25ImageSearch.grid(row=0, column=5, padx=(40, 0), pady=(30, 0), sticky='e')
        snacks26ImageSearch.grid(row=1, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
        snacks27ImageSearch.grid(row=1, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
        snacks18ImageSearch.grid(row=1, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
        snacks21ImageSearch.grid(row=1, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    elif searchFood == "fries" or searchFood == "french fries":
        searchForget()
        snacks28ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')
        snacks29ImageSearch.grid(row=0, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
        snacks30ImageSearch.grid(row=0, column=4, padx=(40, 0), pady=(30, 0), sticky='e')

    elif searchFood == "meatball" or searchFood == "meatballs":
        searchForget()
        mealsImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')

    elif searchFood == "shanghai" or searchFood == "shanghai chao fan" or searchFood == "shanghai chaofan" or searchFood == "lumpia"or searchFood == "lumpiang shanghai":
        searchForget()
        meals2ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')

    elif searchFood == "longganisa"  or searchFood == "longganisa chao fan" or searchFood == "longganisa chaofan":
        searchForget()
        meals3ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')

    elif searchFood == "maling" or searchFood == "maling chao fan" or searchFood == "maling chaofan":
        searchForget()
        meals4ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')

    elif searchFood == "embutido" or searchFood == "embutido chao fan" or searchFood == "embutido chaofan":
        searchForget()
        meals5ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')

    elif searchFood == "siomai" or searchFood == "siomai chao fan" or searchFood == "siomai chaofan" or searchFood == "siomai rice":
        searchForget()
        meals6ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')

    elif searchFood == "sisig" or searchFood == "tofu sisig" or searchFood == "tofusisig":
        searchForget()
        meals7ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')

    elif searchFood == "burgersteak" or searchFood == "burger steak":
        searchForget()
        meals7ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')

    elif searchFood == "chicken" or searchFood == "wings" or searchFood == "buffalo" or searchFood == "buffalo wings" or searchFood == "chicken wings":
        searchForget() 
        snacks24ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')
        snacks25ImageSearch.grid(row=0, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
        meals9ImageSearch.grid(row=0, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
        meals10ImageSearch.grid(row=0, column=5, padx=(40, 0), pady=(30, 0), sticky='e')
        meals11ImageSearch.grid(row=1, column=2, padx=(200, 0), pady=(30, 0), sticky='e')

    elif searchFood == "coffee" or searchFood == "kofi":
        searchForget()
        drinks2ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')
        drinks3ImageSearch.grid(row=0, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
        drinks4ImageSearch.grid(row=0, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
        drinks5ImageSearch.grid(row=0, column=5, padx=(40, 0), pady=(30, 0), sticky='e')
         
    
    elif searchFood == "latte":
        searchForget()
        drinks2ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')
        drinks3ImageSearch.grid(row=0, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
        drinks12ImageSearch.grid(row=0, column=4, padx=(40, 0), pady=(30, 0), sticky='e')    
        drinks11ImageSearch.grid(row=0, column=5, padx=(40, 0), pady=(30, 0), sticky='e')
        drinks10ImageSearch.grid(row=1, column=2, padx=(200, 0), pady=(30, 0), sticky='e')
     
    elif searchFood == "frappe":
        searchForget()
        drinks8ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')
        drinks9ImageSearch.grid(row=0, column=3, padx=(40, 0), pady=(30, 0), sticky='e')

    elif searchFood == "tea":
        searchForget()
        drinksImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')  
        drinks1ImageSearch.grid(row=0, column=3, padx=(40, 0), pady=(30, 0), sticky='e') 
        drinks6ImageSearch.grid(row=0, column=4, padx=(40, 0), pady=(30, 0), sticky='e') 
        drinks7ImageSearch.grid(row=0, column=5, padx=(40, 0), pady=(30, 0), sticky='e') 

    elif searchFood == "fruit tea" or searchFood == "fruit":
        searchForget()
        drinksImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')
        drinks1ImageSearch.grid(row=0, column=3, padx=(40, 0), pady=(30, 0), sticky='e')   

    elif searchFood == "milktea" or searchFood == "milk":
        searchForget()
        drinks6ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')
        drinks7ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')

    elif searchFood == "ice cream" or searchFood == "icecream"  or searchFood == "ice" or searchFood == "cream":
        searchForget()
        dessertImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')
        dessert1ImageSearch.grid(row=0, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
        dessert2ImageSearch.grid(row=0, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
        dessert3ImageSearch.grid(row=0, column=5, padx=(40, 0), pady=(30, 0), sticky='e')
        dessert4ImageSearch.grid(row=1, column=2, padx=(200, 0), pady=(30, 0), sticky='w')

    elif searchFood == "yogurt" or searchFood == "yoghurt":
        searchForget()
        dessert5ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')  

    elif searchFood == "froyo" or searchFood == "froyo topps":
        searchForget()
        dessertImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')
        dessert1ImageSearch.grid(row=0, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
        dessert2ImageSearch.grid(row=0, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
        dessert3ImageSearch.grid(row=0, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    else:
        searchForget()
        invalid_label.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')

#Functions used to reset image displays
def searchReset():
    searchForget()
    invalid_label.grid_forget()
    mealsImageSearch.grid(row=0, column=2, padx=(200, 0), sticky='e')
    meals1ImageSearch.grid(row=0, column=3, padx=(40, 0), sticky='e')
    meals2ImageSearch.grid(row=0, column=4, padx=(40, 0), sticky='w')
    meals3ImageSearch.grid(row=0, column=5, padx=(40, 0), sticky='e')

    meals4ImageSearch.grid(row=1, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
    meals5ImageSearch.grid(row=1, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    meals6ImageSearch.grid(row=1, column=4, padx=(40, 0), pady=(30, 0), sticky='w')
    meals7ImageSearch.grid(row=1, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    meals8ImageSearch.grid(row=2, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
    snacksImageSearch.grid(row=2, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks1ImageSearch.grid(row=2, column=4, padx=(40, 0), pady=(30, 0), sticky='w')
    snacks2ImageSearch.grid(row=2, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks3ImageSearch.grid(row=3, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
    snacks4ImageSearch.grid(row=3, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks5ImageSearch.grid(row=3, column=4, padx=(40, 0), pady=(30, 0), sticky='w')
    snacks6ImageSearch.grid(row=3, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks7ImageSearch.grid(row=4, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
    snacks8ImageSearch.grid(row=4, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks9ImageSearch.grid(row=4, column=4, padx=(40, 0), pady=(30, 0), sticky='w')
    snacks10ImageSearch.grid(row=4, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks11ImageSearch.grid(row=5, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
    snacks12ImageSearch.grid(row=5, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks13ImageSearch.grid(row=5, column=4, padx=(40, 0), pady=(30, 0), sticky='w')
    snacks14ImageSearch.grid(row=5, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks15ImageSearch.grid(row=6, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
    snacks16ImageSearch.grid(row=6, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks17ImageSearch.grid(row=6, column=4, padx=(40, 0), pady=(30, 0), sticky='w')
    snacks18ImageSearch.grid(row=6, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks19ImageSearch.grid(row=7, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
    snacks20ImageSearch.grid(row=7, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks21ImageSearch.grid(row=7, column=4, padx=(40, 0), pady=(30, 0), sticky='w')
    snacks22ImageSearch.grid(row=7, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks23ImageSearch.grid(row=8, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
    snacks24ImageSearch.grid(row=8, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks25ImageSearch.grid(row=8, column=4, padx=(40, 0), pady=(30, 0), sticky='w')
    snacks26ImageSearch.grid(row=8, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks27ImageSearch.grid(row=9, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
    snacks28ImageSearch.grid(row=9, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks29ImageSearch.grid(row=9, column=4, padx=(40, 0), pady=(30, 0), sticky='w')
    snacks30ImageSearch.grid(row=9, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    drinksImageSearch.grid(row=10, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
    drinks1ImageSearch.grid(row=10, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    drinks2ImageSearch.grid(row=10, column=4, padx=(40, 0), pady=(30, 0), sticky='w')
    drinks3ImageSearch.grid(row=10, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    drinks4ImageSearch.grid(row=11, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
    drinks5ImageSearch.grid(row=11, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    drinks6ImageSearch.grid(row=11, column=4, padx=(40, 0), pady=(30, 0), sticky='w')
    drinks7ImageSearch.grid(row=11, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    drinks8ImageSearch.grid(row=12, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
    drinks9ImageSearch.grid(row=12, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    drinks10ImageSearch.grid(row=12, column=4, padx=(40, 0), pady=(30, 0), sticky='w')
    drinks11ImageSearch.grid(row=12, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    drinks12ImageSearch.grid(row=13, column=2, padx=(200, 0), pady=(30, 0), sticky='w')
    dessertImageSearch.grid(row = 13, column = 3, padx = (40,0), pady = (30,0), sticky = 'e')
    dessert1ImageSearch.grid(row = 13, column = 4, padx = (40,0), pady = (30,0), sticky = 'w')
    dessert2ImageSearch.grid(row = 13, column = 5, padx = (40,0), pady = (30,0),  sticky = 'e')

    dessert3ImageSearch.grid(row = 14, column = 2, padx = (200,0), pady = (30,0),  sticky = 'w')  
    meals9ImageSearch.grid(row = 14, column = 3, padx = (40,0), pady = (30,0),  sticky = 'e')
    meals10ImageSearch.grid(row = 14, column = 4, padx = (40,0), pady = (30,0),  sticky = 'w')
    meals11ImageSearch.grid(row = 14, column = 5, padx = (40,0), pady = (30,0),  sticky = 'e')

    dessert4ImageSearch.grid(row = 15, column = 2, padx = (200,0), pady = (30,0),  sticky = 'w')
    dessert5ImageSearch.grid(row = 15, column = 3, padx = (40,0), pady = (30,0),  sticky = 'e')

#Function used for the recommended foods
def reco1Redirect():
    searchFunction()
    search_entry = "FEWA"
    search = search_entry
    searchFood = search.lower()
    if searchFood == "fewa":
        searchForget()
        snacks19ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')

def reco2Redirect():
    searchFunction()
    search_entry = "chicken"
    search = search_entry
    searchFood = search.lower()
    if searchFood == "chicken":
        searchForget()
        meals10ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')
              
def reco3Redirect():
    searchFunction()
    search_entry = "froyo"
    search = search_entry
    searchFood = search.lower()
    if searchFood == "froyo":
        searchForget()
        dessert2ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')
        
def reco4Redirect():
    searchFunction()
    search_entry = "bacon"
    search = search_entry
    searchFood = search.lower()
    if searchFood == "bacon":
        searchForget()
        snacks17ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')

#FILTER FUNCTIONS

#FUNCTION FOR CANCELING FILTER FROM HIGH - LOW
def collapseSearchHL():
        searchForget()
        searchReset()
        filterHLPrice = ctk.CTkButton(master = search_page, text = 'high - low', 
                            bg_color = '#7d1418', fg_color = '#7d1418', command = lambda: searchFilterHL())
        filterHLPrice.place(x=30, y=330)

#FUNCTION FOR CANCELING FILTER FROM LOW - HIGH
def collapseSearchLH():
        searchForget()
        searchReset()
        filterLHPrice = ctk.CTkButton(master = search_page, text = 'low - high', 
                            bg_color = '#7d1418', fg_color = '#7d1418', command = lambda: searchFilterLH())
        filterLHPrice.place(x=30, y=300)

#SEARCH FILTER FROM LOWEST TO HIGHEST
def searchFilterLH():
 
    collapseSearchHL()
    collapseSearchLH()
        
    filterLHPrice = ctk.CTkButton(master = search_page, text = 'low - high', 
                            bg_color = 'white', fg_color = 'white', command = lambda: collapseSearchLH())
    filterLHPrice.place(x=30, y=300)
    
    searchForget()
    snacks26ImageSearch.grid(row=0, column=2, padx=(200, 0), pady=(30, 0), sticky='e')
    snacks24ImageSearch.grid(row=0, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks22ImageSearch.grid(row=0, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks12ImageSearch.grid(row=0, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks4ImageSearch.grid(row=1, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks2ImageSearch.grid(row=1, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks11ImageSearch.grid(row=1, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    dessert4ImageSearch.grid(row=1, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks5ImageSearch.grid(row=2, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks18ImageSearch.grid(row=2, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks1ImageSearch.grid(row=2, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks3ImageSearch.grid(row=2, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks7ImageSearch.grid(row=3, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    snacksImageSearch.grid(row=3, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks9ImageSearch.grid(row=3, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks6ImageSearch.grid(row=3, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks8ImageSearch.grid(row=4, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks16ImageSearch.grid(row=4, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    drinksImageSearch.grid(row=4, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    drinks2ImageSearch.grid(row=4, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    drinks4ImageSearch.grid(row=5, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    drinks6ImageSearch.grid(row=5, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    dessertImageSearch.grid(row=5, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    dessert5ImageSearch.grid(row=5, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks13ImageSearch.grid(row=6, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks14ImageSearch.grid(row=6, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks23ImageSearch.grid(row=6, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks25ImageSearch.grid(row=6, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks27ImageSearch.grid(row=7, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks21ImageSearch.grid(row=7, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks28ImageSearch.grid(row=7, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    drinks10ImageSearch.grid(row=7, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    drinks11ImageSearch.grid(row=8, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    drinks12ImageSearch.grid(row=8, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    drinks1ImageSearch.grid(row=8, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    drinks3ImageSearch.grid(row=8, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    drinks5ImageSearch.grid(row=9, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    drinks7ImageSearch.grid(row=9, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    drinks8ImageSearch.grid(row=9, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    dessert1ImageSearch.grid(row=9, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks19ImageSearch.grid(row=10, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks17ImageSearch.grid(row=10, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    drinks9ImageSearch.grid(row=10, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    meals9ImageSearch.grid(row=10, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    mealsImageSearch.grid(row=11, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    meals1ImageSearch.grid(row=11, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    meals2ImageSearch.grid(row=11, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    meals3ImageSearch.grid(row=11, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    meals4ImageSearch.grid(row=12, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    meals5ImageSearch.grid(row=12, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks30ImageSearch.grid(row=12, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks15ImageSearch.grid(row=12, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    meals10ImageSearch.grid(row=13, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    dessert2ImageSearch.grid(row=13, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks20ImageSearch.grid(row=13, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    meals6ImageSearch.grid(row=13, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    meals7ImageSearch.grid(row=14, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    meals8ImageSearch.grid(row=14, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    dessert3ImageSearch.grid(row=14, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks29ImageSearch.grid(row=14, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    meals11ImageSearch.grid(row=15, column=2, padx=(40, 0), pady=(30, 0), sticky='e')

#SEARCH FILTER FROM HIGHEST TO LOWEST
def searchFilterHL():

    collapseSearchLH()
    collapseSearchHL()
    
    filter1Price = ctk.CTkButton(master = search_page, text = 'high - low', 
                            bg_color = 'white', fg_color = 'white', command = lambda: collapseSearchHL())
    filter1Price.place(x=30, y=330)

    meals11ImageSearch.grid(row=0, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks29ImageSearch.grid(row=0, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    dessert3ImageSearch.grid(row=0, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    meals8ImageSearch.grid(row=0, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    meals7ImageSearch.grid(row=1, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    meals6ImageSearch.grid(row=1, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks20ImageSearch.grid(row=1, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    dessert2ImageSearch.grid(row=1, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    meals10ImageSearch.grid(row=2, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks15ImageSearch.grid(row=2, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks30ImageSearch.grid(row=2, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    meals5ImageSearch.grid(row=2, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    meals4ImageSearch.grid(row=3, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    meals3ImageSearch.grid(row=3, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    meals2ImageSearch.grid(row=3, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    meals1ImageSearch.grid(row=3, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    mealsImageSearch.grid(row=4, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    meals9ImageSearch.grid(row=4, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    drinks9ImageSearch.grid(row=4, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks17ImageSearch.grid(row=4, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks19ImageSearch.grid(row=5, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    dessert1ImageSearch.grid(row=5, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    drinks8ImageSearch.grid(row=5, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    drinks7ImageSearch.grid(row=5, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    drinks5ImageSearch.grid(row=6, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    drinks3ImageSearch.grid(row=6, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    drinks1ImageSearch.grid(row=6, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    drinks12ImageSearch.grid(row=6, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    drinks11ImageSearch.grid(row=7, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    drinks10ImageSearch.grid(row=7, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks28ImageSearch.grid(row=7, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks21ImageSearch.grid(row=7, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks27ImageSearch.grid(row=8, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks25ImageSearch.grid(row=8, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks23ImageSearch.grid(row=8, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks14ImageSearch.grid(row=8, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks13ImageSearch.grid(row=9, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    dessert5ImageSearch.grid(row=9, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    dessertImageSearch.grid(row=9, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    drinks6ImageSearch.grid(row=9, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    drinks4ImageSearch.grid(row=10, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    drinks2ImageSearch.grid(row=10, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    drinksImageSearch.grid(row=10, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks16ImageSearch.grid(row=10, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks8ImageSearch.grid(row=11, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks6ImageSearch.grid(row=11, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks9ImageSearch.grid(row=11, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    snacksImageSearch.grid(row=11, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks7ImageSearch.grid(row=12, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks3ImageSearch.grid(row=12, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks1ImageSearch.grid(row=12, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks18ImageSearch.grid(row=12, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks5ImageSearch.grid(row=13, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    dessert4ImageSearch.grid(row=13, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks11ImageSearch.grid(row=13, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks2ImageSearch.grid(row=13, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks4ImageSearch.grid(row=14, column=2, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks12ImageSearch.grid(row=14, column=3, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks22ImageSearch.grid(row=14, column=4, padx=(40, 0), pady=(30, 0), sticky='e')
    snacks24ImageSearch.grid(row=14, column=5, padx=(40, 0), pady=(30, 0), sticky='e')

    snacks26ImageSearch.grid(row=15, column=2, padx=(200, 0), pady=(30, 0), sticky='e')

#CALLING ADD TO CART PAGE
def addtoCartFunction():
    cart_page.place(relheight=1, relwidth=1)
    homepage.place_forget()
    categories_page.place_forget()
    store_page.place_forget()
    search_page.place_forget()
    meals_page.place_forget()
    drinks_page.place_forget()
    dessert_page.place_forget()
    snacks_page.place_forget()    

#TOTAL COMPUTED PRICE IN ADD TO CART
total = 0
a = 0
b = 0
c = 100

# Store image references to prevent garbage collection
image_references = []

#FUNCTION FOR ADD TO CART
def order_click(number, orderName):
    global total, a, b
    order = int(number)
    total += order
    o.delete(0, ctk.END)
    o.insert(0, total)
    
    if b == 5:
        a += 1
        b = 0

    if orderName == "mealsImageSearch":
       mealsImageR = mealsImagePath.resize((250, 250))
       mealsImageRe = ImageTk.PhotoImage(mealsImageR)
       image_references.append(mealsImageRe)
       mealsImageSe = Label(cartpageScrollbar, image=mealsImageRe, background='white')
       mealsImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='n')

    elif orderName == "meals1ImageSearch":
       meals1ImageR = meals1ImagePath.resize((250, 250))
       meals1ImageRe = ImageTk.PhotoImage(meals1ImageR)
       image_references.append(meals1ImageRe)
       meals1ImageSe = Label(cartpageScrollbar, image=meals1ImageRe, background='white')
       meals1ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w') 

    elif orderName == "meals2ImageSearch":
       meals2ImageR = meals2ImagePath.resize((250, 250))
       meals2ImageRe = ImageTk.PhotoImage(meals2ImageR)
       image_references.append(meals2ImageRe)
       meals2ImageSe = Label(cartpageScrollbar, image=meals2ImageRe, background='white')
       meals2ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w') 

    elif orderName == "meals3ImageSearch":
       meals3ImageR = meals3ImagePath.resize((250, 250))
       meals3ImageRe = ImageTk.PhotoImage(meals3ImageR)
       image_references.append(meals3ImageRe)
       meals3ImageSe = Label(cartpageScrollbar, image=meals3ImageRe, background='white')
       meals3ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w') 

    elif orderName == "meals4ImageSearch":
       meals4ImageR = meals4ImagePath.resize((250, 250))
       meals4ImageRe = ImageTk.PhotoImage(meals4ImageR)
       image_references.append(meals4ImageRe)
       meals4ImageSe = Label(cartpageScrollbar, image=meals4ImageRe, background='white')
       meals4ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w') 

    elif orderName == "meals5ImageSearch":
       meals5ImageR = meals5ImagePath.resize((250, 250))
       meals5ImageRe = ImageTk.PhotoImage(meals5ImageR)
       image_references.append(meals5ImageRe)
       meals5ImageSe = Label(cartpageScrollbar, image=meals5ImageRe, background='white')
       meals5ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')     

    elif orderName == "meals6ImageSearch":
       meals6ImageR = meals6ImagePath.resize((250, 250))
       meals6ImageRe = ImageTk.PhotoImage(meals6ImageR)
       image_references.append(meals6ImageRe)
       meals6ImageSe = Label(cartpageScrollbar, image=meals6ImageRe, background='white')
       meals6ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')

    elif orderName == "meals7ImageSearch":
       meals7ImageR = meals7ImagePath.resize((250, 250))
       meals7ImageRe = ImageTk.PhotoImage(meals7ImageR)
       image_references.append(meals7ImageRe)
       meals7ImageSe = Label(cartpageScrollbar, image=meals7ImageRe, background='white')
       meals7ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')

    elif orderName == "meals8ImageSearch":
       meals8ImageR = meals8ImagePath.resize((250, 250))
       meals8ImageRe = ImageTk.PhotoImage(meals8ImageR)
       image_references.append(meals8ImageRe)
       meals8ImageSe = Label(cartpageScrollbar, image=meals8ImageRe, background='white')
       meals8ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')                                    

    elif orderName == "snacksImageSearch":
       snacksImageR = snacksImagePath.resize((250, 250))
       snacksImageRe = ImageTk.PhotoImage(snacksImageR)
       image_references.append(snacksImageRe)
       snacksImageSe = Label(cartpageScrollbar, image=snacksImageRe, background='white')
       snacksImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')

    elif orderName == "snacks1ImageSearch":
       snacks1ImageR = snacks1ImagePath.resize((250, 250))
       snacks1ImageRe = ImageTk.PhotoImage(snacks1ImageR)
       image_references.append(snacks1ImageRe)
       snacks1ImageSe = Label(cartpageScrollbar, image=snacks1ImageRe, background='white')
       snacks1ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   
    
    elif orderName == "snacks2ImageSearch":
       snacks2ImageR = snacks2ImagePath.resize((250, 250))
       snacks2ImageRe = ImageTk.PhotoImage(snacks2ImageR)
       image_references.append(snacks2ImageRe)
       snacks2ImageSe = Label(cartpageScrollbar, image=snacks2ImageRe, background='white')
       snacks2ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')

    elif orderName == "snacks3ImageSearch":
       snacks3ImageR = snacks3ImagePath.resize((250, 250))
       snacks3ImageRe = ImageTk.PhotoImage(snacks3ImageR)
       image_references.append(snacks3ImageRe)
       snacks3ImageSe = Label(cartpageScrollbar, image=snacks3ImageRe, background='white')
       snacks3ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   

    elif orderName == "snacks4ImageSearch":
       snacks4ImageR = snacks4ImagePath.resize((250, 250))
       snacks4ImageRe = ImageTk.PhotoImage(snacks4ImageR)
       image_references.append(snacks4ImageRe)
       snacks4ImageSe = Label(cartpageScrollbar, image=snacks4ImageRe, background='white')
       snacks4ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   

    elif orderName == "snacks5ImageSearch":
       snacks5ImageR = snacks5ImagePath.resize((250, 250))
       snacks5ImageRe = ImageTk.PhotoImage(snacks5ImageR)
       image_references.append(snacks5ImageRe)
       snacks5ImageSe = Label(cartpageScrollbar, image=snacks5ImageRe, background='white')
       snacks5ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')      
    
    elif orderName == "snacks6ImageSearch":
       snacks6ImageR = snacks6ImagePath.resize((250, 250))
       snacks6ImageRe = ImageTk.PhotoImage(snacks6ImageR)
       image_references.append(snacks6ImageRe)
       snacks6ImageSe = Label(cartpageScrollbar, image=snacks6ImageRe, background='white')
       snacks6ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   

    elif orderName == "snacks7ImageSearch":
       snacks7ImageR = snacks7ImagePath.resize((250, 250))
       snacks7ImageRe = ImageTk.PhotoImage(snacks7ImageR)
       image_references.append(snacks7ImageRe)
       snacks7ImageSe = Label(cartpageScrollbar, image=snacks7ImageRe, background='white')
       snacks7ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   
    
    elif orderName == "snacks8ImageSearch":
       snacks8ImageR = snacks8ImagePath.resize((250, 250))
       snacks8ImageRe = ImageTk.PhotoImage(snacks8ImageR)
       image_references.append(snacks8ImageRe)
       snacks8ImageSe = Label(cartpageScrollbar, image=snacks8ImageRe, background='white')
       snacks8ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')    
    
    elif orderName == "snacks9ImageSearch":
       snacks9ImageR = snacks9ImagePath.resize((250, 250))
       snacks9ImageRe = ImageTk.PhotoImage(snacks9ImageR)
       image_references.append(snacks9ImageRe)
       snacks9ImageSe = Label(cartpageScrollbar, image=snacks9ImageRe, background='white')
       snacks9ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   
    
    elif orderName == "snacks10ImageSearch":
       snacks10ImageR = snacks10ImagePath.resize((250, 250))
       snacks10ImageRe = ImageTk.PhotoImage(snacks10ImageR)
       image_references.append(snacks10ImageRe)
       snacks10ImageSe = Label(cartpageScrollbar, image=snacks10ImageRe, background='white')
       snacks10ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   
    
    elif orderName == "snacks11ImageSearch":
       snacks11ImageR = snacks11ImagePath.resize((250, 250))
       snacks11ImageRe = ImageTk.PhotoImage(snacks11ImageR)
       image_references.append(snacks11ImageRe)
       snacks11ImageSe = Label(cartpageScrollbar, image=snacks11ImageRe, background='white')
       snacks11ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   

    elif orderName == "snacks12ImageSearch":
       snacks12ImageR = snacks12ImagePath.resize((250, 250))
       snacks12ImageRe = ImageTk.PhotoImage(snacks12ImageR)
       image_references.append(snacks12ImageRe)
       snacks12ImageSe = Label(cartpageScrollbar, image=snacks12ImageRe, background='white')
       snacks12ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   

    elif orderName == "snacks13ImageSearch":
       snacks13ImageR = snacks13ImagePath.resize((250, 250))
       snacks13ImageRe = ImageTk.PhotoImage(snacks13ImageR)
       image_references.append(snacks13ImageRe)
       snacks13ImageSe = Label(cartpageScrollbar, image=snacks13ImageRe, background='white')
       snacks13ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   

    elif orderName == "snacks14ImageSearch":
       snacks14ImageR = snacks14ImagePath.resize((250, 250))
       snacks14ImageRe = ImageTk.PhotoImage(snacks14ImageR)
       image_references.append(snacks14ImageRe)
       snacks14ImageSe = Label(cartpageScrollbar, image=snacks14ImageRe, background='white')
       snacks14ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   

    elif orderName == "snacks15ImageSearch":
       snacks15ImageR = snacks15ImagePath.resize((250, 250))
       snacks15ImageRe = ImageTk.PhotoImage(snacks15ImageR)
       image_references.append(snacks15ImageRe)
       snacks15ImageSe = Label(cartpageScrollbar, image=snacks15ImageRe, background='white')
       snacks15ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   

    elif orderName == "snacks16ImageSearch":
       snacks16ImageR = snacks16ImagePath.resize((250, 250))
       snacks16ImageRe = ImageTk.PhotoImage(snacks16ImageR)
       image_references.append(snacks16ImageRe)
       snacks16ImageSe = Label(cartpageScrollbar, image=snacks16ImageRe, background='white')
       snacks16ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   

    elif orderName == "snacks17ImageSearch":
       snacks17ImageR = snacks17ImagePath.resize((250, 250))
       snacks17ImageRe = ImageTk.PhotoImage(snacks17ImageR)
       image_references.append(snacks17ImageRe)
       snacks17ImageSe = Label(cartpageScrollbar, image=snacks17ImageRe, background='white')
       snacks17ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   
    
    elif orderName == "snacks18ImageSearch":
       snacks18ImageR = snacks18ImagePath.resize((250, 250))
       snacks18ImageRe = ImageTk.PhotoImage(snacks18ImageR)
       image_references.append(snacks18ImageRe)
       snacks18ImageSe = Label(cartpageScrollbar, image=snacks18ImageRe, background='white')
       snacks18ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   

    elif orderName == "snacks19ImageSearch":
       snacks19ImageR = snacks19ImagePath.resize((250, 250))
       snacks19ImageRe = ImageTk.PhotoImage(snacks19ImageR)
       image_references.append(snacks19ImageRe)
       snacks19ImageSe = Label(cartpageScrollbar, image=snacks19ImageRe, background='white')
       snacks19ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   

    elif orderName == "snacks20ImageSearch":
       snacks20ImageR = snacks20ImagePath.resize((250, 250))
       snacks20ImageRe = ImageTk.PhotoImage(snacks20ImageR)
       image_references.append(snacks20ImageRe)
       snacks20ImageSe = Label(cartpageScrollbar, image=snacks20ImageRe, background='white')
       snacks20ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   
  
    elif orderName == "snacks21ImageSearch":
       snacks21ImageR = snacks21ImagePath.resize((250, 250))
       snacks21ImageRe = ImageTk.PhotoImage(snacks21ImageR)
       image_references.append(snacks21ImageRe)
       snacks21ImageSe = Label(cartpageScrollbar, image=snacks21ImageRe, background='white')
       snacks21ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   

    elif orderName == "snacks22ImageSearch":
       snacks22ImageR = snacks22ImagePath.resize((250, 250))
       snacks22ImageRe = ImageTk.PhotoImage(snacks22ImageR)
       image_references.append(snacks22ImageRe)
       snacks22ImageSe = Label(cartpageScrollbar, image=snacks22ImageRe, background='white')
       snacks22ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   

    elif orderName == "snacks23ImageSearch":
       snacks23ImageR = snacks23ImagePath.resize((250, 250))
       snacks23ImageRe = ImageTk.PhotoImage(snacks23ImageR)
       image_references.append(snacks23ImageRe)
       snacks23ImageSe = Label(cartpageScrollbar, image=snacks23ImageRe, background='white')
       snacks23ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   

    elif orderName == "snacks24ImageSearch":
       snacks24ImageR = snacks24ImagePath.resize((250, 250))
       snacks24ImageRe = ImageTk.PhotoImage(snacks24ImageR)
       image_references.append(snacks24ImageRe)
       snacks24ImageSe = Label(cartpageScrollbar, image=snacks24ImageRe, background='white')
       snacks24ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   
 
    elif orderName == "snacks25ImageSearch":
       snacks25ImageR = snacks25ImagePath.resize((250, 250))
       snacks25ImageRe = ImageTk.PhotoImage(snacks25ImageR)
       image_references.append(snacks25ImageRe)
       snacks25ImageSe = Label(cartpageScrollbar, image=snacks25ImageRe, background='white')
       snacks25ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')

    elif orderName == "snacks26ImageSearch":
       snacks26ImageR = snacks26ImagePath.resize((250, 250))
       snacks26ImageRe = ImageTk.PhotoImage(snacks26ImageR)
       image_references.append(snacks26ImageRe)
       snacks26ImageSe = Label(cartpageScrollbar, image=snacks26ImageRe, background='white')
       snacks26ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   

    elif orderName == "snacks27ImageSearch":
       snacks27ImageR = snacks27ImagePath.resize((250, 250))
       snacks27ImageRe = ImageTk.PhotoImage(snacks27ImageR)
       image_references.append(snacks27ImageRe)
       snacks27ImageSe = Label(cartpageScrollbar, image=snacks27ImageRe, background='white')
       snacks27ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   

    elif orderName == "snacks28ImageSearch":
       snacks28ImageR = snacks28ImagePath.resize((250, 250))
       snacks28ImageRe = ImageTk.PhotoImage(snacks28ImageR)
       image_references.append(snacks28ImageRe)
       snacks28ImageSe = Label(cartpageScrollbar, image=snacks28ImageRe, background='white')
       snacks28ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   

    elif orderName == "snacks29ImageSearch":
       snacks29ImageR = snacks29ImagePath.resize((250, 250))
       snacks29ImageRe = ImageTk.PhotoImage(snacks29ImageR)
       image_references.append(snacks29ImageRe)
       snacks29ImageSe = Label(cartpageScrollbar, image=snacks29ImageRe, background='white')
       snacks29ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')   

    elif orderName == "snacks30ImageSearch":
       snacks30ImageR = snacks30ImagePath.resize((250, 250))
       snacks30ImageRe = ImageTk.PhotoImage(snacks30ImageR)
       image_references.append(snacks30ImageRe)
       snacks30ImageSe = Label(cartpageScrollbar, image=snacks30ImageRe, background='white')
       snacks30ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='e')

    elif orderName == "drinksImageSearch":
       drinksImageR = drinksImagePath.resize((250, 250))
       drinksImageRe = ImageTk.PhotoImage(drinksImageR)
       image_references.append(drinksImageRe)
       drinksImageSe = Label(cartpageScrollbar, image=drinksImageRe, background='white')
       drinksImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')     

    elif orderName == "drinks1ImageSearch":
       drinks1ImageR = drinks1ImagePath.resize((250, 250))
       drinks1ImageRe = ImageTk.PhotoImage(drinks1ImageR)
       image_references.append(drinks1ImageRe)
       drinks1ImageSe = Label(cartpageScrollbar, image=drinks1ImageRe, background='white')
       drinks1ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')   

    elif orderName == "drinks2ImageSearch":
       drinks2ImageR = drinks2ImagePath.resize((250, 250))
       drinks2ImageRe = ImageTk.PhotoImage(drinks2ImageR)
       image_references.append(drinks2ImageRe)
       drinks2ImageSe = Label(cartpageScrollbar, image=drinks2ImageRe, background='white')
       drinks2ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')

    elif orderName == "drinks3ImageSearch":
       drinks3ImageR = drinks3ImagePath.resize((250, 250))
       drinks3ImageRe = ImageTk.PhotoImage(drinks3ImageR)
       image_references.append(drinks3ImageRe)
       drinks3ImageSe = Label(cartpageScrollbar, image=drinks3ImageRe, background='white')
       drinks3ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')

    elif orderName == "drinks4ImageSearch":
       drinks4ImageR = drinks4ImagePath.resize((250, 250))
       drinks4ImageRe = ImageTk.PhotoImage(drinks4ImageR)
       image_references.append(drinks4ImageRe)
       drinks4ImageSe = Label(cartpageScrollbar, image=drinks4ImageRe, background='white')
       drinks4ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')            

    elif orderName == "drinks5ImageSearch":
       drinks5ImageR = drinks5ImagePath.resize((250, 250))
       drinks5ImageRe = ImageTk.PhotoImage(drinks5ImageR)
       image_references.append(drinks5ImageRe)
       drinks5ImageSe = Label(cartpageScrollbar, image=drinks5ImageRe, background='white')
       drinks5ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')   

    elif orderName == "drinks6ImageSearch":
       drinks6ImageR = drinks6ImagePath.resize((250, 250))
       drinks6ImageRe = ImageTk.PhotoImage(drinks6ImageR)
       image_references.append(drinks6ImageRe)
       drinks6ImageSe = Label(cartpageScrollbar, image=drinks6ImageRe, background='white')
       drinks6ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')  

    elif orderName == "drinks7ImageSearch":
       drinks7ImageR = drinks7ImagePath.resize((250, 250))
       drinks7ImageRe = ImageTk.PhotoImage(drinks7ImageR)
       image_references.append(drinks7ImageRe)
       drinks7ImageSe = Label(cartpageScrollbar, image=drinks7ImageRe, background='white')
       drinks7ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')   

    elif orderName == "drinks8ImageSearch":
       drinks8ImageR = drinks8ImagePath.resize((250, 250))
       drinks8ImageRe = ImageTk.PhotoImage(drinks8ImageR)
       image_references.append(drinks8ImageRe)
       drinks8ImageSe = Label(cartpageScrollbar, image=drinks8ImageRe, background='white')
       drinks8ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')  

    elif orderName == "drinks9ImageSearch":
       drinks9ImageR = drinks9ImagePath.resize((250, 250))
       drinks9ImageRe = ImageTk.PhotoImage(drinks9ImageR)
       image_references.append(drinks9ImageRe)
       drinks9ImageSe = Label(cartpageScrollbar, image=drinks9ImageRe, background='white')
       drinks9ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')    

    elif orderName == "drinks10ImageSearch":
       drinks10ImageR = drinks10ImagePath.resize((250, 250))
       drinks10ImageRe = ImageTk.PhotoImage(drinks10ImageR)
       image_references.append(drinks10ImageRe)
       drinks10ImageSe = Label(cartpageScrollbar, image=drinks10ImageRe, background='white')
       drinks10ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w') 

    elif orderName == "drinks11ImageSearch":
       drinks11ImageR = drinks11ImagePath.resize((250, 250))
       drinks11ImageRe = ImageTk.PhotoImage(drinks11ImageR)
       image_references.append(drinks11ImageRe)
       drinks11ImageSe = Label(cartpageScrollbar, image=drinks11ImageRe, background='white')
       drinks11ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')   

    elif orderName == "drinks12ImageSearch":
       drinks12ImageR = drinks12ImagePath.resize((250, 250))
       drinks12ImageRe = ImageTk.PhotoImage(drinks12ImageR)
       image_references.append(drinks12ImageR)
       drinks12ImageSe = Label(cartpageScrollbar, image=drinks12ImageRe, background='white')
       drinks12ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')              

    elif orderName == "dessertImageSearch":
       dessertImageR = dessert2ImagePath.resize((250, 250))
       dessertImageRe = ImageTk.PhotoImage(dessertImageR)
       image_references.append(dessertImageRe)
       dessertImageSe = Label(cartpageScrollbar, image=dessertImageRe, background='white')
       dessertImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')

    elif orderName == "dessert1ImageSearch":
       dessert1ImageR = dessert3ImagePath.resize((250, 250))
       dessert1ImageRe = ImageTk.PhotoImage(dessert1ImageR)
       image_references.append(dessert1ImageRe)
       dessert1ImageSe = Label(cartpageScrollbar, image=dessert1ImageRe, background='white')
       dessert1ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')    

    elif orderName == "dessert2ImageSearch":
       dessert2ImageR = dessert4ImagePath.resize((250, 250))
       dessert2ImageRe = ImageTk.PhotoImage(dessert2ImageR)
       image_references.append(dessert2ImageRe)
       dessert2ImageSe = Label(cartpageScrollbar, image=dessert2ImageRe, background='white')
       dessert2ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')        

    elif orderName == "dessert3ImageSearch":
       dessert3ImageR = dessert5ImagePath.resize((250, 250))
       dessert3ImageRe = ImageTk.PhotoImage(dessert3ImageR)
       image_references.append(dessert3ImageRe)
       dessert3ImageSe = Label(cartpageScrollbar, image=dessert3ImageRe, background='white')
       dessert3ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')

    elif orderName == "meals9ImageSearch":
       meals9ImageR = meals9ImagePath.resize((250, 250))
       meals9ImageRe = ImageTk.PhotoImage(meals9ImageR)
       image_references.append(meals9ImageRe)
       meals9ImageSe = Label(cartpageScrollbar, image=meals9ImageRe, background='white')
       meals9ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')  

    elif orderName == "meals10ImageSearch":
       meals10ImageR = meals10ImagePath.resize((250, 250))
       meals10ImageRe = ImageTk.PhotoImage(meals10ImageR)
       image_references.append(meals10ImageRe)
       meals10ImageSe = Label(cartpageScrollbar, image=meals10ImageRe, background='white')
       meals10ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')  

    elif orderName == "meals11ImageSearch":
       meals11ImageR = meals11ImagePath.resize((250, 250))
       meals11ImageRe = ImageTk.PhotoImage(meals11ImageR)
       image_references.append(meals11ImageRe)
       meals11ImageSe = Label(cartpageScrollbar, image=meals11ImageRe, background='white')
       meals11ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')     

    elif orderName == "dessert4ImageSearch":
       dessert4ImageR = dessertImagePath.resize((250, 250))
       dessert4ImageRe = ImageTk.PhotoImage(dessert4ImageR)
       image_references.append(dessert4ImageRe)
       dessert4ImageSe = Label(cartpageScrollbar, image=dessert4ImageRe, background='white')
       dessert4ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')

    elif orderName == "dessert5ImageSearch":
       dessert5ImageR = dessert1ImagePath.resize((250, 250))
       dessert5ImageRe = ImageTk.PhotoImage(dessert5ImageR)
       image_references.append(dessert5ImageRe)
       dessert5ImageSe = Label(cartpageScrollbar, image=dessert5ImageRe, background='white')
       dessert5ImageSe.grid(row=a, column=b, padx=(40, 0), pady=(130, 0), sticky='w')   
    
    b += 1

#FUNCTION FOR CLEARING CART
def cartClear():
    global total, image_references, a, b
    o.delete(0, END)
    a = 0
    b = 0
    total = 0
    image_references.clear()

window.mainloop()