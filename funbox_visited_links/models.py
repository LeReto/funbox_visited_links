import re

from pydantic import BaseModel, constr, conlist


class LinksValidator(BaseModel):
    _regexp: str = r"(?:https?:\/\/)?([a-zA-Z0-9.-]+\.[a-z]+)"
    links: conlist(constr(pattern=_regexp), min_length=1)

    def extract_domains(self):
        return {
            re.match(self._regexp, link).group(1)
            for link in self.links
        }
