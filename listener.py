import requests
import inotify.adapters

def main():
    notify = inotify.adapters.Inotify()
    notify.add_watch("exts")

    for event in notify.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        requests.post("http://server:8443/index_new", json={
            "path": path,
            "filename": filename,
            "type_names": type_names
        })

if __name__ == '__main__':
    main()
