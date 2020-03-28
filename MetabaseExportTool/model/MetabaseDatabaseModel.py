from peewee import *


class Config(object):
    database_proxy = DatabaseProxy()

    def __init__(self, database):
        Config.database_proxy.initialize(database)  # Create a proxy for our db.


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = Config.database_proxy  # Use proxy for our DB.


class CoreUser(BaseModel):
    date_joined = DateTimeField()
    email = CharField(unique=True)
    first_name = CharField()
    google_auth = BooleanField(constraints=[SQL("DEFAULT false")])
    is_active = BooleanField()
    is_qbnewb = BooleanField(constraints=[SQL("DEFAULT true")])
    is_superuser = BooleanField()
    last_login = DateTimeField(null=True)
    last_name = CharField()
    ldap_auth = BooleanField(constraints=[SQL("DEFAULT false")])
    login_attributes = TextField(null=True)
    password = CharField()
    password_salt = CharField(constraints=[SQL("DEFAULT 'default'::character varying")])
    reset_token = CharField(null=True)
    reset_triggered = BigIntegerField(null=True)
    updated_at = DateTimeField(null=True)

    class Meta:
        table_name = 'core_user'


class Activity(BaseModel):
    custom_id = CharField(index=True, null=True)
    database_id = IntegerField(null=True)
    details = CharField()
    model = CharField(null=True)
    model_id = IntegerField(null=True)
    table_id = IntegerField(null=True)
    timestamp = DateTimeField(index=True)
    topic = CharField()
    user = ForeignKeyField(column_name='user_id', field='id', model=CoreUser, null=True)

    class Meta:
        table_name = 'activity'


class Collection(BaseModel):
    archived = BooleanField(constraints=[SQL("DEFAULT false")])
    color = CharField()
    description = TextField(null=True)
    location = CharField(constraints=[SQL("DEFAULT '/'::character varying")], index=True)
    name = TextField()
    personal_owner = ForeignKeyField(column_name='personal_owner_id', field='id', model=CoreUser, null=True)
    slug = CharField()

    class Meta:
        table_name = 'collection'


class MetabaseDatabase(BaseModel):
    auto_run_queries = BooleanField(constraints=[SQL("DEFAULT true")])
    cache_field_values_schedule = CharField(constraints=[SQL("DEFAULT '0 50 0 * * ? *'::character varying")])
    caveats = TextField(null=True)
    created_at = DateTimeField()
    description = TextField(null=True)
    details = TextField(null=True)
    engine = CharField()
    is_full_sync = BooleanField(constraints=[SQL("DEFAULT true")])
    is_on_demand = BooleanField(constraints=[SQL("DEFAULT false")])
    is_sample = BooleanField(constraints=[SQL("DEFAULT false")])
    metadata_sync_schedule = CharField(constraints=[SQL("DEFAULT '0 50 * * * ? *'::character varying")])
    name = CharField()
    options = TextField(null=True)
    points_of_interest = TextField(null=True)
    timezone = CharField(null=True)
    updated_at = DateTimeField()

    class Meta:
        table_name = 'metabase_database'


class MetabaseTable(BaseModel):
    active = BooleanField()
    caveats = TextField(null=True)
    created_at = DateTimeField()
    db = ForeignKeyField(column_name='db_id', field='id', model=MetabaseDatabase)
    description = TextField(null=True)
    display_name = CharField(null=True)
    entity_name = CharField(null=True)
    entity_type = CharField(null=True)
    fields_hash = TextField(null=True)
    name = CharField()
    points_of_interest = TextField(null=True)
    rows = BigIntegerField(null=True)
    schema = CharField(null=True)
    show_in_getting_started = BooleanField(constraints=[SQL("DEFAULT false")], index=True)
    updated_at = DateTimeField()
    visibility_type = CharField(null=True)

    class Meta:
        table_name = 'metabase_table'
        indexes = (
            (('name', 'db'), True),
            (('name', 'db', 'schema'), True),
            (('schema', 'db'), False),
        )


