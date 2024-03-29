USE RevolutionaryHarmony;

CREATE INDEX atitle_ind ON Albums(atitle);
CREATE INDEX lcountry_ind ON Labels(lcountry);

SET profiling = 1;
SELECT *
FROM Labels
JOIN Albums ON Labels.lid = Albums.lid
WHERE Labels.lcountry = "Sweden" AND Albums.atitle LIKE "%r%"
LIMIT 1000009;
SHOW PROFILE;