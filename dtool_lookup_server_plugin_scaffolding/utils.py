from dtool_lookup_server_plugin_scaffolding.config import Config

def config_to_dict(username):
    # TODO: check on privileges
    return Config.to_dict()
