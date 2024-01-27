USE RevolutionaryHarmony;

INSERT INTO Labels VALUES (1, "Columbia Records", "https://www.columbiarecords.com/", "USA", 1889);
INSERT INTO Labels VALUES (2, "Kalan Muzik", "https://kalan.com/", "Turkey", 1991);
INSERT INTO Labels VALUES (3, "Seyhan Muzik", "http://www.seyhanmuzik.com/", "Turkey", 1987);
INSERT INTO Labels VALUES (4, "EMRE", "https://www.emreplak.com.tr/", "Turkey", 1970);
INSERT INTO Labels VALUES (5, "Elektra Records", "https://www.elektra.com/", "USA", 1950);
INSERT INTO Labels VALUES (6, "RMV Grammofon", "https://rmvgrammofon.com/", "Sweden", 2010);
INSERT INTO Labels VALUES (7, "Liberation Records", "http://www.liberationrecords.com/", "USA", 1994);
INSERT INTO Labels VALUES (8, "Yavuz Burc Plakcilik", "http://www.yavuzburcplak.com", "Turkey", 1961);
INSERT INTO Labels VALUES (9, "Smithsonian Folkways", "https://folkways.si.edu/", "USA", 1987);

INSERT INTO Artists VALUES (1, "Person", "Pete Seeger", "USA", 1940);
INSERT INTO Artists VALUES (2, "Band", "Grup Yorum", "Turkey", 1985);
INSERT INTO Artists VALUES (3, "Band", "Dinmeyen", "Turkey", 1991);
INSERT INTO Artists VALUES (4, "Band", "Mogollar", "Turkey", 1967);
INSERT INTO Artists VALUES (5, "Person", "Phil Ochs", "USA", 1962);
INSERT INTO Artists VALUES (6, "Choir", "Socialdemokraternas Jubileumskor", "Sweden", 2019);
INSERT INTO Artists VALUES (7, "Person", "Billy Bragg", "UK", 1977);
INSERT INTO Artists VALUES (8, "Person", "Cem Karaca", "Turkey", 1961);
INSERT INTO Artists VALUES (9, "Person", "Joan Baez", "USA", 1958);
INSERT INTO Artists VALUES (10, "Person", "Nathalie Cardone", "France", 1988);

INSERT INTO Albums VALUES (1, "I Can See a New Day (Live)", 1964, 1, 1);
INSERT INTO Albums VALUES (2, "Ille Kavga", 2017, 2, 2);
INSERT INTO Albums VALUES (3, "Sisler Bulvari", 2006, 3, 3);
INSERT INTO Albums VALUES (4, "Dort Renk", 1996, 4, 4);
INSERT INTO Albums VALUES (5, "Phil Ochs in Concert", 1966, 5, 5);
INSERT INTO Albums VALUES (6, "Pa ratt sida av historien", 2019, 6, 6);
INSERT INTO Albums VALUES (7, "The Internationale", 1990, 7, 7);
INSERT INTO Albums VALUES (8, "Haziranda Olmek Zor / Berivan", 1991, 2, 2);
INSERT INTO Albums VALUES (9, "Nerdesin", 1975, 8, 8);
INSERT INTO Albums VALUES (10, "If I Had a Hammer: Songs of Hope and Struggle", 1998, 9, 1);

SELECT * FROM Albums;
SELECT * FROM Artists;

SELECT deb_year
FROM Albums Alb JOIN Artists Art ON Alb.artid = Art.artid;

SELECT Art.acountry, Art.aname, COUNT(Alb.albid)
FROM Artists Art JOIN Albums Alb ON Art.artid = Alb.artid
GROUP BY Art.acountry, Art.aname;

-- Do not execute the section below -  they will not work.
ALTER TABLE Albums
ADD CONSTRAINT Unique_Release_Year CHECK (
    NOT EXISTS (SELECT *
                FROM Albums A
                WHERE A.artid = artid AND A.rel_year = rel_year AND A.albid != albid)
);

INSERT INTO Albums VALUES (11, "New Album", 1998, 9, 1);