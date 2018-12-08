import pickle
from datetime import date
from datetime import datetime
import os

cwd = os.getcwd()
tabooList = ["EVIL", "LIAR", "FAKE", "hello"]
pending = []  # words that are going to be added to the taboo list through user requests.
allDocuments = []
allUsers = []
uniqueIdUsers = -1
uniqueIdDocuments = -1
uniqueIdComplaint = -1


def searchByName(user, name):
    available = []
    if user._membership != "GUEST":
        for x in allUsers:
            if ((name.upper() == x._firstName.upper()) or (name.upper() == x._lastName.upper())):
                available.append(x)
                print(x._firstName)
                print(x._username)
                print(name.upper())
        return (available)
    return (available)


def searchByInterest(user, interest):
    available = []
    if user._membership != "GUEST":
        for x in allUsers:
            if interest.upper() in [y.upper() for y in x._interests]:
                available.append(x)
        return (available)
    return (available)


def saveUsers():
    global allUsers
    directory = cwd + "/meep/system/users"
    file_users = open(directory, 'wb')
    pickle.dump(allUsers, file_users)
    file_users.close()
    return


def saveIds():
    global uniqueIdComplaint
    global uniqueIdDocuments
    global uniqueIdUsers
    ids = [uniqueIdComplaint, uniqueIdDocuments, uniqueIdUsers]
    directory = cwd + "/meep/system/ids"
    file_ids = open(directory, 'wb')
    pickle.dump(ids, file_ids)
    file_ids.close()


def loadIds():
    global uniqueIdComplaint
    global uniqueIdDocuments
    global uniqueIdUsers
    global ids
    directory = cwd + "/meep/system/ids"
    file_ids = open(directory, 'rb')
    ids = pickle.load(file_ids)
    uniqueIdComplaint = ids[0]
    uniqueIdDocuments = ids[1]
    uniqueIdComplaint = ids[2]
    file_ids.close()


def saveDocuments():
    global allDocuments
    directory = cwd + "/meep/system/documents"
    file_doc = open(directory, 'wb')
    pickle.dump(allDocuments, file_doc)
    file_doc.close()
    return


def saveTabooList():
    global tabooList
    directory = cwd + "/meep/system/taboo"
    file_taboo_list = open(directory, 'wb')
    pickle.dump(tabooList, file_taboo_list)
    file_taboo_list.close()
    return


def loadUsers():
    global allUsers
    directory = cwd + "/meep/system/users"
    file_users = open(directory, 'rb')
    allUsers = pickle.load(file_users)
    for user in allUsers:
        globals()[user._username] = user
    file_users.close()
    return


def loadDocuments():
    global allDocuments
    directory = cwd + "/meep/system/documents"
    file_doc = open(directory, 'rb')
    allDocuments = pickle.load(file_doc)
    for document in allDocuments:
        globals()[document._documentName] = document
    file_doc.close()
    return


def loadTabooList():
    global tabooList
    directory = cwd + "/meep/system/taboo"
    file_taboo_list = open(directory, 'rb')
    tabooList = pickle.load(file_taboo_list)
    file_taboo_list.close()
    return


def savePending():
    global pending
    directory = cwd + "/meep/system/pending"
    file_pending = open(directory, 'wb')
    pickle.dump(pending, file_pending)
    file_pending.close()
    return


def loadPending():
    global pending
    directory = cwd + "/meep/system/pending"
    file_pending = open(directory, "rb")
    pending = pickle.load(file_pending)


def loadInformation():
    loadTabooList()
    loadUsers()
    loadDocuments()
    loadPending()
    return


def saveInformation():
    saveUsers()
    saveDocuments()
    saveTabooList()
    savePending()
    return


def searchOwnedDocuments(User, word):
    available = []
    for document in User._ownedDocuments:
        if word.upper() in [c.upper() for c in document._documentBody]:
            # print("Here",document._documentBody)
            available.append(document)
    return available


def blocked(User):  # Blocked function to check whether a user can do anything or if they have to fix a document
    if (User._blocked == True):
        print("Update document before you continue")
        return True
    else:
        return False


def timeStamp():
    return (str(date.today()) + " " + str(datetime.now().strftime("%X")))


def searchUsers():
    return


def suggestTaboo(word, su):
    if word in [x.upper() for x in tabooList]:
        return
    else:
        su._suggestions = 0
        pending.append(word)
        #    Add the possible taboo word to a place where the super user add it


