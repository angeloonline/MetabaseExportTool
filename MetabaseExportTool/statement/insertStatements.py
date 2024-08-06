

def createCollection(tables):
    array = []
    for table in tables:
        # print(table.name, " ", table.schema)
        insert_into = "INSERT INTO public.%s VALUES (%d, %s, %s, %s, %s, %s, %s);" % (
                          "collection",
                          table.id,
                          printNullOrStringIfNone(table.name),
                          printNullOrStringIfNone(table.description),
                          #printNullOrStringIfNone(table.color),
                          printBoolean(table.archived),
                          printNullOrStringIfNone(table.location),
                          printNullIfNone(table.personal_owner_id),
                          printNullOrStringIfNone(table.slug)

        )

        print(insert_into)
        array.append(insert_into)

    print('Array length: ' + str(len(array)))
    return array

def createArrayOfReportDashboards(tables):
    array = []
    for table in tables:
        # print(table.name, " ", table.schema)
        insert_into = "INSERT INTO public.%s VALUES (%d, %s, %s, %s, %s, %s, %s, %s," \
                      "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);" % (
            "report_dashboard",
            table.id,
            printNullOrStringIfNoneDatetime(table.created_at),
            printNullOrStringIfNoneDatetime(table.updated_at),
            printNullOrStringIfNone(table.name),
            printNullOrStringIfNone(table.description),
            printNullIfNone(table.creator_id),
            printNullOrStringIfNone(table.parameters),
            printNullOrStringIfNone(table.points_of_interest),
            printNullOrStringIfNone(table.caveats),
            printBoolean(table.show_in_getting_started), #10
            printNullOrStringIfNone(table.public_uuid),
            printNullIfNone(table.made_public_by_id),
            printBoolean(table.enable_embedding),
            printNullOrStringIfNone(table.embedding_params),
            printBoolean(table.archived),
            printNullIfNone(table.position),
            printNullIfNone(table.collection_id),
            printNullIfNone(table.collection_position) #18

        )

        print(insert_into)
        array.append(insert_into)

    print('Array length: ' + str(len(array)))
    return array

def createArrayOfReportCards(tables):
    array = []
    for table in tables:
        # print(table.name, " ", table.schema)
        insert_into = "INSERT INTO public.%s VALUES (%d, %s, %s, %s, %s, %s, %s, %s," \
                      "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);" % (
            "report_card",
            table.id,
            printNullOrStringIfNoneDatetime(table.created_at),
            printNullOrStringIfNoneDatetime(table.updated_at),
            printNullOrStringIfNone(table.name),
            printNullOrStringIfNone(table.description),
            printNullOrStringIfNone(table.display),
            printNullOrStringIfNone(table.dataset_query),
            printNullOrStringIfNone(table.visualization_settings),
            printNullIfNone(table.creator_id),
            printNullIfNone(table.database_id), #10
            printNullIfNone(table.table_id),
            printNullOrStringIfNone(table.query_type),
            printBoolean(table.archived),
            printNullIfNone(table.collection_id),
            printNullOrStringIfNone(table.public_uuid),
            printNullIfNone(table.made_public_by_id),
            printBoolean(table.enable_embedding),
            printNullOrStringIfNone(table.embedding_params),
            printNullIfNone(table.cache_ttl),
            printNullOrStringIfNone(table.result_metadata),
            #printNullOrStringIfNone(table.read_permissions),
            printNullIfNone(table.collection_position) #21

        )

        print(insert_into)
        array.append(insert_into)

    print('Array length: ' + str(len(array)))
    return array


def createArrayOfReportDashboardCards(tables):
    array = []
    for table in tables:
        # print(table.name, " ", table.schema)
        insert_into = "INSERT INTO public.%s VALUES (%d, %s, %s, %s, %s, %s, %s, %s," \
                      "%s, %s, %s);" % (
            "report_dashboardcard",
            table.id,
            printNullOrStringIfNoneDatetime(table.created_at),
            printNullOrStringIfNoneDatetime(table.updated_at),
            printNullIfNone(table.size_x),
            printNullIfNone(table.size_y),
            printNullIfNone(table.row),
            printNullIfNone(table.col),
            printNullIfNone(table.card_id),
            printNullIfNone(table.dashboard_id),
            printNullOrStringIfNone(table.parameter_mappings),#10
            printNullOrStringIfNone(table.visualization_settings)

        )

        print(insert_into)
        array.append(insert_into)

    print('Array length: ' + str(len(array)))
    return array

