PR_DESCRIPTION_TEMPLATE = """
{program_context}

{file_patches}

{ticket_description}

Based on the above information, generate a detailed Pull Request description:
"""

PROGRAM_CONTEXT_TEMPLATE = """"
You will be generating a detailed Pull Request description based on a ticket description and diffs of python files.
"""

FILE_PATCH_TEMPLATE = """
{filename}:

{patch}
"""


TICKET_DESCRIPTION_TEMPLATE = """
Ticket Description:
{ticket_description}
"""

PR_DESCRIPTION_TEMPLATE_WITHOUT_TICKET = """
{program_context}

{patches}

Based on the above diff, generate a detailed Pull Request description:
"""
# Maybe add repository name
PROGRAM_CONTEXT_TEMPLATE = """"
You will be generating a detailed Pull Request description based on diffs of {file_types} file types in this repository:
##########################################################################################################################
"""

FILE_PATCHES_COLLECTION_TEMPLATE = """
{patch_collections}
"""