class ReportCard(BaseModel):
    archived = BooleanField(constraints=[SQL("DEFAULT false")])
    cache_ttl = IntegerField(null=True)
    collection = ForeignKeyField(column_name='collection_id', field='id', model=Collection, null=True)
    collection_position = SmallIntegerField(null=True)
    created_at = DateTimeField()
    creator = ForeignKeyField(column_name='creator_id', field='id', model=CoreUser)
    database = ForeignKeyField(column_name='database_id', field='id', model=MetabaseDatabase, null=True)
    dataset_query = TextField()
    description = TextField(null=True)
    display = CharField()
    embedding_params = TextField(null=True)
    enable_embedding = BooleanField(constraints=[SQL("DEFAULT false")])
    made_public_by = ForeignKeyField(backref='core_user_made_public_by_set', column_name='made_public_by_id',
                                     field='id', model=CoreUser, null=True)
    name = CharField()
    public_uuid = CharField(index=True, null=True)
    query_type = CharField(null=True)
    read_permissions = TextField(null=True)
    result_metadata = TextField(null=True)
    table = ForeignKeyField(column_name='table_id', field='id', model=MetabaseTable, null=True)
    updated_at = DateTimeField()
    visualization_settings = TextField()

    class Meta:
        table_name = 'report_card'


class Label(BaseModel):
    icon = CharField(null=True)
    name = CharField()
    slug = CharField(index=True)

    class Meta:
        table_name = 'label'


class CardLabel(BaseModel):
    card = ForeignKeyField(column_name='card_id', field='id', model=ReportCard)
    label = ForeignKeyField(column_name='label_id', field='id', model=Label)

    class Meta:
        table_name = 'card_label'
        indexes = (
            (('card', 'label'), True),
        )


class CollectionRevision(BaseModel):
    after = TextField()
    before = TextField()
    created_at = DateTimeField()
    remark = TextField(null=True)
    user = ForeignKeyField(column_name='user_id', field='id', model=CoreUser)

    class Meta:
        table_name = 'collection_revision'


class ComputationJob(BaseModel):
    context = TextField(null=True)
    created_at = DateTimeField()
    creator = ForeignKeyField(column_name='creator_id', field='id', model=CoreUser, null=True)
    ended_at = DateTimeField(null=True)
    status = CharField()
    type = CharField()
    updated_at = DateTimeField()

    class Meta:
        table_name = 'computation_job'


class ComputationJobResult(BaseModel):
    created_at = DateTimeField()
    job = ForeignKeyField(column_name='job_id', field='id', model=ComputationJob)
    payload = TextField()
    permanence = CharField()
    updated_at = DateTimeField()

    class Meta:
        table_name = 'computation_job_result'


class CoreSession(BaseModel):
    created_at = DateTimeField()
    id = CharField(primary_key=True)
    user = ForeignKeyField(column_name='user_id', field='id', model=CoreUser)

    class Meta:
        table_name = 'core_session'


class ReportDashboard(BaseModel):
    archived = BooleanField(constraints=[SQL("DEFAULT false")])
    caveats = TextField(null=True)
    collection = ForeignKeyField(column_name='collection_id', field='id', model=Collection, null=True)
    collection_position = SmallIntegerField(null=True)
    created_at = DateTimeField()
    creator = ForeignKeyField(column_name='creator_id', field='id', model=CoreUser)
    description = TextField(null=True)
    embedding_params = TextField(null=True)
    enable_embedding = BooleanField(constraints=[SQL("DEFAULT false")])
    made_public_by = ForeignKeyField(backref='core_user_made_public_by_set', column_name='made_public_by_id',
                                     field='id', model=CoreUser, null=True)
    name = CharField()
    parameters = TextField()
    points_of_interest = TextField(null=True)
    position = IntegerField(null=True)
    public_uuid = CharField(index=True, null=True)
    show_in_getting_started = BooleanField(constraints=[SQL("DEFAULT false")], index=True)
    updated_at = DateTimeField()

    class Meta:
        table_name = 'report_dashboard'


