from .index import index
from .login import login_get
from .qualifications import (
    get_qualifications_no_selections,
    get_qualifications,
    post_qualifications,
    update_qualifications,
)
from .prisoners import (
    get_all_prisoners,
    get_prisoners_by_name,
    get_prisoners_by_surname,
    get_prisoners_by_company,
    get_prisoners_by_field_redirect,
)
from .job_offers import (
    get_all_jobs,
    get_job_by_id,
    get_jobs_by_field_redirect,
    get_jobs_by_company,
    get_jobs_by_title,
    get_jobs_by_hours_redirect,
    get_jobs_by_hours,
    get_jobs_by_salary_redirect,
    get_jobs_by_salary,
)
