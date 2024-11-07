-- List Glam bands by how long they've been together, ranked by years active
SELECT band_name, (IFNULL(split, YEAR(CURRENT_DATE())) - formed) AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
ORDER BY lifespan DESC;
