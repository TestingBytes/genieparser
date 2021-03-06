expected_output = {
    "mobility_event_statistics": {
        "joined_as": {
            "local": 60431,
            "foreign": 0,
            "export_foreign": 0,
            "export_anchor": 0,
        },
        "delete": {"local": 60316, "remote": 0},
        "role_changes": {"local_to_anchor": 0, "anchor_to_local": 0},
        "roam_stats": {
            "l2_roam_count": 0,
            "l3_roam_count": 0,
            "flex_client_roam_count": 0,
            "inter_wncd_roam_count": 0,
            "intra_wncd_roam_count": 154227,
            "remote_inter_cntrl_roam_count": 0,
            "remote_webauth_pending_roams": 0,
        },
        "anchor_request": {
            "sent": 0,
            "grant_received": 0,
            "deny_received": 0,
            "received": 0,
            "grant_sent": 0,
            "deny_sent": 0,
        },
        "handoff_status_received": {
            "success": 0,
            "group_mismatch": 0,
            "client_unknown": 0,
            "client_blacklisted": 0,
            "ssid_mismatch": 0,
            "denied": 0,
            "l3_vlan_override": 0,
            "unknown_peer": 0,
        },
        "handoff_status_sent": {
            "success": 0,
            "group_mismatch": 0,
            "client_unknown": 0,
            "client_blacklisted": 0,
            "ssid_mismatch": 0,
            "denied": 0,
            "l3_vlan_override": 0,
        },
        "export_anchor": {
            "request_sent": 0,
            "response_received": {
                "ok": 0,
                "deny_generic": 0,
                "client_blacklisted": 0,
                "client_limit_reached": 0,
                "profile_mismatch": 0,
                "deny_unknown_reason": 0,
                "request_received": 0,
            },
            "response_sent": {
                "ok": 0,
                "deny_generic": 0,
                "client_blacklisted": 0,
                "client_limit_reached": 0,
                "profile_mismatch": 0,
            },
        },
    },
    "mm_mobility_event_statistics": {
        "event_data_allocs": 120747,
        "event_data_frees": 120747,
        "fsm_set_allocs": 60427,
        "fsm_set_frees": 60316,
        "timer_allocs": 0,
        "timer_frees": 0,
        "timer_starts": 0,
        "timer_stops": 0,
        "invalid_events": 0,
        "internal_errors": 0,
        "delete_internal_errors": 0,
        "roam_internal_errors": 0,
    },
    "mmif_mobility_event_statistics": {
        "event_data_allocs": 354187,
        "event_data_frees": 354187,
        "invalid_events": 13,
        "event_schedule_errors": 0,
        "mmif_internal_errors": {
            "ipc_failure": 0,
            "database_failure": 0,
            "invalid_parameters": 0,
            "mobility_message_decode_failure": 0,
            "fsm_failure": 0,
            "client_handoff_success": 0,
            "client_handoff_failure": 0,
            "anchor_deny": 0,
            "remote_delete": 0,
            "tunnel_down_delete": 0,
            "mbssid_down": 0,
            "unknown_failure": 0,
        },
    },
}