def createArrayOfDatabases(tables):
    array = []
    for table in tables:
        # print(table.name, " ", table.schema)
        insert_into = "INSERT INTO public.%s VALUES (%d, '%s', '%s', '%s', %s, '%s', %s, %s, %s, %s, " \
                      "%s, %s, %s, %s, %s, %s);" % (
                          "metabase_database",
                          table.id,
                          table.created_at,
                          table.updated_at,
                          table.name,
                          printNullIfNone(table.description),
                          printNullIfNone(table.details),
                          printNullIfNone(table.engine),
                          str(table.is_sample).lower(),
                          str(table.is_full_sync).lower(),
                          printNullIfNone(table.points_of_interest),
                          printNullIfNone(table.caveats), #10
                          str("'" + table.metadata_sync_schedule+ "'"),
                          str("'" + table.cache_field_values_schedule + "'"),
                          str("'" + table.timezone+ "'"),
                          printBoolean(table.is_on_demand),
                          #printNullIfNone(table.options),
                          printBoolean(table.auto_run_queries) #16
        )

        print(insert_into)
        array.append(insert_into)

    print('Array length: ' + str(len(array)))
    return array

def createArrayOfTables(tables, schemaNameToChange, offsetIncrement=0):
    array =[]
    for table in tables:
        # print(table.name, " ", table.schema)
        insert_into = "INSERT INTO public.%s VALUES (%d, '%s', '%s', %s, %s, '%s', %s, %d, " \
                      "'%s', %s, '%s', %s, %s, %s);" % (
                          "metabase_table",
                          table.id,
                          table.created_at,
                          table.updated_at,
                          table.name,
                          #'NULL' if table.rows is None else table.rows,
                          'NULL' if table.description is None else "'" + table.description + "'",
                          #'NULL' if table.entity_name is None else "'" + table.entity_name + "'",
                          table.entity_type,
                          str(table.active).lower(),
                          table.db_id,
                          table.display_name,
                          'NULL' if table.visibility_type is None else "'" + table.visibility_type + "'",
                          schemaNameToChange if schemaNameToChange is not None else table.schema,
                          'NULL' if table.points_of_interest is None else "'" + table.points_of_interest + "'",
                          'NULL' if table.caveats is None else "'" + table.caveats + "'",
                          str(table.show_in_getting_started).lower()
                          #table.fields_hash
                      )

        print(insert_into)
        array.append(insert_into)

    print('Array length: ' + str(len(array)))
    return array

def createArrayOfFields(tables):
    array =[]
    for table in tables:
        # print(table.name, " ", table.schema)
        insert_into = "INSERT INTO public.%s VALUES (%d, '%s', '%s', '%s', '%s', %s, %s, %s, %s, %s, %s, %s, " \
                      "'%s', '%s', %s, %s, %s, %s, %d, %s, %s, %s);" % (
                          "metabase_field",
                          table.id, #1
                          table.created_at,
                          table.updated_at,
                          table.name,
                          printNullOrStringIfNone(table.base_type),
                          #printNullOrStringIfNone(table.special_type),
                          str(table.active).lower(),
                          printNullIfNone(table.description),
                          str(table.preview_display).lower(),
                          table.position, #10
                          table.table_id, #11
                          printNullIfNone(table.parent_id),
                          printNullIfNone(table.display_name),
                          table.visibility_type,
                          printNullIfNone(table.fk_target_field_id),
                          printNullOrStringIfNoneDatetime(table.last_analyzed),
                          printNullIfNone(table.points_of_interest),
                          printNullIfNone(table.caveats),
                          printNullOrStringIfNone(table.fingerprint),
                          table.fingerprint_version,
                          printNullOrStringIfNone(table.database_type),
                          printNullOrStringIfNone(table.has_field_values),
                          printNullOrStringIfNone(table.settings)
        )

        print(insert_into)
        array.append(insert_into)

    print('Array length: ' + str(len(array)))
    return array

def createArrayOfMetrics(tables):
    array = []
    for table in tables:
        # print(table.name, " ", table.schema)
        insert_into = "INSERT INTO public.%s VALUES (%d, %s, %s, %s, %s, %s, %s, %s," \
                      "%s, %s, %s, %s, %s);" % (
            "metric",
            table.id,
            printNullIfNone(table.table_id),
            printNullIfNone(table.creator_id),
            printNullOrStringIfNone(table.name),
            printNullOrStringIfNone(table.description),
            printBoolean(table.archived),
            printNullOrStringIfNone(table.definition),
            printNullOrStringIfNoneDatetime(table.created_at),
            printNullOrStringIfNoneDatetime(table.updated_at),
            printNullIfNone(table.points_of_interest),#10
            printNullIfNone(table.caveats),
            printNullOrStringIfNone(table.how_is_this_calculated),
            printBoolean(table.show_in_getting_started) #13

        )

        print(insert_into)
        array.append(insert_into)

    print('Array length: ' + str(len(array)))
    return array

def printNullIfNone(value):
    if value is None:
        return 'NULL'
    else:
        return value

def printNullOrStringIfNone(value):
    if value is None:
        return 'NULL'
    else:
        return "'" + value + "'"

def printNullOrStringIfNoneDatetime(value):
    if value is None:
        return 'NULL'
    else:
        return "'" + str(value) + "'"

def printBoolean(value):
    return str(value).lower()
