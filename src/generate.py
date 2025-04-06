import os
from blocktype import markdown_to_html_node
from helpers import extract_title

def generate_page(from_path:str,template_path:str,dest_path:str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
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

    with open(dest_path,'w', encoding="utf-8") as f:
        f.write(template_data)
        f.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        if not os.path.isfile(f"{dir_path_content}/{item}"):
            os.mkdir(f"{dest_dir_path}/{item}")
            generate_pages_recursive(
                    f"{dir_path_content}/{item}",
                    template_path,
                    f"{dest_dir_path}/{item}"
                    )
        else:
            if f"{dir_path_content}/{item}".endswith("md"):
                generate_page(
                        f"{dir_path_content}/{item}",
                        template_path,
                        f"{dest_dir_path}/{item}".replace("md","html")
                    )
