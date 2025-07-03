CREATE TABLE [sysLogs] (
    [RunId]            UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(), -- ID único
    [JobIb]            NVARCHAR(100)  NOT NULL,                      -- oracle_clientes, azure_contracts…
    [SourceConnection] NVARCHAR(100)  NULL,                          -- oracle, azure, sql34
    [TargetTable]      NVARCHAR(200)  NULL,                          -- stage.clientes
    [StartTime]        DATETIME2      NOT NULL DEFAULT SYSUTCDATETIME(),
    [EndTime]          DATETIME2      NULL,
    [Status]           NVARCHAR(20)   NULL,                          -- RUNNING / OK / ERROR
    [ErrorMsg]         NVARCHAR(4000) NULL
    );
GO

CREATE INDEX idx_etl_log_job_time
    ON [sysLogs] ([JobIb], [StartTime] DESC);
GO
