USE RevolutionaryHarmony;

CREATE INDEX rel_year_ind ON Albums(rel_year);
CREATE INDEX est_year_ind ON Labels(est_year);

SET profiling = 1;
SELECT *
FROM Labels
JOIN Albums ON Labels.lid = Albums.lid
WHERE Albums.rel_year > 2000 and Labels.est_year < 2000
LIMIT 1000009;
SHOW PROFILE;