import os, shutil, sys
from generate import generate_pages_recursive


def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)




def main():
    dir_path_static = "./static"
    dir_path_public = "./docs"
    dir_path_content = "./content"
    template_path = "./template.html"

    if len(sys.argv) == 1:

        print("Deleting public directory...")
        if os.path.exists(dir_path_public):
            shutil.rmtree(dir_path_public)

        print("Copying static files to public directory...")
        copy_files_recursive(dir_path_static, dir_path_public)

        print("Generating content...")
        generate_pages_recursive(dir_path_content, template_path, dir_path_public)
    else:
        base_path = sys.argv[1]
        generate_pages_recursive(
                dir_path_content,
                template_path,
                dir_path_public,
                base_path
                )


if __name__ == "__main__":
    main()