def readOpenDocuments():  # returns a list of documents that have open as their privacy
    available = []
    for document in allDocuments:
        if document._privacy is document.privacies[0]:
            available.append(document)
    return available


def fileComplaint(Document, victim, target, Problem):  # helper Function
    global uniqueIdComplaint
    uniqueIdComplaint += 1
    globals()["Complaint_" + str(uniqueIdComplaint)] = Complaint(uniqueIdComplaint, victim, target,
                                                                 globals()[Document._owner], Problem, Document)
    globals()[Document._owner].addComplaint(((globals()["Complaint_" + str(uniqueIdComplaint)]), Document))
    return (((globals()["Complaint_" + str(uniqueIdComplaint)]), Document))


def storeComplaint(Document, victim, target, Problem):
    globals()[Document._owner]._complaints.append(fileComplaint(Document, victim, target, Problem))


class SuperUser:

    def __init__(self, username, name, password, interests):
        global uniqueIdUsers
        uniqueIdUsers += 1
        self._membership = str.upper("Super")
        self._username = username
        self._firstName = name[0]
        self._Lastname = name[1]
        self._blocked = False
        self._interests = [interest.upper() for interest in interests]
        self._requestPromotion = 0
        self._userDocumentRequests = []
        self._ownedDocuments = []
        self._id = uniqueIdUsers
        self._password = password
        self._suggestions = -1
        self._complaints = []
        allUsers.append(self)
        return

    def addComplaint(self, complaint):
        self._complaints.append(complaint)
        print(self._complaints)

    def promote(self, user):
        if str.upper(user._membership) == "GUEST":
            user._firstName = user._application[0][0]
            user._lastName = user._application[0][1]
            user._membership = "ORDINARY"
            user._interests = [x.upper() for x in user._application[1]]
            del user._application
            user._ownedDocuments = []
            user._complaints = []
            return
        elif str.upper(user._membership) == "ORDINARY":
            user._membership = "SUPER"
            return
        else:
            return

    def demote(self, User):
        if str.upper(User._membership) == "ORDINARY":
            User._membership = "GUEST"
            User._requestPromotion = 0
            return
        elif str.upper(User._membership) == "SUPER":
            User._membership = "ORDINARY"
            User._requestPromotion = 0
            return
        else:
            return

    def processComplaint(self, Complaint, OrdinaryUser):
        return

    def updateMembership(self, User):
        if (User._requestPromotion == 1):
            self.promote(User)
        elif (User._requestPromotion == -1):
            self.demote(User)
        else:
            return

    def updateTabooList(self, word):  # Check if the word is already in the taboo list,
        # otherwise add it to the list and remove it from all documents
        temp = [x.upper() for x in tabooList]
        # tabooList=[x.upper() for x in tabooList]
        if word.upper() in [x.upper() for x in tabooList]:
            return
        else:
            tabooList.append(word.upper())
        self.applyTabooList()

    def resolveSuggestions(self):  # add suggested taboo words to the taboo list
        global pending
        if self._suggestions is -1:
            return
        else:
            for word in pending:
                print(word)
                self.updateTabooList(word)
            del pending[:]
            self._suggestions = -1

    def applyTabooList(
            self):  # update all the taboo words from all existing documents and block users who added the word
        for document in allDocuments:
            dc = [word.upper() for word in document._documentBody]
            for word in dc:
                if word.upper() in [x.upper() for x in tabooList]:
                    document._documentBody[dc.index(word)] = "UNK"
        return


class Complaint:
    def __init__(self, id, Victim, Target, Owner, Problem,
                 Document):  # Both Complain and target are User types SU,OU,GU
        self._resolved = False
        self._id = id
        self._complaintBy = Victim._username
        self._complaintFor = Owner._username
        self._complaintAbout = Target._username
        self._Document = Document
        self._problem = Problem


class GuestUser:
    def __init__(self, username, password):
        global uniqueIdUsers
        uniqueIdUsers += 1
        self._membership = str.upper("GUEST")
        self._username = username
        self._password = password
        self._blocked = False
        self._requestPromotion = 0
        self._userDocumentRequests = []
        self._id = uniqueIdUsers
        self._application = []
        allUsers.append(self)
        return

    def applyToOrdinary(self, name, interests):
        self._application = [name, interests]
        self._requestPromotion = 1
        return


