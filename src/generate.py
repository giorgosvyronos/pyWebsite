import os
from blocktype import markdown_to_html_node
from helpers import extract_title

def generate_page(from_path:str,template_path:str,dest_path:str,base_path:str):
    print(f"Generating page from {base_path}/{from_path} to {base_path}/{dest_path} using {base_path}/{template_path}")
    with open(from_path,encoding="utf-8") as f:
        from_data = f.read()
        f.close()


    with open(template_path,encoding="utf-8") as f:
        template_data = f.read()
        f.close()


    title = extract_title(from_data)
    nodes = markdown_to_html_node(from_data)
    html_result = nodes.to_html()
    template_data = template_data.replace("{{ Title }}",title)
    template_data = template_data.replace("{{ Content }}",html_result)
    # template_data = template_data.replace("href=\"/",f"href=\"{base_path}/")
    # template_data = template_data.replace("src=\"/",f"src=\"{base_path}/")


    with open(dest_path,'w', encoding="utf-8") as f:
        f.write(template_data)
        f.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path,base_path="."):
    for item in os.listdir(dir_path_content):
        if not os.path.isfile(f"{base_path}/{dir_path_content}/{item}"):
            os.mkdir(f"{base_path}/{dest_dir_path}/{item}")
            generate_pages_recursive(
                    f"{base_path}/{dir_path_content}/{item}",
                    template_path,
                    f"{base_path}/{dest_dir_path}/{item}"
                    )
        else:
            if f"{base_path}/{dir_path_content}/{item}".endswith("md"):
                generate_page(
                        f"{base_path}/{dir_path_content}/{item}",
                        template_path,
                        f"{base_path}/{dest_dir_path}/{item}".replace("md","html"),
                        base_path
                    )
