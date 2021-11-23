import dbase

#-----------------------Warning---------------------------. 
def databaseCreation():
    #use this code only for creating and then comment it. 
    dbase.createdb()
#----------------------Warning----------------------------.

#adding multiple records
def addingMulRecord():
    MovieList = []
    n = int(input("PLEASE ENTER NUMBER OF ENTRIES: "))
    print("PLEASE ENTER THE DETAILS AS: MOVIE_NAME, ACTOR_NAME, ACTRESS NAME, YEAR, DIRECTOR_NAME")
    for i in range(n):
        k = tuple(input().split())
        MovieList.append(k)
    dbase.addMany_record(MovieList)


#adding single records
def addingSingleRecord():
    movie = input("Please Enter Movie Name: ")
    actor = input("Please Enter Actor Name: ")
    actress = input("Please Enter Actress Name: ")
    year = input("Please Enter Year: ")
    director = input("Please Enter Director Name: ")
    dbase.add_record(movie, actor, actress, year, director)

#deleting Single record based on actor name.
def deletingActorRecord():
    Dactor = input("Please Enter the Actor name to delete his record: ")
    dbase.delete_record(Dactor)

#actor search
def ActorLookup():
    Factor = input("Please Enter The Actor Name for his movie details:  ")
    dbase.Lookup(Factor)

#show database
def ShowDB():
    print("THE MOVIE DATABASE IS: ")
    dbase.showall()

#drop table
def drop():
    dbase.droptable()

#interface
print("""1. Create DataBase(!NOTE: USE THIS FUNCTION ONLU ONCE!)
2. Add Multiple Records.
3. Add Single Record.
4. Delete Single Record.
5. Find Actor Details.
6. Show DATABASE.
7. Drop Table.
""")
Data = int(input())
if Data == 1:
    databaseCreation()
elif Data == 2:
    addingMulRecord()
    dbase.showall()
elif Data == 3:
    addingSingleRecord()
    dbase.showall()
elif Data == 4:
    deletingActorRecord()
    dbase.showall()
elif Data == 5:
    ActorLookup()
elif Data == 6:
    ShowDB()
elif Data == 7:
    drop()
else:
    print("PLEASE ENTER VALID NUMBER")



