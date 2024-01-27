USE RevolutionaryHarmony;

SET profiling = 1;
SELECT *
FROM Labels
JOIN Albums ON Labels.lid = Albums.lid
WHERE Albums.rel_year > 2000 and Labels.est_year < 2000
LIMIT 1000009;
SHOW PROFILE;