class DashboardFavorite(BaseModel):
    dashboard = ForeignKeyField(column_name='dashboard_id', field='id', model=ReportDashboard)
    user = ForeignKeyField(column_name='user_id', field='id', model=CoreUser)

    class Meta:
        table_name = 'dashboard_favorite'
        indexes = (
            (('user', 'dashboard'), True),
        )


class ReportDashboardcard(BaseModel):
    card = ForeignKeyField(column_name='card_id', field='id', model=ReportCard, null=True)
    col = IntegerField(constraints=[SQL("DEFAULT 0")])
    created_at = DateTimeField()
    dashboard = ForeignKeyField(column_name='dashboard_id', field='id', model=ReportDashboard)
    parameter_mappings = TextField()
    row = IntegerField(constraints=[SQL("DEFAULT 0")])
    size_x = IntegerField(column_name='sizeX')
    size_y = IntegerField(column_name='sizeY')
    updated_at = DateTimeField()
    visualization_settings = TextField()

    class Meta:
        table_name = 'report_dashboardcard'


class DashboardcardSeries(BaseModel):
    card = ForeignKeyField(column_name='card_id', field='id', model=ReportCard)
    dashboardcard = ForeignKeyField(column_name='dashboardcard_id', field='id', model=ReportDashboardcard)
    position = IntegerField()

    class Meta:
        table_name = 'dashboardcard_series'


class DataMigrations(BaseModel):
    id = CharField(primary_key=True)
    timestamp = DateTimeField()

    class Meta:
        table_name = 'data_migrations'


class Databasechangelog(BaseModel):
    author = CharField()
    comments = CharField(null=True)
    contexts = CharField(null=True)
    dateexecuted = DateTimeField()
    deployment_id = CharField(null=True)
    description = CharField(null=True)
    exectype = CharField()
    filename = CharField()
    id = CharField()
    labels = CharField(null=True)
    liquibase = CharField(null=True)
    md5sum = CharField(null=True)
    orderexecuted = IntegerField()
    tag = CharField(null=True)

    class Meta:
        table_name = 'databasechangelog'
        indexes = (
            (('id', 'author', 'filename'), True),
        )
        primary_key = False


class Databasechangeloglock(BaseModel):
    locked = BooleanField()
    lockedby = CharField(null=True)
    lockgranted = DateTimeField(null=True)

    class Meta:
        table_name = 'databasechangeloglock'


class Dependency(BaseModel):
    created_at = DateTimeField()
    dependent_on_id = IntegerField(index=True)
    dependent_on_model = CharField(index=True)
    model = CharField(index=True)
    model_id = IntegerField(index=True)

    class Meta:
        table_name = 'dependency'


class MetabaseField(BaseModel):
    active = BooleanField(constraints=[SQL("DEFAULT true")])
    base_type = CharField()
    caveats = TextField(null=True)
    created_at = DateTimeField()
    database_type = TextField()
    description = TextField(null=True)
    display_name = CharField(null=True)
    fingerprint = TextField(null=True)
    fingerprint_version = IntegerField(constraints=[SQL("DEFAULT 0")])
    fk_target_field_id = IntegerField(null=True)
    has_field_values = TextField(null=True)
    last_analyzed = DateTimeField(null=True)
    name = CharField()
    parent = ForeignKeyField(column_name='parent_id', field='id', model='self', null=True)
    points_of_interest = TextField(null=True)
    position = IntegerField(constraints=[SQL("DEFAULT 0")])
    preview_display = BooleanField(constraints=[SQL("DEFAULT true")])
    settings = TextField(null=True)
    special_type = CharField(null=True)
    table = ForeignKeyField(column_name='table_id', field='id', model=MetabaseTable)
    updated_at = DateTimeField()
    visibility_type = CharField(constraints=[SQL("DEFAULT 'normal'::character varying")])

    class Meta:
        table_name = 'metabase_field'
        indexes = (
            (('name', 'table'), True),
            (('parent', 'name', 'table'), True),
        )


