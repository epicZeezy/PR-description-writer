from langchain_core.prompts import PromptTemplate
from langchain_core.prompts.pipeline import PipelinePromptTemplate
from prompt_templates import *

# Ideally this is passed into function as an argument
CONSTANT_PROGRAM_FILE_TYPES = "python and yaml" 
class GeneratePRDescriptionPromptTemplate:
    def __init__(self):
        self.program_context_prompt = PromptTemplate.from_template(PROGRAM_CONTEXT_TEMPLATE)
        # ticket_description_prompt = PromptTemplate.from_template(TICKET_DESCRIPTION_TEMPLATE)
        self.full_pr_description_prompt = PromptTemplate.from_template(PR_DESCRIPTION_TEMPLATE_WITHOUT_TICKET)
        self.patches_prompt = PromptTemplate.from_template(FILE_PATCHES_COLLECTION_TEMPLATE)
        self.input_prompts = [
            ("program_context", self.program_context_prompt),
            ("patches", self.patches_prompt),
            # ("ticket_description", ticket_description_prompt)
        ]
    def generate_pr_description_prompt(self, file_patches, ticket_description=""):
        pipeline_prompt = PipelinePromptTemplate(
            final_prompt=self.full_pr_description_prompt,
            pipeline_prompts=self.input_prompts
        )
        file_patch_prompt =  PromptTemplate.from_template(FILE_PATCH_TEMPLATE)
        formatted_file_patches = "\n\n".join(file_patch_prompt.format(filename=file["filename"], patch=file["patch"]) for file in file_patches)
        return pipeline_prompt.format(
            patch_collections=formatted_file_patches,
            file_types=CONSTANT_PROGRAM_FILE_TYPES,
            # ticket_description=ticket_description
        )



