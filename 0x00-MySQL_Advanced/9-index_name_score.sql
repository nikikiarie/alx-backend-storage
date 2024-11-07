-- Creates an index on the first letter of the name and
-- the score in the names table.
CREATE INDEX idx_name_first_score ON names(name(1), score);