class Dimension(BaseModel):
    created_at = DateTimeField()
    field = ForeignKeyField(column_name='field_id', field='id', model=MetabaseField)
    human_readable_field = ForeignKeyField(backref='metabase_field_human_readable_field_set',
                                           column_name='human_readable_field_id', field='id', model=MetabaseField,
                                           null=True)
    name = CharField()
    type = CharField()
    updated_at = DateTimeField()

    class Meta:
        table_name = 'dimension'
        indexes = (
            (('field', 'name'), True),
        )


class ExportField(BaseModel):
    active = BooleanField(null=True)
    base_type = CharField(null=True)
    caveats = TextField(null=True)
    created_at = DateTimeField(null=True)
    database_type = TextField(null=True)
    description = TextField(null=True)
    display_name = CharField(null=True)
    fingerprint = TextField(null=True)
    fingerprint_version = IntegerField(null=True)
    fk_target_field_id = IntegerField(null=True)
    has_field_values = TextField(null=True)
    id = IntegerField(null=True)
    last_analyzed = DateTimeField(null=True)
    name = CharField(null=True)
    parent_id = IntegerField(null=True)
    points_of_interest = TextField(null=True)
    position = IntegerField(null=True)
    preview_display = BooleanField(null=True)
    settings = TextField(null=True)
    special_type = CharField(null=True)
    table_id = IntegerField(null=True)
    updated_at = DateTimeField(null=True)
    visibility_type = CharField(null=True)

    class Meta:
        table_name = 'export_field'
        primary_key = False


class ExportTable(BaseModel):
    active = BooleanField(null=True)
    caveats = TextField(null=True)
    created_at = DateTimeField(null=True)
    db_id = IntegerField(null=True)
    description = TextField(null=True)
    display_name = CharField(null=True)
    entity_name = CharField(null=True)
    entity_type = CharField(null=True)
    fields_hash = TextField(null=True)
    id = IntegerField(null=True)
    name = CharField(null=True)
    points_of_interest = TextField(null=True)
    rows = BigIntegerField(null=True)
    schema = CharField(null=True)
    show_in_getting_started = BooleanField(null=True)
    updated_at = DateTimeField(null=True)
    visibility_type = CharField(null=True)

    class Meta:
        table_name = 'export_table'
        primary_key = False


class MetabaseFieldvalues(BaseModel):
    created_at = DateTimeField()
    field = ForeignKeyField(column_name='field_id', field='id', model=MetabaseField)
    human_readable_values = TextField(null=True)
    updated_at = DateTimeField()
    values = TextField(null=True)

    class Meta:
        table_name = 'metabase_fieldvalues'


class Metric(BaseModel):
    archived = BooleanField(constraints=[SQL("DEFAULT false")])
    caveats = TextField(null=True)
    created_at = DateTimeField()
    creator = ForeignKeyField(column_name='creator_id', field='id', model=CoreUser)
    definition = TextField()
    description = TextField(null=True)
    how_is_this_calculated = TextField(null=True)
    name = CharField()
    points_of_interest = TextField(null=True)
    show_in_getting_started = BooleanField(constraints=[SQL("DEFAULT false")], index=True)
    table = ForeignKeyField(column_name='table_id', field='id', model=MetabaseTable)
    updated_at = DateTimeField()

    class Meta:
        table_name = 'metric'


class MetricImportantField(BaseModel):
    field = ForeignKeyField(column_name='field_id', field='id', model=MetabaseField)
    metric = ForeignKeyField(column_name='metric_id', field='id', model=Metric)

    class Meta:
        table_name = 'metric_important_field'
        indexes = (
            (('metric', 'field'), True),
        )


