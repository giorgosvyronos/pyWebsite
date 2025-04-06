import os,shutil,sys
from generate import generate_pages_recursive

def copy_dir(parent_path=".",new_parent="."):
    for item in os.listdir(f"{parent_path}"):
        if not os.path.isfile(f"{parent_path}/{item}"):
            os.mkdir(f"{new_parent}/{item}")
            copy_dir(f"{parent_path}/{item}",f"{new_parent}/{item}")
        else:
            shutil.copy(f"{parent_path}/{item}",f"{new_parent}/{item}")


def main():

    if os.path.isfile("docs"):
        os.remove("docs")

    if os.path.exists("docs"):
        try:
            shutil.rmtree("docs")
        except Exception as e:
            raise Exception(f"Encountered error while trying to remove docs/ : {e}")
    os.makedirs("docs")
    
    if len(sys.argv)==1:
        copy_dir("static", "docs")
        generate_pages_recursive("content","template.html","docs")
    else:
        copy_dir(f"{sys.argv[1]}/static", f"{sys.argv[1]}/docs")
        generate_pages_recursive(f"{sys.argv[1]}/content",f"{sys.argv[1]}/template.html",f"{sys.argv[1]}/docs",f"{sys.argv[1]}")

if __name__ == "__main__":
    main()
