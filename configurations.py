# MODULE: CÁC CONFIG KHI GÁN NHÃN DATASET

# ALL FILES
all_files = ["email", "gmailchat", "aim_chat", "facebook_chat",
             "hangout_chat", "icq_chat", "skype_chat", "AIMchat", "ICQchat", "facebookchat", "hangouts_chat", "netflix", "spotify", "vimeo", "youtube", "youtubeHTML5", "ftps_down", "ftps_up", "scpDown",
             "scpUp", "sftp_down", "sftp_up", "sftpDown", "sftpUp", "skype_file", "scp", "sftp", "facebook_audio", "hangouts_audio", "skype_audio", "voipbuster", "vpn_email", "vpn_aim_chat", "vpn_facebook_chat", "vpn_hangouts_chat", "vpn_icq_chat", "vpn_skype_chat", "vpn_netflix", "vpn_spotify",
             "vpn_vimeo", "vpn_youtube", "vpn_ftps",
             "vpn_sftp", "vpn_skype_files", "vpn_facebook_audio",
             "vpn_hangouts_audio", "vpn_skype_audio", "vpn_voipbuster", "vpn_bittorrent"]

# Name: non VPN - VPN
# Type: Binary
# Description:
# 0 : non-VPN
# 1 : VPN
binary_lable = [0, 1]

# Name: non VPN - VPN
# Type: Multiclass
# Description:
# 0 : email
# 1 : chat
# 2 : streaming
# 3 : file
# 4 : voip
# 5 : p2p
# 6 : vpn_email
# 7 : vpn_chat
# 8 : vpn_streaming
# 9 : vpn_file
# 10: vpn_voip
# 11: vpn_p2p
# note: Bỏ netflix
# không có p2p (5) vì dataset không có pcap p2p
# traffic_rules = [
#     {"name": "email", "value": ["email"], "label": 0},
#     {"name": "chat", "value": ["aim_chat", "facebook_chat",
#                                "hangout_chat", "icq_chat", "skype_chat", "AIMchat", "gmailchat", "ICQchat", "facebookchat", "hangouts_chat"], "label": 1},
#     {"name": "streaming", "value": [
#         "netflix", "spotify", "vimeo", "youtube", "youtubeHTML5"], "label": 2},
#     {"name": "file", "value": ["ftps_down", "ftps_up", "scpDown",
#                                "scpUp", "sftp_down", "sftp_up", "sftpDown", "sftpUp", "skype_file", "scp", "sftp"], "label": 3},
#     {"name": "voip", "value": ["facebook_audio", "facebook_video", "hangouts_audio",
#                                "hangouts_video", "skype_audio", "skype_video", "voipbuster"], "label": 4},
#     {"name": "p2p", "value": [], "label": 5},
#     {"name": "vpn_email", "value": ["vpn_email"], "label": 6},
#     {"name": "vpn_chat", "value": ["vpn_aim_chat", "vpn_facebook_chat",
#                                    "vpn_hangouts_chat", "vpn_icq_chat", "vpn_skype_chat"],
#                                    "label": 7},
#     {"name": "vpn_streaming", "value": ["vpn_netflix", "vpn_spotify",
#                                         "vpn_vimeo", "vpn_youtube"], "label": 8},
#     {"name": "vpn_file", "value": ["vpn_ftps",
#                                    "vpn_sftp", "vpn_skype_files"], "label": 9},
#     {"name": "vpn_voip", "value": ["vpn_facebook_audio",
#                                    "vpn_hangouts_audio", "vpn_skype_audio", "vpn_voipbuster"], "label": 10},
#     {"name": "vpn_p2p", "value": ["vpn_bittorrent"], "label": 11},
# ]
# {"name": "file", "value": ["ftps_down", "ftps_up", "scpDown",
#                            "scpUp", "sftp_down", "sftp_up", "sftpDown", "sftpUp", "skype_file", "scp", "sftp"], "label": 3},
traffic_rules = [
    {"name": "email", "value": ["email", "gmailchat"], "label": 0},
    {"name": "chat", "value": ["aim_chat", "facebook_chat",
                               "hangout_chat", "icq_chat", "skype_chat", "AIMchat", "ICQchat", "facebookchat", "hangouts_chat"], "label": 1},
    {"name": "streaming", "value": [
        "netflix", "spotify", "vimeo", "youtube", "youtubeHTML5"], "label": 2},
    {"name": "file", "value": ["ftps_down", "ftps_up",
                               "sftp_down", "sftp_up", "sftpDown", "sftpUp", "skype_file", "sftp"], "label": 3},
    {"name": "voip", "value": [
        "facebook_audio", "hangouts_audio", "skype_audio", "voipbuster"], "label": 4},
    {"name": "p2p", "value": [], "label": 5},
    {"name": "vpn_email", "value": ["vpn_email"], "label": 6},
    {"name": "vpn_chat", "value": ["vpn_aim_chat", "vpn_facebook_chat",
                                   "vpn_hangouts_chat", "vpn_icq_chat", "vpn_skype_chat"],
     "label": 7},
    {"name": "vpn_streaming", "value": ["vpn_netflix", "vpn_spotify",
                                        "vpn_vimeo", "vpn_youtube"], "label": 8},
    {"name": "vpn_file", "value": ["vpn_ftps",
                                   "vpn_sftp", "vpn_skype_files"], "label": 9},
    {"name": "vpn_voip", "value": ["vpn_facebook_audio",
                                   "vpn_hangouts_audio", "vpn_skype_audio", "vpn_voipbuster"], "label": 10},
    {"name": "vpn_p2p", "value": ["vpn_bittorrent"], "label": 11},
]