class PermissionsGroup(BaseModel):
    name = CharField(index=True)

    class Meta:
        table_name = 'permissions_group'


class Permissions(BaseModel):
    group = ForeignKeyField(column_name='group_id', field='id', model=PermissionsGroup)
    object = CharField(index=True)

    class Meta:
        table_name = 'permissions'
        indexes = (
            (('group', 'object'), False),
            (('group', 'object'), True),
        )


class PermissionsGroupMembership(BaseModel):
    group = ForeignKeyField(column_name='group_id', field='id', model=PermissionsGroup)
    user = ForeignKeyField(column_name='user_id', field='id', model=CoreUser)

    class Meta:
        table_name = 'permissions_group_membership'
        indexes = (
            (('user', 'group'), False),
            (('user', 'group'), True),
        )


class PermissionsRevision(BaseModel):
    after = TextField()
    before = TextField()
    created_at = DateTimeField()
    remark = TextField(null=True)
    user = ForeignKeyField(column_name='user_id', field='id', model=CoreUser)

    class Meta:
        table_name = 'permissions_revision'


class Pulse(BaseModel):
    alert_above_goal = BooleanField(null=True)
    alert_condition = CharField(null=True)
    alert_first_only = BooleanField(null=True)
    archived = BooleanField(constraints=[SQL("DEFAULT false")], null=True)
    collection = ForeignKeyField(column_name='collection_id', field='id', model=Collection, null=True)
    collection_position = SmallIntegerField(null=True)
    created_at = DateTimeField()
    creator = ForeignKeyField(column_name='creator_id', field='id', model=CoreUser)
    name = CharField(null=True)
    skip_if_empty = BooleanField(constraints=[SQL("DEFAULT false")])
    updated_at = DateTimeField()

    class Meta:
        table_name = 'pulse'


class PulseCard(BaseModel):
    card = ForeignKeyField(column_name='card_id', field='id', model=ReportCard)
    include_csv = BooleanField(constraints=[SQL("DEFAULT false")])
    include_xls = BooleanField(constraints=[SQL("DEFAULT false")])
    position = IntegerField()
    pulse = ForeignKeyField(column_name='pulse_id', field='id', model=Pulse)

    class Meta:
        table_name = 'pulse_card'


class PulseChannel(BaseModel):
    channel_type = CharField()
    created_at = DateTimeField()
    details = TextField()
    enabled = BooleanField(constraints=[SQL("DEFAULT true")])
    pulse = ForeignKeyField(column_name='pulse_id', field='id', model=Pulse)
    schedule_day = CharField(null=True)
    schedule_frame = CharField(null=True)
    schedule_hour = IntegerField(null=True)
    schedule_type = CharField(index=True)
    updated_at = DateTimeField()

    class Meta:
        table_name = 'pulse_channel'


class PulseChannelRecipient(BaseModel):
    pulse_channel = ForeignKeyField(column_name='pulse_channel_id', field='id', model=PulseChannel)
    user = ForeignKeyField(column_name='user_id', field='id', model=CoreUser)

    class Meta:
        table_name = 'pulse_channel_recipient'


class QrtzJobDetails(BaseModel):
    description = CharField(null=True)
    is_durable = BooleanField()
    is_nonconcurrent = BooleanField()
    is_update_data = BooleanField()
    job_class_name = CharField()
    job_data = BlobField(null=True)
    job_group = CharField()
    job_name = CharField()
    requests_recovery = BooleanField()
    sched_name = CharField()

    class Meta:
        table_name = 'qrtz_job_details'
        indexes = (
            (('job_group', 'sched_name'), False),
            (('job_name', 'job_group', 'sched_name'), True),
            (('requests_recovery', 'sched_name'), False),
        )
        primary_key = CompositeKey('job_group', 'job_name', 'sched_name')


