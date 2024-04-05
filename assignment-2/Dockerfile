FROM continuumio/miniconda3:22.11.1

# Make a new conda environment named a2-env
COPY environment.yml ./
RUN conda env create -f environment.yml

# Create an assignment user
RUN echo "conda activate a2-env" >> ~/.bashrc
ENV PATH="$PATH:/opt/conda/envs/a2-env/bin"

RUN useradd -m assignment
USER assignment

WORKDIR /home/assignment

COPY a2_final.ipynb

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0"]
