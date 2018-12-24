from xbmcswift2 import Plugin
from resources import megacmd


PLUGIN_NAME = 'MegaCMD'
PLUGIN_ID = 'plugin.video.megacmd'
plugin = Plugin(PLUGIN_NAME, PLUGIN_ID, __file__)


@plugin.route('/<path>')
def route_me(path):
    return index(path=path)


@plugin.route('/')
def index(path='/'):
    megacmd_files = megacmd.list_files(path)
    items = []
    for file_info in megacmd_files:
        item = {
            'label': file_info["name"],
            'thumbnail': None,
            'info': {
                'plot': None
            },
            'is_playable': not file_info["is_dir"] }

        if file_info["is_dir"]:
            item["path"] = plugin.url_for(route_me, path=file_info["path"])
        else:
            item["path"] = file_info["url"]

        xbmc.log(file_info["path"], xbmc.LOGERROR)
        items.append(item)

    return items


if __name__ == '__main__':
    plugin.run()