class QrtzTriggers(BaseModel):
    calendar_name = CharField(null=True)
    description = CharField(null=True)
    end_time = BigIntegerField(null=True)
    job_data = BlobField(null=True)
    job_group = ForeignKeyField(backref='qrtz_job_details_job_group_set', column_name='job_group', field='sched_name',
                                model=QrtzJobDetails)
    job_name = ForeignKeyField(backref='qrtz_job_details_job_name_set', column_name='job_name', field='sched_name',
                               model=QrtzJobDetails)
    misfire_instr = SmallIntegerField(null=True)
    next_fire_time = BigIntegerField(null=True)
    prev_fire_time = BigIntegerField(null=True)
    priority = IntegerField(null=True)
    sched_name = ForeignKeyField(backref='qrtz_job_details_sched_name_set', column_name='sched_name',
                                 field='sched_name', model=QrtzJobDetails)
    start_time = BigIntegerField()
    trigger_group = CharField()
    trigger_name = CharField()
    trigger_state = CharField()
    trigger_type = CharField()

    class Meta:
        table_name = 'qrtz_triggers'
        indexes = (
            (('calendar_name', 'sched_name'), False),
            (('job_group', 'sched_name'), False),
            (('job_name', 'job_group', 'sched_name'), False),
            (('next_fire_time', 'sched_name'), False),
            (('next_fire_time', 'sched_name', 'misfire_instr'), False),
            (('next_fire_time', 'sched_name', 'misfire_instr', 'trigger_state'), False),
            (('sched_name', 'trigger_group'), False),
            (('trigger_group', 'trigger_name', 'sched_name'), True),
            (('trigger_name', 'trigger_group', 'trigger_state', 'sched_name'), False),
            (('trigger_state', 'next_fire_time', 'sched_name', 'trigger_group', 'misfire_instr'), False),
            (('trigger_state', 'sched_name'), False),
            (('trigger_state', 'sched_name', 'next_fire_time'), False),
            (('trigger_state', 'sched_name', 'trigger_group'), False),
        )
        primary_key = CompositeKey('sched_name', 'trigger_group', 'trigger_name')


class QrtzBlobTriggers(BaseModel):
    blob_data = BlobField(null=True)
    sched_name = ForeignKeyField(backref='qrtz_triggers_sched_name_set', column_name='sched_name', field='trigger_name',
                                 model=QrtzTriggers)
    trigger_group = ForeignKeyField(backref='qrtz_triggers_trigger_group_set', column_name='trigger_group',
                                    field='trigger_name', model=QrtzTriggers)
    trigger_name = ForeignKeyField(backref='qrtz_triggers_trigger_name_set', column_name='trigger_name',
                                   field='trigger_name', model=QrtzTriggers)

    class Meta:
        table_name = 'qrtz_blob_triggers'
        indexes = (
            (('sched_name', 'trigger_name', 'trigger_group'), True),
        )
        primary_key = CompositeKey('sched_name', 'trigger_group', 'trigger_name')


class QrtzCalendars(BaseModel):
    calendar = BlobField()
    calendar_name = CharField()
    sched_name = CharField()

    class Meta:
        table_name = 'qrtz_calendars'
        indexes = (
            (('sched_name', 'calendar_name'), True),
        )
        primary_key = CompositeKey('calendar_name', 'sched_name')


class QrtzCronTriggers(BaseModel):
    cron_expression = CharField()
    sched_name = ForeignKeyField(backref='qrtz_triggers_sched_name_set', column_name='sched_name', field='trigger_name',
                                 model=QrtzTriggers)
    time_zone_id = CharField(null=True)
    trigger_group = ForeignKeyField(backref='qrtz_triggers_trigger_group_set', column_name='trigger_group',
                                    field='trigger_name', model=QrtzTriggers)
    trigger_name = ForeignKeyField(backref='qrtz_triggers_trigger_name_set', column_name='trigger_name',
                                   field='trigger_name', model=QrtzTriggers)

    class Meta:
        table_name = 'qrtz_cron_triggers'
        indexes = (
            (('sched_name', 'trigger_name', 'trigger_group'), True),
        )
        primary_key = CompositeKey('sched_name', 'trigger_group', 'trigger_name')