class OrdinaryUser:
    def __init__(self, username, name, password, interests):
        global uniqueIdUsers
        uniqueIdUsers = uniqueIdUsers+1
        self._membership = str.upper("ORDINARY")
        self._username = username
        self._blocked = False
        self._requestPromotion = 0
        self._firstName = name[0]
        self._lastName = name[1]
        self._userDocumentRequests = []
        self._interests = [interest.upper() for interest in interests]
        self._ownedDocuments = []
        self._id = uniqueIdUsers
        self._password = password
        self._complaints = []
        allUsers.append(self)
        return


class Document:
    privacies = {0: "OPEN", 1: "RESTRICTED", 2: "SHARED", 3: "PRIVATE"}

    def __init__(self, documentName, User):
        global uniqueIdDocuments
        uniqueIdDocuments += 1
        self._privacy = self.privacies[3]
        self._lock = False
        self._documentName = documentName
        self._owner = User._username
        self._lockedBy = User._username
        self._unlockedBy = ""
        self._users = [User._username]
        self._documentBody = []  # DocumentBody will always be the current version
        self._id = uniqueIdDocuments
        self._versionHistory = [(0, "CREATE", self._documentBody.copy(), self._owner, timeStamp())]
        # self._versionHistory[-1] is also the current versoin/latest
        User._ownedDocuments.append(self)
        allDocuments.append(self)

    def unlockDocument(self,
                       User):  # Unlock the document, only the super user can unlock the document regardless of who locked it
        # otherwise document can be unlocked by whoever locked it or the owner
        if ((str.upper(User._membership) == "SUPER") & self._lock == True):  # unlock the document if you are super user
            self._lock = False
            self._unlockedBy = User._username
            self._lockedBy = ""
        else:
            if self._lock == True:  # unlock the document if you are the owner
                if self._owner == User._username:
                    self._lock = False
                    self._unlockedBy = User._username
                    self._lockedBy = ""
                else:
                    if self._lockedBy == User._username:  # if you are not the owner then unlock the document if you locked it initially
                        self._lock = False
                        self._unlockedBy = User._username
                        self._lockedBy = ""
                    else:
                        return
            else:  # Document isn't locked
                return

    def lockDocument(self, User):  # lock the document that can be done by anyone
        if (self._lock == False):
            self._lock = True
            self._lockedBy = User._username
            self._unlockedBy = ""
        else:
            return

    def invite(self, Owner, User):
        if (Owner._username == self._owner):
            if (self._documentName, User._username) in Owner._userDocumentRequests:
                self._users.append(User._username)
                Owner._userDocumentRequests.remove((self._documentName, User._username))
                return
            else:
                return
        else:
            return

    def requestPermission(self, Owner, User):
        if (Owner._username == self._owner):
            if User._username not in self._users:
                Owner._userDocumentRequests.append((self._documentName, User._username))
            else:
                return
        else:
            return

    def add(self, Word, User):
        self._documentBody.append(Word)
        su.applyTabooList()
        self._versionHistory.append(
            (len(self._versionHistory), "ADD", self._documentBody.copy(), User._username, timeStamp()))
        return

    def delete(self, index, User):
        if len(self._documentBody) >= index:
            del self._documentBody[index]
            self._versionHistory.append(
                (len(self._versionHistory), "DELETE", self._documentBody.copy(), User._username, timeStamp()))
        else:
            return

    def update(self, User, index, word):
        if len(self._documentBody) >= index:
            self._documentBody[index] = word
            su.applyTabooList()
            self._versionHistory.append(
                (len(self._versionHistory), "UPDATE", self._documentBody.copy(), User._username, timeStamp()))
        return

    def denyInvitation(self, Owner, User):
        if (self._documentName, User._username) in Owner._userDocumentRequests:
            del Owner._userDocumentRequests[(Owner._userDocumentRequests.index((self._documentName, User._username)))]
        return

    def acceptInvitation(self, Owner, User):
        if (self._documentName, User._username) in Owner._userDocumentRequests:
            del Owner._userDocumentRequests[(Owner._userDocumentRequests.index((self._documentName, User._username)))]
            self._users.append(User._username)
            self._privacy = self.privacies[2]
        return


su = SuperUser("su", ["Super", "User"], "root", ["Algorithms", "Minecraft", "Pokemon"])
# loadUsers()

