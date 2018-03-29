# coding: utf-8

RESOURCE_MAPPING = {
    # Agent confg
    'get_agent_config': {
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
    'create_exclusion': {
        'resource': '/scanners/{scanner_id}/agents/exclusions',
        'docs': 'https://cloud.tenable.com/api#/resources/agent-exclusions/create',
        'methods': ['POST']
    },
    'update_exclusion': {
        'resource': '/scanners/{scanner_id}/agents/exclusions/{exclusion_id}',
        'docs': 'https://cloud.tenable.com/api#/resources/agent-exclusions/edit',
        'methods': ['PUT']
    },
    'delete_exclusion': {
        'resource': '/scanners/{scanner_id}/agents/exclusions/{exclusion_id}',
        'docs': 'https://cloud.tenable.com/api#/resources/agent-exclusions/delete',
        'methods': ['DELETE']
    },
    'get_exclusion_details': {
        'resource': '/scanners/{scanner_id}/agents/exclusions/{exclusion_id}',
        'docs': 'https://cloud.tenable.com/api#/resources/agent-exclusions/details',
        'methods': ['GET']
    },
    'get_exclusions': {
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
}