class QrtzFiredTriggers(BaseModel):
    entry_id = CharField()
    fired_time = BigIntegerField()
    instance_name = CharField()
    is_nonconcurrent = BooleanField(null=True)
    job_group = CharField(null=True)
    job_name = CharField(null=True)
    priority = IntegerField()
    requests_recovery = BooleanField(null=True)
    sched_name = CharField()
    sched_time = BigIntegerField(null=True)
    state = CharField()
    trigger_group = CharField()
    trigger_name = CharField()

    class Meta:
        table_name = 'qrtz_fired_triggers'
        indexes = (
            (('entry_id', 'sched_name'), True),
            (('job_group', 'sched_name'), False),
            (('job_name', 'sched_name', 'job_group'), False),
            (('sched_name', 'instance_name'), False),
            (('sched_name', 'requests_recovery', 'instance_name'), False),
            (('trigger_group', 'sched_name'), False),
            (('trigger_name', 'sched_name', 'trigger_group'), False),
        )
        primary_key = CompositeKey('entry_id', 'sched_name')


class QrtzLocks(BaseModel):
    lock_name = CharField()
    sched_name = CharField()

    class Meta:
        table_name = 'qrtz_locks'
        indexes = (
            (('sched_name', 'lock_name'), True),
        )
        primary_key = CompositeKey('lock_name', 'sched_name')


class QrtzPausedTriggerGrps(BaseModel):
    sched_name = CharField()
    trigger_group = CharField()

    class Meta:
        table_name = 'qrtz_paused_trigger_grps'
        indexes = (
            (('sched_name', 'trigger_group'), True),
        )
        primary_key = CompositeKey('sched_name', 'trigger_group')


class QrtzSchedulerState(BaseModel):
    checkin_interval = BigIntegerField()
    instance_name = CharField()
    last_checkin_time = BigIntegerField()
    sched_name = CharField()

    class Meta:
        table_name = 'qrtz_scheduler_state'
        indexes = (
            (('sched_name', 'instance_name'), True),
        )
        primary_key = CompositeKey('instance_name', 'sched_name')


class QrtzSimpleTriggers(BaseModel):
    repeat_count = BigIntegerField()
    repeat_interval = BigIntegerField()
    sched_name = ForeignKeyField(backref='qrtz_triggers_sched_name_set', column_name='sched_name', field='trigger_name',
                                 model=QrtzTriggers)
    times_triggered = BigIntegerField()
    trigger_group = ForeignKeyField(backref='qrtz_triggers_trigger_group_set', column_name='trigger_group',
                                    field='trigger_name', model=QrtzTriggers)
    trigger_name = ForeignKeyField(backref='qrtz_triggers_trigger_name_set', column_name='trigger_name',
                                   field='trigger_name', model=QrtzTriggers)

    class Meta:
        table_name = 'qrtz_simple_triggers'
        indexes = (
            (('sched_name', 'trigger_name', 'trigger_group'), True),
        )
        primary_key = CompositeKey('sched_name', 'trigger_group', 'trigger_name')


class QrtzSimpropTriggers(BaseModel):
    bool_prop_1 = BooleanField(null=True)
    bool_prop_2 = BooleanField(null=True)
    dec_prop_1 = DecimalField(null=True)
    dec_prop_2 = DecimalField(null=True)
    int_prop_1 = IntegerField(null=True)
    int_prop_2 = IntegerField(null=True)
    long_prop_1 = BigIntegerField(null=True)
    long_prop_2 = BigIntegerField(null=True)
    sched_name = ForeignKeyField(backref='qrtz_triggers_sched_name_set', column_name='sched_name', field='trigger_name',
                                 model=QrtzTriggers)
    str_prop_1 = CharField(null=True)
    str_prop_2 = CharField(null=True)
    str_prop_3 = CharField(null=True)
    trigger_group = ForeignKeyField(backref='qrtz_triggers_trigger_group_set', column_name='trigger_group',
                                    field='trigger_name', model=QrtzTriggers)
    trigger_name = ForeignKeyField(backref='qrtz_triggers_trigger_name_set', column_name='trigger_name',
                                   field='trigger_name', model=QrtzTriggers)

    class Meta:
        table_name = 'qrtz_simprop_triggers'
        indexes = (
            (('sched_name', 'trigger_name', 'trigger_group'), True),
        )
        primary_key = CompositeKey('sched_name', 'trigger_group', 'trigger_name')


