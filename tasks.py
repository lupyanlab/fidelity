from invoke import task, run

@task
def install():
    """Install the fidelity R package."""
    run("Rscript -e 'devtools::install()'")
