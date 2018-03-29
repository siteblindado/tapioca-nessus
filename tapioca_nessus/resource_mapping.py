# coding: utf-8

RESOURCE_MAPPING = {
    # Agent confg
    'get_agent_config_details': {
        'resource': '/scanners/{scanner_id}/agents/config',
        'docs': 'https://cloud.tenable.com/api#/resources/agent-config/details',
        'methods': ['GET']
    },
    'update_agent_config': {
        'resource': '/scanners/{scanner_id}/agents/config',
        'docs': 'https://cloud.tenable.com/api#/resources/agent-config/edit',
        'methods': ['PUT']
    },

    # Agent Exclusions
    'create_agent_exclusion': {
        'resource': '/scanners/{scanner_id}/agents/exclusions',
        'docs': 'https://cloud.tenable.com/api#/resources/agent-exclusions/create',
        'methods': ['POST']
    },
    'update_agent_exclusion': {
        'resource': '/scanners/{scanner_id}/agents/exclusions/{exclusion_id}',
        'docs': 'https://cloud.tenable.com/api#/resources/agent-exclusions/edit',
        'methods': ['PUT']
    },
    'delete_agent_exclusion': {
        'resource': '/scanners/{scanner_id}/agents/exclusions/{exclusion_id}',
        'docs': 'https://cloud.tenable.com/api#/resources/agent-exclusions/delete',
        'methods': ['DELETE']
    },
    'get_agent_exclusion_details': {
        'resource': '/scanners/{scanner_id}/agents/exclusions/{exclusion_id}',
        'docs': 'https://cloud.tenable.com/api#/resources/agent-exclusions/details',
        'methods': ['GET']
    },
    'get_agent_exclusions': {
        'resource': '/scanners/{scanner_id}/agents/exclusions',
        'docs': 'https://cloud.tenable.com/api#/resources/agent-exclusions/list',
        'methods': ['GET']
    },

    # Agent groups
    'add_agent': {
        'resource': '/scanners/{scanner_id}/agent-groups/{group_id}/agents/{agent_id}',
        'docs': 'https://cloud.tenable.com/api#/resources/agent-groups/add-agent',
        'methods': ['PUT']
    },
    'configure_agent_group': {
        'resource': '/scanners/{scanner_id}/agent-groups/{group_id}',
        'docs': 'https://cloud.tenable.com/api#/resources/agent-groups/configure',
        'methods': ['PUT']
    },
    'create_agent_group': {
        'resource': '/scanners/{scanner_id}/agent-groups',
        'docs': 'https://cloud.tenable.com/api#/resources/agent-groups/create',
        'methods': ['POST']
    },
    'delete_agent_group': {
        'resource': '/scanners/{scanner_id}/agent-groups/{group_id}',
        'docs': 'https://cloud.tenable.com/api#/resources/agent-groups/delete',
        'methods': ['DELETE']
    },
    'delete_agent_from_group': {
        'resource': '/scanners/{scanner_id}/agent-groups/{group_id}/agents/{agent_id}',
        'docs': 'https://cloud.tenable.com/api#/resources/agent-groups/delete-agent',
        'methods': ['DELETE']
    },
    'get_agent_group_details': {
        'resource': '/scanners/{scanner_id}/agent-groups/{group_id}',
        'docs': 'https://cloud.tenable.com/api#/resources/agent-groups/details',
        'methods': ['GET']
    },
    'get_agent_groups': {
        'resource': '/scanners/{scanner_id}/agent-groups',
        'docs': 'https://cloud.tenable.com/api#/resources/agent-groups/list',
        'methods': ['GET']
    },

    # Agents
    'delete_agent': {
        'resource': '/scanners/{scanner_id}/agents/{agent_id}',
        'docs': 'https://cloud.tenable.com/api#/resources/agents/delete',
        'methods': ['DELETE']
    },
    'get_agents': {
        'resource': '/scanners/{scanner_id}/agents',
        'docs': 'https://cloud.tenable.com/api#/resources/agents/list',
        'methods': ['DELETE']
    },
    'get_agent': {
        'resource': '/scanners/{scanner_id}/agents/{agent_id}',
        'docs': 'https://cloud.tenable.com/api#/resources/agents/get',
        'methods': ['GET']
    },

    # Assets
    'list_assets': {
        'resource': '/assets',
        'docs': 'https://cloud.tenable.com/api#/resources/assets/list-assets',
        'methods': ['GET']
    },
    'asset_info': {
        'resource': '/assets/{asset_uuid}',
        'docs': 'https://cloud.tenable.com/api#/resources/assets/asset-info',
        'methods': ['GET']
    },
    'import_assets': {
        'resource': '/import/assets',
        'docs': 'https://cloud.tenable.com/api#/resources/assets/import',
        'methods': ['POST']
    },
    'list_import_jobs': {
        'resource': '/import/asset-jobs',
        'docs': 'https://cloud.tenable.com/api#/resources/assets/list-import-jobs',
        'methods': ['GET']
    },
    'get_import_jobs_info': {
        'resource': '/import/asset-jobs/{asset_import_job_uuid}',
        'docs': 'https://cloud.tenable.com/api#/resources/assets/import-job-info',
        'methods': ['GET']
    },

    # Audit log
    'audit_log_events': {
        'resource': '/audit-log/v1/events',
        'docs': 'https://cloud.tenable.com/api#/resources/audit-log/events',
        'methods': ['GET']
    },

    # Bulk operations
    'bulk_add_agent': {
        'resource': '/scanners/{scanner_id}/agent-groups/{group_id}/agents/_bulk/add',
        'docs': 'https://cloud.tenable.com/api#/resources/bulk-operations/bulk-add-agent',
        'methods': ['POST']
    },
    'bulk_remove_agent': {
        'resource': '/scanners/{scanner_id}/agent-groups/{group_id}/agents/_bulk/remove',
        'docs': 'https://cloud.tenable.com/api#/resources/bulk-operations/bulk-remove-agent',
        'methods': ['POST']
    },
    'unlink_agent': {
        'resource': '/scanners/{scanner_id}/agents/_bulk/unlink',
        'docs': 'https://cloud.tenable.com/api#/resources/bulk-operations/bulk-unlink-agent',
        'methods': ['POST']
    },
    'bulk_agent_group_status': {
        'resource': '/scanners/{scanner_id}/agent-groups/{group_id}/agents/_bulk/{task_uuid}',
        'docs': 'https://cloud.tenable.com/api#/resources/bulk-operations/bulk-agent-group-status',
        'methods': ['GET']
    },
    'bulk_agent_status': {
        'resource': '/scanners/{scanner_id}/agents/_bulk/{task_uuid}',
        'docs': 'https://cloud.tenable.com/api#/resources/bulk-operations/bulk-agent-status',
        'methods': ['GET']
    },

    # Editor
    'export_audit_file': {
        'resource': '/editor/{type}/{object_id}/audits/{file_id}',
        'docs': 'https://cloud.tenable.com/api#/resources/editor/audits',
        'methods': ['GET']
    },
    'get_template_details': {
        'resource': '/editor/{type}/templates/{template_uuid}',
        'docs': 'https://cloud.tenable.com/api#/resources/editor/details',
        'methods': ['GET']
    },
    'get_editor_object': {
        'resource': '/editor/{type}/{id}',
        'docs': 'https://cloud.tenable.com/api#/resources/editor/edit',
        'methods': ['GET']
    },
    'get_templates': {
        'resource': '/editor/{type}/templates',
        'docs': 'https://cloud.tenable.com/api#/resources/editor/list',
        'methods': ['GET']
    },
    'get_plugin_description': {
        'resource': '/editor/policy/{policy_id}/families/{family_id}/plugins/{plugin_id}',
        'docs': 'https://cloud.tenable.com/api#/resources/editor/plugin-description',
        'methods': ['GET']
    },

    # Exclusions
    'create_exclusion': {
        'resource': '/exclusions',
        'docs': 'https://cloud.tenable.com/api#/resources/exclusions/create',
        'methods': ['POST']
    },
    'delete_exclusion': {
        'resource': '/exclusions/{list_id}',
        'docs': 'https://cloud.tenable.com/api#/resources/exclusions/delete',
        'methods': ['DELETE']
    },
    'get_exclusion_details': {
        'resource': '/exclusions/{list_id}',
        'docs': 'https://cloud.tenable.com/api#/resources/exclusions/details',
        'methods': ['GET']
    },
    'update_exclusion': {
        'resource': '/exclusions/{list_id}',
        'docs': 'https://cloud.tenable.com/api#/resources/exclusions/edit',
        'methods': ['PUT']
    },
    'get_exclusions': {
        'resource': '/exclusions',
        'docs': 'https://cloud.tenable.com/api#/resources/exclusions/list',
        'methods': ['GET']
    },

    # File
    'file_upload': {
        'resource': '/file/upload',
        'docs': 'https://cloud.tenable.com/api#/resources/file/upload',
        'methods': ['GET']
    },
}
