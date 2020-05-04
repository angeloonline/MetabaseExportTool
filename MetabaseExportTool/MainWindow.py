import datetime
import json
import logging
import sys
import os
import yaml

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from playhouse.shortcuts import model_to_dict

from MetabaseExportTool.query.dbQueries import *
from MetabaseExportTool.statement.insertStatements import *
from MetabaseExportTool.ui.MetabaseExportMain import Ui_MainWindow


def getConfigDB():
    with open(os.path.abspath("MetabaseExportTool/config_db.yml"), 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    return cfg


''' old implementation
def exportAll(cgfDB, collectionToExport, databaseToExport, schemaName, changeToSchemaName, exportFolder):
    # export Collection related part
    collection = getCollectionById(collectionToExport)
    reportDashboards = getReportDashboardsByCollectionId(collectionToExport)
    reportCards = getReportCardsByCollectionId(collectionToExport)
    reportDashboardCards = getReportDashboardCardsByCollectionId(collectionToExport)

    # export Db related part
    databases = getDatabaseById(databaseToExport)
    if databases == 0:
        return 'Database not found!'
    tables = getTablesByDbId(databaseToExport, schemaName)
    # maxId = getTablesMaxIdByDbId(databaseToExport, schemaName)
    # print(str(maxId))
    fields = getFieldsByDbId(databaseToExport, schemaName)
    metrics = getMetricsByDbId(databaseToExport)

    arrayOfReportDashboardCards = createArrayOfReportDashboardCards(reportDashboardCards)
    with open(exportFolder + 'export_report_dashboardcard.sql', 'w', encoding="utf-8") as file:
        for table in arrayOfReportDashboardCards:
            file.write(table)
            file.write("\n")

    arrayOfReportCards = createArrayOfReportCards(reportCards)
    with open(exportFolder + 'export_report_card.sql', 'w', encoding="utf-8") as file:
        for table in arrayOfReportCards:
            file.write(table)
            file.write("\n")

    arrayOfReportDashboards = createArrayOfReportDashboards(reportDashboards)
    with open(exportFolder + 'export_report_dashboard.sql', 'w') as file:
        for table in arrayOfReportDashboards:
            file.write(table)
            file.write("\n")

    collectionTable = createCollection(collection)
    with open(exportFolder + 'export_collection.sql', 'w') as file:
        for table in collectionTable:
            file.write(table)
            file.write("\n")

    arrayOfDatabases = createArrayOfDatabases(databases)
    with open(exportFolder + 'export_databases.sql', 'w') as file:
        for table in arrayOfDatabases:
            file.write(table)
            file.write("\n")

    arrayOfTables = createArrayOfTables(tables, schemaNameToChange=changeToSchemaName, offsetIncrement=100)
    with open(exportFolder + 'export_tables.sql', 'w') as file:
        for table in arrayOfTables:
            file.write(table)
            file.write("\n")

    arrayOfFields = createArrayOfFields(fields)
    with open(exportFolder + 'export_fields.sql', 'w') as file:
        for table in arrayOfFields:
            file.write(table)
            file.write("\n")

    arrayOfMetrics = createArrayOfMetrics(metrics)
    with open(exportFolder + 'export_metrics.sql', 'w', encoding="utf-8") as file:
        for table in arrayOfMetrics:
            file.write(table)
            file.write("\n")

    return 'Export completed'
'''


def exportAll(cfgDB, dbSource, collectionToExport, databaseToExport, changeToSchemaName, exportFolder):
    logMessages = []
    # Source Db
    logging.info('Source Database ' + cfgDB['source']['database'])
    sourceDatabase = cfgDB['source']
    database = PostgresqlDatabase(dbSource, user=sourceDatabase['user'], password=sourceDatabase['password'],
                                  host=sourceDatabase['host'], port=sourceDatabase['port'])
    Config(database)

    # export Collection related part
    collection = getCollectionById(collectionToExport)
    if collection.count() == 0:
        logMessages.append('Collection not found!')
    else:
        reportDashboards = getReportDashboardsByCollectionId(collectionToExport)
        reportCards = getReportCardsByCollectionId(collectionToExport)
        reportDashboardCards = getReportDashboardCardsByCollectionId(collectionToExport)

        arrayOfReportDashboardCards = createArrayOfReportDashboardCards(reportDashboardCards)
        with open(exportFolder + 'export_report_dashboardcard.sql', 'w', encoding="utf-8") as file:
            for table in arrayOfReportDashboardCards:
                file.write(table)
                file.write("\n")

        arrayOfReportCards = createArrayOfReportCards(reportCards)
        with open(exportFolder + 'export_report_card.sql', 'w', encoding="utf-8") as file:
            for table in arrayOfReportCards:
                file.write(table)
                file.write("\n")

        arrayOfReportDashboards = createArrayOfReportDashboards(reportDashboards)
        with open(exportFolder + 'export_report_dashboard.sql', 'w') as file:
            for table in arrayOfReportDashboards:
                file.write(table)
                file.write("\n")

        collectionTable = createCollection(collection)
        with open(exportFolder + 'export_collection.sql', 'w') as file:
            for table in collectionTable:
                file.write(table)
                file.write("\n")

    # export Db related part
    databases = getDatabaseById(databaseToExport)
    if databases.count() == 0:
        logMessages.append('Database not found!')
    else:
        tables = getTablesByDbId(databaseToExport)
        fields = getFieldsByDbId(databaseToExport)
        metrics = getMetricsByDbId(databaseToExport)

        # TO DO
        # maxId = getTablesMaxIdByDbId(databaseToExport, schemaName)
        # print(str(maxId))

        arrayOfDatabases = createArrayOfDatabases(databases)
        with open(exportFolder + 'export_databases.sql', 'w') as file:
            for table in arrayOfDatabases:
                file.write(table)
                file.write("\n")

        arrayOfTables = createArrayOfTables(tables, schemaNameToChange=changeToSchemaName, offsetIncrement=100)
        with open(exportFolder + 'export_tables.sql', 'w') as file:
            for table in arrayOfTables:
                file.write(table)
                file.write("\n")

        arrayOfFields = createArrayOfFields(fields)
        with open(exportFolder + 'export_fields.sql', 'w') as file:
            for table in arrayOfFields:
                file.write(table)
                file.write("\n")

        arrayOfMetrics = createArrayOfMetrics(metrics)
        with open(exportFolder + 'export_metrics.sql', 'w', encoding="utf-8") as file:
            for table in arrayOfMetrics:
                file.write(table)
                file.write("\n")

    logMessages.append('Export completed')
    return logMessages


def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


'''
def insertRecord(record):
    json_data = json.dumps(model_to_dict(record), default=myconverter)
    dict = model_to_dict(record)
    logging.info(json_data)
    database = PostgresqlDatabase('metabase_target', **{'user': 'postgres'})
    Config(database)
    result = Metric.insert(dict['id']).execute()
    logging.info(' result:' + str(result))
'''


def deleteDb(cfgDB, dbTarget, collectionToDelete, databaseToDelete):
    logMessages = []
    # Destination DB
    targetDatabase = cfgDB['target']
    database = PostgresqlDatabase(dbTarget, user=targetDatabase['user'], password=targetDatabase['password'],
                                  host=targetDatabase['host'], port=targetDatabase['port'])
    Config(database)

    fieldValues = deleteFieldValuesByDbId(databaseToDelete)
    fields = deleteFieldsByDbId(databaseToDelete)
    logging.info('Field Record deleted: ' + str(fields))

    # Collection part
    if collectionToDelete is not None:
        reportDashboardCards = deleteReportDashboardCardsByDbId(databaseToDelete)
        reportCards = deleteReportCardsByDbId(databaseToDelete)

    # Database part
    metrics = deleteMetricsByDbId(databaseToDelete)
    logging.info('Metrics Record deleted: ' + str(metrics))
    tableDeleted = deleteTablesByDbId(databaseToDelete)
    logging.info('Table Record deleted: ' + str(tableDeleted))
    databaseDeleted = deleteDatabaseById(databaseToDelete)
    logging.info('Database Record deleted: ' + str(databaseDeleted))
    if databaseDeleted == 0:
        logMessages.append('Database not found!')

    logMessages.append('Delete completed')
    return logMessages


''' Migrate DB function 
'''
def migrateDB(cfgDB, dbSource, dbTarget, schemaName, changeToDatabaseId, changeToSchemaName, collectionToExport,
              databaseToExport):
    # Configure our proxy to use the db we specified in config.
    # Source Db
    sourceDatabase = cfgDB['source']
    database = PostgresqlDatabase(dbSource, user=sourceDatabase['user'], password=sourceDatabase['password'],
                                  host=sourceDatabase['host'], port=sourceDatabase['port'])
    Config(database)

    if collectionToExport is not None:
        collectionRecords = getCollectionById(collectionToExport).execute()
        reportDashboardsRecords = getReportDashboardsByCollectionId(collectionToExport).execute()
        reportCardsRecords = getReportCardsByCollectionId(collectionToExport).execute()
        reportDashboardCardsRecords = getReportDashboardCardsByCollectionId(collectionToExport).execute()

    tablesRecords = getTablesByDbId(databaseToExport, schemaName).execute()
    databasesRecord = getDatabaseById(databaseToExport).execute()
    fieldsRecords = getFieldsByDbId(databaseToExport, schemaName).execute()
    metricsRecords = getMetricsByDbId(databaseToExport).execute()

    # Destination DB
    targetDatabase = cfgDB['target']
    database = PostgresqlDatabase(dbTarget, user=targetDatabase['user'], password=targetDatabase['password'],
                                  host=targetDatabase['host'], port=targetDatabase['port'])
    Config(database)

    # Delete preexisting records
    if changeToDatabaseId is None:
        databaseToDelete = databaseToExport
    else:
        databaseToDelete = changeToDatabaseId
    fieldValues = deleteFieldValuesByDbId(databaseToDelete)
    fields = deleteFieldsByDbId(databaseToDelete)
    logging.info('Field Record deleted: ' + str(fields))

    if collectionToExport is not None:
        reportDashboardCards = deleteReportDashboardCardsByDbId(databaseToDelete)
        reportCards = deleteReportCardsByDbId(databaseToDelete)
    metrics = deleteMetricsByDbId(databaseToDelete)
    logging.info('Metrics Record deleted: ' + str(metrics))
    tableDeleted = deleteTablesByDbId(databaseToDelete)
    logging.info('Table Record deleted: ' + str(tableDeleted))
    databaseDeleted = deleteDatabaseById(databaseToDelete)
    logging.info('Record deleted: ' + str(databaseDeleted))

    # insert database Id
    for record in databasesRecord:
        value = model_to_dict(record, recurse=False)  # we dont want that foreign-keys should be recursed.
        if changeToDatabaseId is not None:
            value['id'] = changeToDatabaseId
        MetabaseDatabase.insert(value).execute()

    logging.info('Insert table records: ' + str(len(tablesRecords)))
    for record in tablesRecords:
        value = model_to_dict(record, recurse=False)  # we dont want that foreign-keys should be recursed.
        if changeToDatabaseId is not None:
            value['db'] = changeToDatabaseId
        MetabaseTable.insert(value).execute()
        logging.info('Record inserted: ' + str(value))

    logging.info('Insert fields records: ' + str(len(fieldsRecords)))
    for record in fieldsRecords:
        value = model_to_dict(record, recurse=False)  # we dont want that foreign-keys should be recursed.
        MetabaseField.insert(value).execute()
        logging.info('Record inserted: ' + str(value))

    logging.info('Insert metrics records: ' + str(len(metricsRecords)))
    for record in metricsRecords:
        value = model_to_dict(record, recurse=False)  # we dont want that foreign-keys should be recursed.
        Metric.insert(value).execute()
        logging.info('Record inserted: ' + str(value))

    if collectionToExport is not None:
        for record in reportCardsRecords:
            value = model_to_dict(record, recurse=False)  # we dont want that foreign-keys should be recursed.
            ReportCard.insert(value).execute()
            logging.info('Record inserted: ' + str(value))

        for record in reportDashboardCardsRecords:
            value = model_to_dict(record, recurse=False)  # we dont want that foreign-keys should be recursed.
            ReportDashboardcard.insert(value).execute()
            logging.info('Record inserted: ' + str(value))

    return 'Migration completed'


def main():
    try:
        exportFolder = './export/'
        schemaName = 'PUBLIC'
        changeToSchemaName = None
        changeToDatabaseId = 4
        collectionToExport = None
        databaseToExport = 1
        dbSource = 'metabase'
        dbTarget = 'metabase_target'

        migrateDB(dbSource, dbTarget, schemaName, changeToDatabaseId, changeToSchemaName, collectionToExport,
                  databaseToExport)

        '''
        exportAll(collectionToExport, databaseToExport, schemaName, changeToSchemaName, exportFolder)

        # Configure our proxy to use the db we specified in config.
        database = PostgresqlDatabase('metabase_target', **{'user': 'postgres'})
        Config(database)

        collectionToExport = 1
        databaseToExport = 1
        schemaName = 'PUBLIC'
        exportAll(collectionToExport, databaseToExport, schemaName, changeToSchemaName, exportFolder)
        '''

    # fields = deleteFieldsByDbId(databaseToExport, "ANGELO_THED")
    except Exception as e:
        print(str(e))  # print exceptions


class MetabaseWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MetabaseWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Migrate.clicked.connect(self.btnMigrateClicked)
        self.ui.Export.clicked.connect(self.btnExportClicked)
        self.ui.Delete.clicked.connect(self.btnDeleteClicked)
        self.cfg = getConfigDB()
        self.initPanel()

    def initPanel(self):
        self.ui.dbSourceToMigrate.setText(self.cfg['source']['database'])
        self.ui.dbSourceToExport.setText(self.cfg['source']['database'])
        self.ui.dbTargetToMigrate.setText(self.cfg['target']['database'])
        self.ui.dbTargetToDelete.setText(self.cfg['target']['database'])

    def printLog(self, text):
        self.ui.outputLog.setText(str(text))

    def btnMigrateClicked(self):
        logging.info('Running...')
        logging.info(self.ui.dbSourceToMigrate.text())
        logging.info(self.ui.dbTargetToMigrate.text())
        logging.info(self.ui.collectionToMigrate.text())
        logging.info(self.ui.databaseToMigrate.text())
        logging.info(self.ui.changeToDatabaseId.text())

        try:
            dbSource = self.ui.dbSourceToMigrate.text()
            dbTarget = self.ui.dbTargetToMigrate.text()
            collection = self.ui.collectionToMigrate.value()
            if collection == 0:
                collection = None

            database = int(self.ui.databaseToMigrate.text())

            changeToDatabaseId = self.ui.changeToDatabaseId.value()
            if changeToDatabaseId == 0:
                changeToDatabaseId = None

            schemaName = 'PUBLIC'
            changeToSchemaName = None

            reply = QMessageBox.question(self, 'Continue?',
                                         'Are you sure to continue?', QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                logging.info("Yes")
                output = migrateDB(self.cfg, dbSource, dbTarget, schemaName, changeToDatabaseId, changeToSchemaName,
                                   collection,
                                   database)
                self.printLog('\n'.join(output))
            else:
                logging.info("No")
                self.printLog('Abort')

        except Exception as e:
            logging.error(str(e))  # log exceptions
            self.printLog(e)

    def btnExportClicked(self):
        logging.info('Running...')
        logging.info(self.ui.dbSourceToExport.text())
        logging.info(self.ui.collectionToExport.value())
        logging.info(self.ui.databaseToExport.value())
        try:
            exportFolder = './export/'
            changeToSchemaName = self.ui.changeToSchemaName.text()
            if changeToSchemaName == '':
                changeToSchemaName = None
            dbSource = self.ui.dbSourceToExport.text()
            collectionToExport = self.ui.collectionToExport.value()
            if collectionToExport == 0:
                collectionToExport = None

            databaseToExport = self.ui.databaseToExport.value()
            output = exportAll(self.cfg, dbSource, collectionToExport, databaseToExport, changeToSchemaName,
                               exportFolder)
            self.printLog('\n'.join(output))

        except Exception as e:
            logging.error(str(e))  # log exceptions
            self.printLog(e)

    def btnDeleteClicked(self):
        logging.info('Running...')
        logging.info(self.ui.dbTargetToDelete.text())
        logging.info(self.ui.collectionToDelete.text())
        logging.info(self.ui.databaseToDelete.text())
        try:
            dbTarget = self.ui.dbTargetToDelete.text()
            collection = self.ui.collectionToDelete.value()
            if collection == 0:
                collection = None

            database = self.ui.databaseToDelete.value()
            output = deleteDb(self.cfg, dbTarget, collection, database)
            self.printLog('\n'.join(output))
        except Exception as e:
            logging.error(str(e))  # log exceptions
            self.printLog(e)


def runMetabaseExportToolGUI():
    # main()
    logging.basicConfig(format='[%(asctime)s-%(levelname)s] %(message)s', level=logging.DEBUG)
    app = QtWidgets.QApplication(sys.argv)
    w = MetabaseWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    runMetabaseExportToolGUI()