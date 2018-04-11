SELECT
  MIN(f.repo_name),
  MIN(f.path),
  c.pbkey
FROM
  [bigquery-public-data:github_repos.files] f
JOIN (
  SELECT
    id,
    REGEXP_EXTRACT(content, r'(?:^|[^a-zA-Z0-9])(5[HJK][1-9a-km-zA-HJ-NP-Z]{48,49})(?:$|[^a-zA-Z0-9])') pbkey
  FROM
    [bigquery-public-data:github_repos.contents]
  WHERE
    REGEXP_MATCH(content, r'(?:^|[^a-zA-Z0-9])(5[HJK][1-9a-km-zA-HJ-NP-Z]{48,49})(?:$|[^a-zA-Z0-9])')) c
ON
  f.id = c.id
GROUP BY
  c.pbkey