app_rules = [
    {'name': 'aim', 'value': ["aim_chat",
                              "AIMchat", "vpn_aim_chat"], 'label': 0},
    {'name': 'bittorrent', 'value': ["vpn_bittorrent"], 'label': 1},
    {'name': 'facebook', 'value': [
        "facebook_chat", "facebook_audio", "facebook_video", "facebookchat",
        "vpn_facebook_audio", "vpn_facebook_chat"], 'label': 2},
    {'name': 'ftps', 'value': ["ftps_down",
                               "ftps_up", "vpn_ftps"], 'label': 3},
    {'name': 'gmail', 'value': ["gmailchat"], 'label': 4},
    {'name': 'hangouts', 'value': [
        "hangout_chat", "hangouts_audio", "hangouts_chat",
        "hangouts_video", "vpn_hangouts_audio", "vpn_hangouts_chat"], 'label': 5},
    {'name': 'icq', 'value': ["icq_chat",
                              "ICQchat", "vpn_icq_chat"], 'label': 6},
    {'name': 'netflix', 'value': ["netflix", "vpn_netflix"], 'label': 7},
    {'name': 'scp', 'value': ["scp", "scpDown", "scpUp"], 'label': 8},
    {'name': 'sftp', 'value': ["sftp_down",
                               "sftp_up", "sftp", "sftpDown", "sftpUp", "vpn_sftp"], 'label': 9},
    {'name': 'skype', 'value': ["skype_audio",
                                "skype_chat", "skype_file", "skype_video",
                                "vpn_skype_audio", "vpn_skype_chat", "vpn_skype_files"], 'label': 10},
    {'name': 'spotify', 'value': ["spotify", "vpn_spotify"], 'label': 11},
    {'name': 'vimeo', 'value': ["vimeo", "vpn_vimeo"], 'label': 12},
    {'name': 'voip', 'value': ["voipbuster", "vpn_voipbuster"], 'label': 13},
    {'name': 'youtube', 'value': ["vpn_youtube",
                                  "youtube", "youtubeHTML5"], 'label': 14},
]

# app_rules = [
#     {'name': 'aim', 'value': ["aim_chat",
#                               "AIMchat"], 'label': 0},
#     {'name': 'email', 'value': ["email"], 'label': 1},
#     {'name': 'facebook', 'value': [
#         "facebook_chat", "facebook_audio", "facebook_video", "facebookchat"], 'label': 2},
#     {'name': 'ftps', 'value': ["ftps_down",
#                                "ftps_up"], 'label': 3},
#     {'name': 'gmail', 'value': ["gmailchat"], 'label': 4},
#     {'name': 'hangouts', 'value': [
#         "hangout_chat", "hangouts_audio", "hangouts_chat",
#         "hangouts_video"], 'label': 5},
#     {'name': 'icq', 'value': ["icq_chat",
#                               "ICQchat"], 'label': 6},
#     {'name': 'netflix', 'value': ["netflix"], 'label': 7},
#     {'name': 'scp', 'value': ["scp", "scpDown", "scpUp"], 'label': 8},
#     {'name': 'sftp', 'value': ["sftp_down",
#                                "sftp_up", "sftp", "sftpDown", "sftpUp"], 'label': 9},
#     {'name': 'skype', 'value': ["skype_audio",
#                                 "skype_chat", "skype_file", "skype_video"], 'label': 10},
#     {'name': 'spotify', 'value': ["spotify"], 'label': 11},
#     {'name': 'vimeo', 'value': ["vimeo"], 'label': 12},
#     {'name': 'voip', 'value': ["voipbuster"], 'label': 13},
#     {'name': 'youtube', 'value': [
#         "youtube", "youtubeHTML5"], 'label': 14},
# ]