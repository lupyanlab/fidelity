from invoke import task, run

@task
def make():
    """Make the csvs."""
    scripts = [
        'read_messages.py',
        'read_questions.py',
        'read_responses.py',
        'survey_maker.py',
    ]
    for s in scripts:
        run("python scripts/{}".format(s))


@task
def rda():
    """Run the use-data script."""
    run("Rscript data-raw/use-data.R")


@task
def install():
    """Install the fidelity R package."""
    run("Rscript -e 'devtools::install()'")
