from sqlite3 import Error
import sqlite3


conn = sqlite3.connect('jokes_db.db')
c = conn.cursor()


def add_joke(joke_title, joke_body, joke_url, joke_author):
    print(joke_title, joke_body)
    c.execute("INSERT INTO jokes_list (title,selftext,url,author) VALUES(?,?,?,?)",(joke_title, joke_body, joke_url, joke_author))
    conn.commit()

# def saved():
#     conn = sqlite3.connect('jokes_db.db')
#     c = conn.cursor()
#     c.execute("SELECT id, Title from jokes_list")
#     rows = c.fetchall()
#     for row in rows:
#         print(row)

# saved()






