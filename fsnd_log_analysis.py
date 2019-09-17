#!/usr/bin/env python3

import psycopg2
import datetime

databaseName = "news"


def question1():
    """Print the top three articles by views.
    Prints a list of article titles, along with the number of views each title
    has, ordered by the number of views. Only the top three are printed. The
    list is printed to the console.
    """
    try:
        statement = """
                    select articles.title article, count(log.id)
                    as hits from articles left join log on log.path
                    like concat('%',articles.slug) group by article
                    order by hits desc limit 3;
                    """
        db = psycopg2.connect(database=databaseName)
        cursor = db.cursor()
        cursor.execute(statement)
        rs = cursor.fetchall()
        print("1)What are the most popular three articles of all time?:\n ")

        for row in rs:
            article = row[0]
            hits = row[1]
            print(article + " received " + str(hits) + " total Hits.")

    except (Exception, psycopg2.Error) as error:
        print("DB Error", error)

    finally:
        # closing db connection.
        if(cursor):
            cursor.close()
            db.close()


def question2():
    """Print the top authors of articles by views.
    Prints a list of author names, along with the number of views each author
    has, ordered by the number of views.The list is printed to the console."""
    try:
        statement = """
                    select authors.name, count(log.id) as hits
                    from authors left join articles on authors.id =
                    articles.author left join log on log.path like
                    concat('%',articles.slug) group by authors.name
                    order by hits desc;
                    """
        db = psycopg2.connect(database=databaseName)
        cursor = db.cursor()
        cursor.execute(statement)
        rs = cursor.fetchall()
        print("2)Who are the most popular article authors of all time:\n ")

        for row in rs:
            author = row[0]
            hits = row[1]
            print(author + " received " + str(hits) + " total Hits.")

    except (Exception, psycopg2.Error) as error:
        print("DB Error", error)

    finally:
        # closing db connection.
        if(cursor):
            cursor.close()
            db.close()


def question3():
    """Print the day and error percent.
    Print the day and error percent where
    errors occured more than 1% of total requests for that day.
    The list is printed to the console."""
    try:
        statement = """
                       SELECT TO_CHAR(days :: DATE, 'Mon dd, yyyy'),
                       round( CAST(float8 (ERROR*1.0/TOTAL)*100.0 as numeric),
                       2) Percentage FROM (select date(date_trunc('day',time))
                       days, COUNT(case when status = '404 NOT FOUND' then 1
                       ELSE NULL END) ERROR, COUNT(1) TOTAL from log group by
                       date(date_trunc('day',time))) A where
                       round( CAST(float8 (ERROR*1.0/TOTAL)*100.0
                       as numeric), 2) > 1;
                       """
        db = psycopg2.connect(database=databaseName)
        cursor = db.cursor()
        cursor.execute(statement)
        rs = cursor.fetchall()
        print("3)On which days did more than 1% requests lead to errors:\n ")

        for row in rs:
            errorDate = row[0]
            errors = str(row[1])
            print(errorDate + ", " + errors + "% Errors.")

    except (Exception, psycopg2.Error) as error:
        print("DB Error", error)

    finally:
        # closing db connection.
        if(cursor):
            cursor.close()
            db.close()

question1()
question2()
question3()