class Query(BaseModel):
    average_execution_time = IntegerField()
    query = TextField(null=True)
    query_hash = BlobField(primary_key=True)

    class Meta:
        table_name = 'query'


class QueryCache(BaseModel):
    query_hash = BlobField(primary_key=True)
    results = BlobField()
    updated_at = DateTimeField(index=True)

    class Meta:
        table_name = 'query_cache'


class QueryExecution(BaseModel):
    card_id = IntegerField(null=True)
    context = CharField(null=True)
    dashboard_id = IntegerField(null=True)
    database_id = IntegerField(null=True)
    error = TextField(null=True)
    executor_id = IntegerField(null=True)
    hash = BlobField()
    native = BooleanField()
    pulse_id = IntegerField(null=True)
    result_rows = IntegerField()
    running_time = IntegerField()
    started_at = DateTimeField(index=True)

    class Meta:
        table_name = 'query_execution'
        indexes = (
            (('hash', 'started_at'), False),
        )


class ReportCardfavorite(BaseModel):
    card = ForeignKeyField(column_name='card_id', field='id', model=ReportCard)
    created_at = DateTimeField()
    owner = ForeignKeyField(column_name='owner_id', field='id', model=CoreUser)
    updated_at = DateTimeField()

    class Meta:
        table_name = 'report_cardfavorite'
        indexes = (
            (('card', 'owner'), True),
        )


class Revision(BaseModel):
    is_creation = BooleanField(constraints=[SQL("DEFAULT false")])
    is_reversion = BooleanField(constraints=[SQL("DEFAULT false")])
    message = TextField(null=True)
    model = CharField()
    model_id = IntegerField()
    object = CharField()
    timestamp = DateTimeField()
    user = ForeignKeyField(column_name='user_id', field='id', model=CoreUser)

    class Meta:
        table_name = 'revision'
        indexes = (
            (('model', 'model_id'), False),
        )


class Segment(BaseModel):
    archived = BooleanField(constraints=[SQL("DEFAULT false")])
    caveats = TextField(null=True)
    created_at = DateTimeField()
    creator = ForeignKeyField(column_name='creator_id', field='id', model=CoreUser)
    definition = TextField()
    description = TextField(null=True)
    name = CharField()
    points_of_interest = TextField(null=True)
    show_in_getting_started = BooleanField(constraints=[SQL("DEFAULT false")], index=True)
    table = ForeignKeyField(column_name='table_id', field='id', model=MetabaseTable)
    updated_at = DateTimeField()

    class Meta:
        table_name = 'segment'


class Setting(BaseModel):
    key = CharField(primary_key=True)
    value = TextField()

    class Meta:
        table_name = 'setting'


class TaskHistory(BaseModel):
    db_id = IntegerField(index=True, null=True)
    duration = IntegerField()
    ended_at = DateTimeField(index=True)
    started_at = DateTimeField()
    task = CharField()
    task_details = TextField(null=True)

    class Meta:
        table_name = 'task_history'


class ViewLog(BaseModel):
    model = CharField()
    model_id = IntegerField(index=True)
    timestamp = DateTimeField()
    user = ForeignKeyField(column_name='user_id', field='id', model=CoreUser, null=True)

    class Meta:
        table_name = 'view_log'
