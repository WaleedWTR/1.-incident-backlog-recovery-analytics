-- Breached tickets
SELECT *
FROM incidents
WHERE status IN ('Open', 'Pending')
  AND current_timestamp > opened_at + (sla_target_hours * INTERVAL '1 hour')
ORDER BY priority, opened_at;

-- Oldest open tickets by resolver
SELECT
    resolver,
    COUNT(*) AS open_tickets,
    MIN(opened_at) AS oldest_opened
FROM incidents
WHERE status IN ('Open', 'Pending')
GROUP BY resolver
ORDER BY oldest_opened;

-- Backlog by priority
SELECT
    priority,
    COUNT(*) AS ticket_count
FROM incidents
WHERE status IN ('Open', 'Pending')
GROUP BY priority
ORDER BY priority;
