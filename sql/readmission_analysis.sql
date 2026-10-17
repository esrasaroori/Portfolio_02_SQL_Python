SELECT
    SUM(CASE
        WHEN readmitted = '<30' THEN 1
        ELSE 0
    END) AS readmitted_within_30_days,

    COUNT(*) AS total_visits,

    ROUND(
        100.0 * SUM(CASE
            WHEN readmitted = '<30' THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS readmission_rate_pct

FROM diabetes_encounters;

SELECT
    age,
    COUNT(*) AS total_visits,

    SUM(
        CASE
            WHEN readmitted = '<30' THEN 1
            ELSE 0
        END
    ) AS readmitted_within_30_days,

    ROUND(
        100.0 * SUM(
            CASE
                WHEN readmitted = '<30' THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS readmission_rate_pct

FROM diabetes_encounters

GROUP BY age

ORDER BY readmission_rate_pct DESC;

SELECT
    time_in_hospital,
    COUNT(*) AS total_visits,

    SUM(
        CASE
            WHEN readmitted = '<30' THEN 1
            ELSE 0
        END
    ) AS readmitted_within_30_days,

    ROUND(
        100.0 * SUM(
            CASE
                WHEN readmitted = '<30' THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS readmission_rate_pct

FROM diabetes_encounters

GROUP BY time_in_hospital

ORDER BY time_in_hospital;