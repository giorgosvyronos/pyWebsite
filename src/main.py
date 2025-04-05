import os,shutil
from generate import generate_page

def copy_dir(parent_path=".",new_parent="."):
    for item in os.listdir(f"{parent_path}"):
        if not os.path.isfile(f"{parent_path}/{item}"):
            os.mkdir(f"{new_parent}/{item}")
            copy_dir(f"{parent_path}/{item}",f"{new_parent}/{item}")
        else:
            shutil.copy(f"{parent_path}/{item}",f"{new_parent}/{item}")
            return


def copy_static_to_public():
    if not ".gitignore" in os.listdir("."):
        raise RuntimeError("Not running from root directory of Repository")
    if os.path.isfile("public"):
        os.remove("public")

    if os.path.exists("./public/"):
        try:
            shutil.rmtree("./public/")
        except Exception as e:
            raise Exception(f"Encountered error while trying to remove public/ : {e}")
    os.makedirs("./public/")
    

    copy_dir("./static/", "./public/")

def main():
    copy_static_to_public()
    generate_page("content/index.md","template.html","public/index.html")

if __name__ == "__main__":
    main()
