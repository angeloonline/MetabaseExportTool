from model.MetabaseDatabaseModel import *


def getCollectionById(collection_id):
    return Collection.select().where((Collection.id == collection_id))


def getReportDashboardsByCollectionId(collection_id):
    return ReportDashboard.select().where((ReportDashboard.collection_id == collection_id))


def getReportCardsByCollectionId(collection_id):
    return ReportCard.select().where((ReportCard.collection_id == collection_id))


def getReportDashboardCardsByCollectionId(collection_id):
    return ReportDashboardcard.select().join(ReportDashboard).where((ReportDashboard.collection_id == collection_id))


def getDatabaseById(db_id):
    return MetabaseDatabase.select().where((MetabaseDatabase.id == db_id))


def getTablesByDbId(db_id):
    #return MetabaseTable.select().where((MetabaseTable.db_id == db_id) & (MetabaseTable.schema == schema))
    return MetabaseTable.select().where(MetabaseTable.db_id == db_id)


def getTablesMaxIdByDbId(db_id, schema):
    return MetabaseTable.select(fn.MAX(MetabaseTable.id)).where(
        (MetabaseTable.db_id == db_id) & (MetabaseTable.schema == schema)).scalar()
    # return MetabaseTable.select().where((MetabaseTable.db_id == db_id) & (MetabaseTable.schema == schema))

def getFieldsByDbId(db_id, schema):
    return MetabaseField.select().join(MetabaseTable).where(
        (MetabaseTable.db_id == db_id) & (MetabaseTable.schema == schema))

def getFieldsByDbId(db_id):
    return MetabaseField.select().join(MetabaseTable).where(MetabaseTable.db_id == db_id)

def getMetricsByDbId(db_id):
    return Metric.select().join(MetabaseTable).where(MetabaseTable.db_id == db_id)


def deleteReportDashboardCardsByDbId(db_id, schema):
    table_ids = ReportCard.select().join(MetabaseTable).where((MetabaseTable.db_id == db_id) & (MetabaseTable.schema == schema))
    dq = ReportDashboardcard.delete().where(ReportDashboardcard.card.in_(table_ids))
    return dq.execute()

def deleteReportCardsByDbId(db_id, schema):
    table_ids = MetabaseTable.select().where((MetabaseTable.db_id == db_id) & (MetabaseTable.schema == schema))
    dq = ReportCard.delete().where(ReportCard.table_id.in_(table_ids))
    return dq.execute()

def deleteDatabaseById(db_id):
    dq = MetabaseDatabase.delete().where(MetabaseDatabase.id == db_id)
    return dq.execute()

def deleteTablesByDbId(db_id):
    table_ids = MetabaseTable.select().where((MetabaseTable.db_id == db_id))
    dq = MetabaseTable.delete().where(MetabaseTable.id.in_(table_ids))
    return dq.execute()

def deleteFieldsByDbId(db_id):
    table_ids = MetabaseTable.select().where((MetabaseTable.db_id == db_id) )
    dq = MetabaseField.delete().where(MetabaseField.table_id.in_(table_ids))
    return dq.execute()

def deleteFieldValuesByDbId(db_id):
    table_ids = MetabaseFieldvalues.select().join(MetabaseField).join(MetabaseTable)\
        .where((MetabaseTable.db_id == db_id) )
    dq = MetabaseFieldvalues.delete().where(MetabaseFieldvalues.id.in_(table_ids))
    return dq.execute()

def deleteMetricsByDbId(db_id):
    table_ids = MetabaseTable.select().where(MetabaseTable.db_id == db_id)
    dq = Metric.delete().where(Metric.table_id.in_(table_ids))
    return dq.execute()
