import connect_firebase
import datetime
# from Mail_Sending import GenerateMail

db_ref = connect_firebase.db.collection('users')


users = {}
lastid = 0
userIds = []
emails = []

def refresh():
    docs = db_ref.stream()
    global users, userIds, lastid
    userIds = []
    for doc in docs:
        users[doc.id] = doc.to_dict()
        userIds.append(users[doc.id]['Username'])
        emails.append(users[doc.id]['Email'])
        lastid = int(doc.id.replace("ID", ""))


def check(userID,password):
    refresh()

    for i,j in users.items():
        if '@' in userID:
            if j['Email'] == userID and j['Password'] == password:
                return True
        else:
            if j['Username'] == userID and j['Password'] == password:
                return True
    return False



def changePassword(email, newPassword):
    refresh()
    if email not in emails:
        print("Email does not exist")
        return "Email does not exist"

    user_doc_id = None
    for doc_id, user_data in users.items():
        if user_data['Email'] == email:
            user_doc_id = doc_id
            break

    if user_doc_id:
        try:
            db_ref.document(user_doc_id).update({"Password": newPassword})
            print(f"Password successfully updated for user with email '{email}'!")
            return True
        except Exception as e:
            print(f"An error occurred while updating the password: {e}")
            return f"An error occurred while updating the password: {e}"
    else:
        return "User not found"



def New_User(Username,Password,Email,Contact,Date_Created,LastLoggedIN):
    
    refresh()
    
    if Username in userIds:
        return "ID Already Exists"
    if Email in emails:
        return "Email Already Exists"
        
    Date_Created = datetime.datetime.combine(Date_Created, datetime.datetime.min.time())
    LastLoggedIN = datetime.datetime.combine(LastLoggedIN, datetime.datetime.min.time())
    
    data_list = {
        "Username":Username,
        "Password":Password,
        "Email":Email,
        "Contact":Contact,
        "Date_Created":Date_Created,
        "LastLoggedIN":LastLoggedIN,
        }
    
    global lastid
    usermainid = f"ID{lastid+1}"
    lastid +=1
    
    doc_ref = db_ref .document(usermainid)
    
    try:
        doc_ref.set(data_list)
        print(f"Document '{usermainid}' successfully written!")
        return f"Document successfully written!"
    
    except Exception as e:
        return f"An error occurred while writing document '{db_ref}': {e}"
    
refresh()

